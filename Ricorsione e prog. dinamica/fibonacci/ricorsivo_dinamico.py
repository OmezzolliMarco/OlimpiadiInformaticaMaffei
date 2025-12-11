import time

def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for i in range(2, n+1):
        a, b = b, a + b
    return b

start = time.perf_counter()
print(fibonacci(50))
stop = time.perf_counter()
print(f"Tempo: {stop-start}")

