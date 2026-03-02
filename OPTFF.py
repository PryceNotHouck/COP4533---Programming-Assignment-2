import collections
from Formatting import formatter

def optff(cache, inputs_arr):
    hits = 0
    misses = 0
    inputs = collections.deque(inputs_arr)

    while len(inputs):
        input = inputs.popleft()

    return hits, misses

if __name__ == "__main__":
    sample = """5 10
    1253 120938 1029383 38102938 838428 3512 1253 120938 1029383 38102938"""

    ex_cache, ex_inputs = formatter(sample)
    hits, misses = optff(ex_cache, ex_inputs)
    print(f"Hits: {hits}\nMisses: {misses}")