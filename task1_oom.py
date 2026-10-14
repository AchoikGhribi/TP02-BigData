# ============================================================
# TASK 1: Traditional Failure (OOM Challenge)
# ============================================================
import pandas as pd
import psutil
import time

print("=" * 60)
print("TASK 1: Traditional Failure (OOM Challenge)")
print("=" * 60)

mem = psutil.virtual_memory()
print(f"\nRAM Before: {mem.percent}% ({mem.used/1024**3:.1f} GB / {mem.total/1024**3:.1f} GB)")

print("\nAttempting to load train.csv with pd.read_csv()...")
print("This will likely CRASH with MemoryError!\n")

start = time.time()

try:
    df = pd.read_csv("train.csv", low_memory=False)
    elapsed = time.time() - start
    print(f"\nLoaded in {elapsed:.2f}s")
    print(f"   Rows: {len(df):,}")
    print(f"   Columns: {len(df.columns)}")
except MemoryError as e:
    elapsed = time.time() - start
    print(f"\nMemoryError after {elapsed:.2f}s!")
    print(f"   {e}")
except Exception as e:
    elapsed = time.time() - start
    print(f"\nError after {elapsed:.2f}s: {type(e).__name__}")
    print(f"   {e}")

mem = psutil.virtual_memory()
print(f"\nRAM After: {mem.percent}% ({mem.used/1024**3:.1f} GB)")

print("\n" + "=" * 60)
print("CONCLUSION: Standard pandas cannot handle 5GB files!")
print("=" * 60)