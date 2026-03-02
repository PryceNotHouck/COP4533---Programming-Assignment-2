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
        else:
            misses += 1
            assigned = False
            for i in range(0, len(cache)):
                if cache[i] == float('inf'):
                    cache[i] = int(input)
                    age[input] = 0
                    assigned = True
                    break
            if not assigned:
                oldest = (-1, 0)
                for id in age.keys():
                    if age[id] >= oldest[1]:
                        oldest = (id, age[id])
                for i in range(0, len(cache) - 1):
                    if cache[i] == int(oldest[0]):
                        cache[i] = int(input)
                        age[input] = 0
                        break
                del age[oldest[0]]

        for id in age.keys():
            age[id] += 1

    return hits, misses

if __name__ == "__main__":
    sample = """5 10
    1253 120938 1029383 38102938 838428 3512 1253 120938 1029383 38102938
    """

    ex_cache, ex_inputs = formatter(sample)
    hits, misses = lru(ex_cache, ex_inputs)
    print(f"Hits: {hits}\nMisses: {misses}")