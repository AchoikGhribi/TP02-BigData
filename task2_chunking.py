# ============================================================
# TASK 2: Pandas Chunking
# ============================================================
import pandas as pd
import psutil
import time

CHUNK_SIZE = 100_000

print("=" * 60)
print(f"TASK 2: Pandas Chunking (chunksize={CHUNK_SIZE:,})")
print("=" * 60)

mem = psutil.virtual_memory()
print(f"\nRAM Before: {mem.percent}%")

start = time.time()
total_rows = 0
n_chunks = 0

for chunk in pd.read_csv("train.csv", chunksize=CHUNK_SIZE):
    n_chunks += 1
    total_rows += len(chunk)
    mem = psutil.virtual_memory()
    print(f"Chunk {n_chunks} | Rows: {total_rows:,} | RAM: {mem.percent}% | Time: {time.time()-start:.1f}s")

elapsed = time.time() - start
print(f"\nChunking Complete!")
print(f"   Total rows: {total_rows:,}")
print(f"   Time: {elapsed:.2f}s")
print(f"   RAM: {psutil.virtual_memory().percent}%")