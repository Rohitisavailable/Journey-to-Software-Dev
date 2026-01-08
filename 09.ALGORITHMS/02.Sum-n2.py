import time

def sum(n: int) -> int:
    result = 0
    for i in range(n + 1):
        result += i
    return result
def sum_optimized(n: int) -> int:
    return n * (n + 1)/2


ranges = (100, 1000, 10000, 10000)

print("\nMeasuring optimized()")
for n in ranges:
    start = time.process_time_ns()
    sum(n)
    end = time.process_time_ns()
    exec_time = end - start
    print(f"sum ({n}) execution time: {exec_time} ns")

print("\nMeasuring sum_optimized()")

for n in ranges:
    start = time.process_time_ns()
    sum_optimized(n)
    end = time.process_time_ns()
    exec_time = end - start
    print(f"sum_optimized ({n}) execution time: {exec_time} ns")