#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Per-parameter periodicity inference for MSTL + optional debug spectra plots.

Library usage (recommended)
---------------------------
from infer_periods import extractPeriods, plot_periodicity_debug

period_dict = extractPeriods(df_hourly, print_peaks=True, nperseg_opt="full", nfft_mult=16)

plot_periodicity_debug(df_hourly, period_dict, annotate=True, outfile="periodicity_debug.png")
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass
from typing import List, Tuple, Dict, Optional, Iterable, Callable

import numpy as np
import pandas as pd
from scipy.signal import welch, find_peaks, detrend
import matplotlib.pyplot as plt

# change the working directory to the script's directory
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

__all__ = ["extractPeriods", "plot_periodicity_debug"]

# ---------------- Utilities ---------------- #

def _modal_timedelta(index: pd.DatetimeIndex) -> pd.Timedelta:
    if not isinstance(index, pd.DatetimeIndex):
        raise TypeError("Index must be a pandas DateTimeIndex.")
    if len(index) < 2:
        raise ValueError("Need at least two timestamps.")
    diffs = pd.Series(index[1:] - index[:-1], dtype="timedelta64[ns]")
    diffs = diffs[diffs > pd.Timedelta(0)]
    if diffs.empty:
        raise ValueError("Index has no increasing deltas.")
    mode_counts = diffs.value_counts()
    return mode_counts.index[np.argmax(mode_counts.values)]


def _regularise(df: pd.DataFrame, interp_limit: int = 5) -> tuple[pd.DataFrame, pd.Timedelta]:
    if not isinstance(df.index, pd.DatetimeIndex):
        raise TypeError("DataFrame index must be a DateTimeIndex.")
    if len(df.index) < 10:
        raise ValueError("Not enough rows to estimate periods (need >= 10).")

    df = df.sort_index()
    step = _modal_timedelta(df.index)
    uniform_index = pd.date_range(df.index[0], df.index[-1], freq=step)
    df_u = df.reindex(uniform_index)
    df_u = df_u.interpolate(method="time", limit=interp_limit, limit_direction="both")
    return df_u, step


def _local_noise_floor(power: np.ndarray, peak_idx: int, width: int = 50, exclude: int = 3) -> float:
    n = len(power)
    lo = max(0, peak_idx - width)
    hi = min(n, peak_idx + width + 1)
    mask = np.ones(hi - lo, dtype=bool)
    exc_lo = max(lo, peak_idx - exclude)
    exc_hi = min(hi, peak_idx + exclude + 1)
    mask[(exc_lo - lo):(exc_hi - lo)] = False
    window = power[lo:hi][mask]
    if window.size == 0:
        return float(np.median(power))
    return float(np.median(window))


def _parabolic_peak(freqs: np.ndarray, power: np.ndarray, k: int) -> float:
    if k <= 0 or k >= len(power) - 1:
        return float(freqs[k])
    a, b, c = power[k - 1], power[k], power[k + 1]
    denom = (a - 2 * b + c)
    if denom == 0:
        return float(freqs[k])
    delta_bins = 0.5 * (a - c) / denom
    df = freqs[1] - freqs[0]
    return float(freqs[k] + delta_bins * df)


def _resolve_nperseg(n: int, nperseg_opt: str | int) -> int:
    if isinstance(nperseg_opt, str):
        s = nperseg_opt.strip().lower()
        if s == "auto":
            base = max(32, n // 4)
            pw2 = 1 << int(math.log2(min(base, n)))
            return max(32, min(pw2, n))
        if s == "full":
            return max(32, n)
        if s.endswith("%"):
            frac = float(s[:-1]) / 100.0
            return max(32, min(n, int(n * frac)))
        nps = int(float(s))
    else:
        nps = int(nperseg_opt)
    return max(32, min(n, nps))


def _resolve_nfft(nperseg: int, nfft_mult: float) -> int:
    target = max(nperseg, int(nperseg * max(1.0, float(nfft_mult))))
    return 1 << int(math.ceil(math.log2(target)))

# ---------------- Peak container ---------------- #

@dataclass
class PeakInfo:
    period_rows: float     # refined via quadratic interpolation
    snr: float             # power / local-median-power
    prominence: float      # from scipy.signal.find_peaks
    power: float           # PSD value at peak (Welch)
    frequency: float       # cycles per row (refined)

# ---------------- Core spectral routines ---------------- #

def _column_peaks_from_psd(
    y: np.ndarray,
    nperseg: int,
    nfft: int,
    min_period_rows: int,
    max_period_rows: int,
    snr_threshold: float,
    peak_prominence: float,
) -> List[PeakInfo]:
    """
    Welch PSD + peak finding. Returns a list of PeakInfo for peaks that pass:
      - within [min_period_rows, max_period_rows]
      - SNR >= snr_threshold
      - prominence >= max(peak_prominence, 2*median(power))
    """
    y = np.asarray(y, dtype=float)
    if not np.isfinite(y).any() or np.nanstd(y) == 0:
        return []

    med = np.nanmedian(y) if np.isfinite(np.nanmedian(y)) else 0.0
    y = np.where(np.isfinite(y), y, med)
    y = detrend(y, type="linear")

    n = len(y)
    nps = min(nperseg, n)
    if nps < 16:
        return []

    freqs, power = welch(
        y, fs=1.0, nperseg=nps, noverlap=nps // 2,
        nfft=max(nps, nfft), detrend=False, scaling="density"
    )

    valid = (freqs > 0) & np.isfinite(power) & (power > 0)
    freqs = freqs[valid]
    power = power[valid]
    if freqs.size < 8:
        return []

    default_prom = float(np.median(power)) * 2.0
    prom = max(peak_prominence, default_prom)
    peak_idxs, props = find_peaks(power, prominence=prom)

    # Order by period for SNR calc
    periods = 1.0 / freqs
    si = np.argsort(periods)
    periods_sorted = periods[si]
    power_sorted = power[si]

    # map original peak index -> sorted index
    peak_set = set(peak_idxs.tolist())
    map_to_sorted = {orig_idx: k for k, orig_idx in enumerate(si) if orig_idx in peak_set}

    out: List[PeakInfo] = []
    for j, orig_pi in enumerate(peak_idxs):
        k = map_to_sorted[orig_pi]
        f_ref = _parabolic_peak(freqs, power, orig_pi)
        p_rows_ref = 1.0 / f_ref
        if not (min_period_rows <= p_rows_ref <= max_period_rows):
            continue
        noise = _local_noise_floor(power_sorted, k, width=max(10, power_sorted.size // 20), exclude=3)
        snr = float(power_sorted[k] / (noise if noise > 0 else np.finfo(float).eps))
        if snr >= snr_threshold:
            prom_val = float(props["prominences"][j])
            out.append(PeakInfo(
                period_rows=float(p_rows_ref),
                snr=float(snr),
                prominence=prom_val,
                power=float(power[orig_pi]),
                frequency=float(f_ref),
            ))
    return out


def _dedup_and_take_top(
    candidates: List[PeakInfo],
    rel_tol: float,
    max_periods: int,
) -> List[int]:
    """
    From PeakInfo candidates, take up to max_periods by descending SNR,
    de-duplicating within ±rel_tol.
    """
    if not candidates:
        return []
    cands = sorted(candidates, key=lambda p: (-p.snr, p.period_rows))
    chosen: List[float] = []

    def within_tol(a: float, b: float) -> bool:
        tol = max(1.0, rel_tol * max(a, b))
        return abs(a - b) <= tol

    for pk in cands:
        if all(not within_tol(pk.period_rows, q) for q in chosen):
            chosen.append(pk.period_rows)
        if len(chosen) >= max_periods:
            break
    return sorted(int(round(p)) for p in chosen)

# ---------------- Public API ---------------- #
def _merge_close_ints(periods: list[int], rel_tol: float) -> list[int]:
    periods = sorted(periods)
    merged = []
    for p in periods:
        if not merged:
            merged.append(p); continue
        tol = max(1, int(round(rel_tol * max(p, merged[-1]))))
        if abs(p - merged[-1]) > tol:
            merged.append(p)
    return merged

def extractPeriods(
    df: pd.DataFrame,
    *,
    snr_threshold: float = 5.0,
    min_period_rows: int = 2,
    max_period_rows: Optional[int] = None,
    peak_prominence: float = 0.0,
    rel_merge_tol: float = 0.03,
    max_periods: int = 3,
    nperseg_opt: str | int = "auto",
    nfft_mult: float = 8.0,
    refine: bool = True,
    refine_span: float = 0.10,
    refine_grid: int = 101,
    print_peaks: bool = False,
    print_func: Callable[[str], None] = print,
) -> Dict[str, List[int]]:
    """
    Extract per-parameter seasonal periods (in rows) suitable for MSTL.
    Set print_peaks=True to print period, SNR and prominence for each kept peak.
    """
    # print all arguments
    print_func(f"[extractPeriods] df.shape={df.shape}"
               f"snr_threshold={snr_threshold}, min_period_rows={min_period_rows}, "
               f"max_period_rows={max_period_rows}, peak_prominence={peak_prominence}, "
               f"rel_merge_tol={rel_merge_tol}, max_periods={max_periods}, "
               f"nperseg_opt={nperseg_opt}, nfft_mult={nfft_mult}, "
               f"refine={refine}, refine_span={refine_span}, refine_grid={refine_grid}")

    if not isinstance(df.index, pd.DatetimeIndex):
        raise TypeError("df index must be a DateTimeIndex.")

    df_u, step = _regularise(df)

    n = len(df_u)
    if n < 64:
        raise ValueError("Time series too short after regularising (need >= 64 rows).")

    max_pr = max_period_rows if max_period_rows is not None else max(8, n // 2)
    min_pr = max(2, int(min_period_rows))
    if min_pr >= max_pr:
        raise ValueError("min_period_rows must be < max_period_rows.")

    nperseg = _resolve_nperseg(n, nperseg_opt)
    detect_max_pr = min(max_pr, nperseg)
    nfft = _resolve_nfft(nperseg, nfft_mult)

    per_param_periods: Dict[str, List[int]] = {}

    if print_peaks:
        print_func(f"[extractPeriods] cadence ≈ {step}; nperseg={nperseg}, nfft={nfft}; "
                   f"search rows=[{min_pr}, {detect_max_pr}], SNR≥{snr_threshold}, "
                   f"prom≥max({peak_prominence}, 2×medianPSD)")

    for col in df_u.columns:
        series = df_u[col].to_numpy()
        peaks: List[PeakInfo] = _column_peaks_from_psd(
            series,
            nperseg=nperseg,
            nfft=nfft,
            min_period_rows=min_pr,
            max_period_rows=detect_max_pr,
            snr_threshold=snr_threshold,
            peak_prominence=peak_prominence,
        )

        if print_peaks:
            print_func(f"  ── Peaks for {col}:")
            if not peaks:
                print_func("     (none kept)")
            else:
                # order by increasing period for readability
                for pk in sorted(peaks, key=lambda p: p.period_rows):
                    hrs = float(step / pd.Timedelta(hours=1)) * pk.period_rows
                    print_func(f"     P={pk.period_rows:7.1f} rows (~{hrs:8.0f} h) | "
                               f"SNR={pk.snr:7.2f} | prom={pk.prominence:9.3g} | "
                               f"power={pk.power:9.3g}")

        chosen = _dedup_and_take_top(peaks, rel_tol=rel_merge_tol, max_periods=max_periods)

        if refine and chosen:
            refined: List[int] = []
            # simple per-column harmonic refine reusing the series
            y = np.asarray(series, float)
            y = np.where(np.isfinite(y), y, np.nanmedian(y))
            y = detrend(y, type="linear")
            for p in chosen:
                pmin = p * (1.0 - refine_span); pmax = p * (1.0 + refine_span)
                grid = np.linspace(max(2.0, pmin), pmax, int(refine_grid))
                best_p, best_err = p, np.inf
                for P in grid:
                    w = 2*np.pi / P
                    t = np.arange(len(y), dtype=float)
                    X = np.column_stack([np.sin(w*t), np.cos(w*t), np.ones_like(t)])
                    coef, _, _, _ = np.linalg.lstsq(X, y, rcond=None)
                    err = float(np.nanmean((y - X @ coef)**2))
                    if err < best_err:
                        best_err, best_p = err, P
                refined.append(int(round(best_p)))
            # de-dup again
            refined = _merge_close_ints([int(round(p)) for p in refined], rel_merge_tol)
            chosen = refined or chosen

        per_param_periods[str(col)] = chosen

    return per_param_periods

# ---------------- Debug plotting (optional) ---------------- #

def plot_periodicity_debug(
    df: pd.DataFrame,
    selected_periods_by_col: Dict[str, List[int]],
    *,
    snr_threshold: float = 5.0,
    min_period_rows: int = 2,
    max_period_rows: Optional[int] = None,
    peak_prominence: float = 0.0,
    nperseg_opt: str | int = "auto",
    nfft_mult: float = 8.0,
    outfile: Optional[str] = None,
    annotate: bool = True,
    label_max: int = 8,
) -> None:
    df_u, step = _regularise(df)
    n = len(df_u)
    if max_period_rows is None:
        max_period_rows = max(8, n // 2)
    nperseg = _resolve_nperseg(n, nperseg_opt)
    plot_max_pr = min(max_period_rows, nperseg)
    nfft = _resolve_nfft(nperseg, nfft_mult)

    ncols = len(df_u.columns)
    if ncols == 0:
        return
    grid_cols = min(3, ncols)
    grid_rows = int(np.ceil(ncols / grid_cols))
    fig, axes = plt.subplots(grid_rows, grid_cols, figsize=(5 * grid_cols, 3.9 * grid_rows), squeeze=False)
    axes = axes.flatten()

    for i, col in enumerate(df_u.columns):
        ax = axes[i]
        y = df_u[col].to_numpy()

        seg = min(nperseg, len(y))
        freqs, power = welch(
            detrend(np.where(np.isfinite(y), y, np.nanmedian(y)), type="linear"),
            fs=1.0, nperseg=seg, noverlap=seg // 2, nfft=max(seg, nfft),
            detrend=False, scaling="density"
        )

        valid = (freqs > 0) & np.isfinite(power) & (power > 0)
        freqs = freqs[valid]
        power = power[valid]
        periods = 1.0 / freqs

        si = np.argsort(periods)
        periods = periods[si]
        power = power[si]
        freqs = freqs[si]

        ax.plot(periods, power, lw=1.2)
        ax.set_title(str(col))
        ax.set_xlabel("Period (rows)")
        ax.set_ylabel("Power (Welch PSD)")
        ax.grid(True, alpha=0.3)
        ax.set_xlim(left=min_period_rows, right=plot_max_pr)

        default_prom = float(np.median(power)) * 2.0
        prom_threshold = max(peak_prominence, default_prom)
        peak_idxs, props = find_peaks(power, prominence=prom_threshold)

        kept_info = []
        for j, k in enumerate(peak_idxs):
            f_ref = _parabolic_peak(freqs, power, k)
            p_rows = 1.0 / f_ref
            if not (min_period_rows <= p_rows <= plot_max_pr):
                continue
            noise = _local_noise_floor(power, k, width=max(10, power.size // 20), exclude=3)
            snr = float(power[k] / (noise if noise > 0 else np.finfo(float).eps))
            if snr >= snr_threshold:
                prom_val = float(props["prominences"][j])
                kept_info.append((p_rows, power[k], snr, prom_val))

        if kept_info:
            ax.scatter([p for (p, *_ ) in kept_info],
                       [y for (_, y, *_ ) in kept_info],
                       marker="o", s=22)

        if annotate and kept_info:
            kept_info.sort(key=lambda t: (-t[2], t[0]))
            for (p_rows, pwr, snr, prom_val) in kept_info[:max(1, int(label_max))]:
                label = f"P={int(round(p_rows))} r, SNR={snr:.1f}, prom={prom_val:.2g}"
                ax.annotate(label, xy=(p_rows, pwr), xytext=(6, 4),
                            textcoords="offset points", fontsize=8, rotation=20, alpha=0.85)

        for sp in selected_periods_by_col.get(str(col), []):
            ax.axvline(sp, linestyle="--", linewidth=1.2)
            if annotate:
                ax.annotate(f"sel {sp} r", xy=(sp, ax.get_ylim()[1]),
                            xytext=(2, -14), textcoords="offset points",
                            fontsize=8, ha="left", va="top", rotation=90, alpha=0.8)

        ax.text(0.01, 0.97,
                f"SNR≥{snr_threshold:g}, prom≥{prom_threshold:.2g}\n"
                f"nperseg={nperseg}, nfft={nfft}",
                transform=ax.transAxes, va="top", ha="left",
                fontsize=8, alpha=0.7)

        try:
            sec = ax.secondary_xaxis(
                "top",
                functions=(
                    lambda rows: rows * (step / pd.Timedelta(hours=1)),
                    lambda hours: hours / (step / pd.Timedelta(hours=1)),
                ),
            )
            sec.set_xlabel("Approx period (hours)")
        except Exception:
            pass

    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    fig.suptitle(
        "Per-parameter periodicity debug spectra "
        f"(cadence ≈ {step}; longest resolvable period ≈ {nperseg} rows)",
        y=0.995
    )
    fig.tight_layout(rect=[0, 0.02, 1, 0.95])

    if outfile:
        fig.savefig(outfile, dpi=150)
    try:
        plt.show()
    except Exception:
        pass

# ---------------- CLI ---------------- #

def _load_pickle_df(path: str) -> pd.DataFrame:
    obj = pd.read_pickle(path)
    if isinstance(obj, pd.DataFrame):
        return obj
    elif isinstance(obj, dict) and "df" in obj and isinstance(obj["df"], pd.DataFrame):
        return obj["df"]
    else:
        raise TypeError("Pickle did not contain a pandas DataFrame (or {'df': DataFrame}).")


def main():
    default_pickle = "data/eyebrook/df_hourly.pickle"

    ap = argparse.ArgumentParser(description="Infer MSTL periods per parameter (rows) and plot debug spectra.")
    ap.add_argument("--pickle", "-p", default=default_pickle,
                    help=f"Path to a pickle file containing a pandas DataFrame (default: {default_pickle}).")
    ap.add_argument("--snr", type=float, default=300.0, help="SNR threshold for peak inclusion.")
    ap.add_argument("--min-period", type=int, default=4, help="Minimum period in rows.")
    ap.add_argument("--max-period", type=int, default=int(1.5*24*365), help="Maximum period in rows.")
    ap.add_argument("--rel-merge", type=float, default=0.1, help="Relative merge tolerance.")
    ap.add_argument("--max-periods", type=int, default=3, help="Max periods to return per parameter.")
    ap.add_argument("--prom", type=float, default=1000, help="Peak prominence for find_peaks (0 => auto).")
    ap.add_argument("--nperseg", default="full",
                    help='Welch window length. Examples: 12000, "full", "50%%", or "auto" (default).')
    ap.add_argument("--nfft-mult", type=float, default=8.0, help="Zero-padding multiplier for Welch nfft (default: 8.0).")
    ap.add_argument("--no-refine", action="store_true", help="Disable harmonic regression refinement (per parameter).")
    ap.add_argument("--refine-span", type=float, default=0.20, help="±span for harmonic refinement (fraction of period).")
    ap.add_argument("--refine-grid", type=int, default=201, help="Grid points for refinement scan.")
    ap.add_argument("--out", type=str, default="periodicity_debug.png", help="Output PNG for spectra plot.")
    ap.add_argument("--no-annotate", action="store_true", help="Disable text labels on peaks/lines.")
    ap.add_argument("--label-max", type=int, default=8, help="Max annotated peaks per panel.")
    # --- replace your existing --print-peaks arg with this ---
    grp = ap.add_mutually_exclusive_group()
    grp.add_argument("--print-peaks", dest="print_peaks",
                    action="store_true", default=True,
                    help="Print SNR/prominence for kept peaks (default: on).")
    grp.add_argument("--no-print-peaks", dest="print_peaks",
                    action="store_false",
                    help="Disable printing of peak SNR/prominence.")

    args = ap.parse_args()

    df = _load_pickle_df(args.pickle)

    periods_by_param = extractPeriods(
        df,
        snr_threshold=args.snr,
        min_period_rows=args.min_period,
        max_period_rows=(args.max_period if args.max_period > 0 else None),
        peak_prominence=args.prom,
        rel_merge_tol=args.rel_merge,
        max_periods=args.max_periods,
        nperseg_opt=args.nperseg,
        nfft_mult=args.nfft_mult,
        refine=(not args.no_refine),
        refine_span=args.refine_span,
        refine_grid=args.refine_grid,
        print_peaks=args.print_peaks,
    )

    df_u, _ = _regularise(df)
    n = len(df_u)
    max_pr_for_plot = args.max_period if args.max_period > 0 else max(8, n // 2)

    print("MSTL periods per parameter (rows):")
    for k, v in periods_by_param.items():
        print(f"  {k}: {v}")

    plot_periodicity_debug(
        df=df,
        selected_periods_by_col=periods_by_param,
        snr_threshold=args.snr,
        min_period_rows=args.min_period,
        max_period_rows=max_pr_for_plot,
        peak_prominence=args.prom,
        nperseg_opt=args.nperseg,
        nfft_mult=args.nfft_mult,
        outfile=args.out,
        annotate=(not args.no_annotate),
        label_max=args.label_max,
    )
    print(f"Saved spectra plot to: {args.out}")


if __name__ == "__main__":
    main()