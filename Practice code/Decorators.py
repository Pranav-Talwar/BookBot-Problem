import time

def timer(fn):
    def wrapper (*args, **kwargs):
        start_time = time.time()
        result = fn(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timer
def calculate_sum(n):
    total = 0
    for i in range(n):
        total += i
    return total
print(calculate_sum(1000000))

