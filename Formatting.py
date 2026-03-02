"""
k m
r1 r2 r3 ... rm
"""
sample = """5 10
1253 120938 1029383 38102938 838428 38102938 838428 1253 120938 1029383
"""

"""
WILL REQUIRE UPDATING LATER TO HANDLE MULTIPLE INPUTS IN THE SAME FILE
"""

def formatter(to_format):
    cache = []
    cache_size_i = to_format.find(' ')
    cache_size = int(to_format[:cache_size_i])
    for i in range(0, cache_size):
        cache.append(float('inf'))

    input_size_i = to_format.find('\n')
    #input_size = int(to_format[:input_size_i])
    ids = to_format[input_size_i + 1:]
    input_ids = ids.split() # change this to accept id's in a for loop up to input size

    return cache, input_ids

if __name__ == "__main__":
    ex_cache, ex_ids = formatter(sample)
    print(f"{ex_cache}\n{ex_ids}")