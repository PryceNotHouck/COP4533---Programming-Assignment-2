import collections
from Formatting import formatter

def optff(cache, inputs_arr):
    hits = 0
    misses = 0
    inputs = collections.deque(inputs_arr)

    while len(inputs):
        input = inputs.popleft()
        if int(input) in cache:
            hits += 1
        else:
            misses += 1
            try:
                empty_i = cache.index(float('inf'))
                cache[empty_i] = int(input)
            except ValueError:
                distances = []  # (id, distance)
                for id in cache:
                    if id != float('inf'):  # i just realized this is redundant but i kind of want to leave it in. little artifact to show that this code is hand written
                        requested = False
                        distance = 0
                        for request in inputs:
                            distance += 1
                            if int(request) == id:
                                requested = True
                                distances.append((id, distance))
                                break
                        if not requested:
                            distances.append((id, float('inf')))

                evict = max(distances, key = lambda x: x[1])[0]
                evict_i = cache.index(evict)
                cache[evict_i] = int(input)

    return hits, misses

if __name__ == "__main__":
    sample = """5 10
    1253 120938 1029383 38102938 838428 3512 1253 120938 1029383 38102938"""

    ex_cache, ex_inputs = formatter(sample)
    hits, misses = optff(ex_cache, ex_inputs)
    print(f"Hits: {hits}\nMisses: {misses}")