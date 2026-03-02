import collections
from Formatting import formatter

def lru(cache, inputs_arr):
    hits = 0
    misses = 0
    age = {}

    inputs = collections.deque(inputs_arr)
    while len(inputs):
        input = inputs.popleft()
        if int(input) in cache:
            hits += 1
            age[input] = 0
        else:
            misses += 1
            try:
                empty_i = cache.index(float('inf'))
                cache[empty_i] = int(input)
                age[input] = 0
            except ValueError:  # no empty spot in cache
                oldest = max(age.items(), key = lambda item: item[1])
                evict_i = cache.index(int(oldest[0]))
                cache[evict_i] = int(input)
                age[input] = 0
                del age[oldest[0]]

        for id in age.keys():
            age[id] += 1

    return hits, misses

if __name__ == "__main__":
    sample = """5 10
    1253 120938 1029383 38102938 838428 3512 1253 120938 1029383 38102938"""

    ex_cache, ex_inputs = formatter(sample)
    hits, misses = lru(ex_cache, ex_inputs)
    print(f"Hits: {hits}\nMisses: {misses}")