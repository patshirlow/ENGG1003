import time

N = 1_000_000
REPEATS = 5

def time_loop_sum():
    times = []
    for _ in range(REPEATS):
        start = time.perf_counter()
        total = 0
        for i in range(1, N + 1):
            total += i
        end = time.perf_counter()
        times.append(end - start)
    return times

def time_builtin_sum():
    times = []
    for _ in range(REPEATS):
        start = time.perf_counter()
        total = sum(range(1, N + 1))
        end = time.perf_counter()
        times.append(end - start)
    return times

# Run timings
loop_times = time_loop_sum()
builtin_times = time_builtin_sum()

# Print results
print("Loop approach times:")
for t in loop_times:
    print(f"{t:.6f} seconds")
print(f"Average: {sum(loop_times)/REPEATS:.6f} seconds\n")

print("Built‑in sum(range) times:")
for t in builtin_times:
    print(f"{t:.6f} seconds")
print(f"Average: {sum(builtin_times)/REPEATS:.6f} seconds")