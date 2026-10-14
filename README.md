# TP02: How to Work with Big Data Files (5GB+)

**University of Eloued - Big Data Analytics**
**GHRIBI ACHOIK - Groupe 1**

## Objective
Compare 3 methods for reading a 5.33 GB CSV file.

## Files
- `task1_oom.py` — Pandas OOM Challenge
- `task2_chunking.py` — Pandas Chunking
- `task3_dask.py` — Dask DataFrame
- `report.pdf` — Full report

## Results
| Method | RAM | Time | Status |
|--------|-----|------|--------|
| Pandas | 100% | 160s | ❌ OOM |
| **Chunking** | **40-43%** | **104.93s** | ✅ **Best** |
| Dask | 36.2% | 270.96s | ✅ |

## Why Chunking is Best ?
1. Fastest: 104.93s (2.5× faster than Dask)
2. Constant RAM: 40-43%
3. Ideal for HDD
4. Simple: 3 lines
5. No overhead
6. Reliable

## Dataset
Source: [Kaggle - CMI Precompute Features](https://www.kaggle.com/datasets/urvishp80/cmi-precompute-features)