import time

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

start = time.perf_counter()
print(fibonacci(30))
stop = time.perf_counter()
print(f"Tempo: {stop-start}")