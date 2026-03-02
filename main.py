from Formatting import formatter
from LRU import lru
from FIFO import fifo
from OPTFF import optff
import copy

sample = """5 10
1253 120938 1029383 38102938 838428 3512 1253 120938 1029383 38102938"""

s_cache, s_inputs = formatter(sample)
blank_cache1 = copy.deepcopy(s_cache)
blank_cache2 = copy.deepcopy(s_cache)

print(f"FIFO  : {fifo(s_cache, s_inputs)[1]}")
print(f"LRU   : {lru(blank_cache1, s_inputs)[1]}")
print(f"OPTFF : {optff(blank_cache2, s_inputs)[1]}")