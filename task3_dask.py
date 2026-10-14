# ============================================================
# TASK 3: Dask DataFrame (OPTIMIZED)
# ============================================================
import dask.dataframe as dd
import psutil
import time

print("=" * 60)
print("TASK 3: Dask DataFrame")
print("=" * 60)

mem = psutil.virtual_memory()
print(f"\nRAM Before: {mem.percent}% ({mem.used/1024**3:.2f} GB)")

print("\n[LAZY] Creating Dask DataFrame...")
start = time.time()

ddf = dd.read_csv("train.csv", blocksize="2GB")

print(f"   Done in {time.time()-start:.3f}s")
print(f"   Partitions: {ddf.npartitions}")
print(f"   RAM: {psutil.virtual_memory().percent}%")

print("\n[LAZY] Building graph...")
total_rows = ddf.shape[0]

print("\n[COMPUTE] Now executing...")
compute_start = time.time()
rows_result = total_rows.compute()
compute_time = time.time() - compute_start

print(f"\nDask Complete!")
print(f"   Total rows: {rows_result:,}")
print(f"   Compute time: {compute_time:.2f}s")
print(f"   Total time: {time.time()-start:.2f}s")
print(f"   RAM: {psutil.virtual_memory().percent}%")