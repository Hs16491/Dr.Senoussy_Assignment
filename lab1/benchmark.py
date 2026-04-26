# benchmark.py
import requests, time, concurrent.futures, statistics

URL = "http://localhost:5000/"
NUM_REQUESTS = 100
CONCURRENCY = 10

def fetch(_):
    start = time.time()
    requests.get(URL)
    return time.time() - start

with concurrent.futures.ThreadPoolExecutor(max_workers=CONCURRENCY) as ex:
    latencies = list(ex.map(fetch, range(NUM_REQUESTS)))

latencies.sort()
print(f"Mean:    {statistics.mean(latencies)*1000:.1f} ms")
print(f"Median:  {statistics.median(latencies)*1000:.1f} ms")
print(f"P90:     {latencies[int(0.90*len(latencies))]*1000:.1f} ms")
print(f"P99:     {latencies[int(0.99*len(latencies))]*1000:.1f} ms")
print(f"Max:     {max(latencies)*1000:.1f} ms")