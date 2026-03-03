from Formatting import formatter
from LRU import lru
from FIFO import fifo
from OPTFF import optff
import copy

input_paths = [
    "Input Files/Input_1_050.txt",
    "Input Files/Input_2_100.txt",
    "Input Files/Input_3_150.txt",
]

for path in input_paths:
    print(path, ":")
    with open(path, "r") as file:
        sample = file.read()

        s_cache, s_inputs = formatter(sample)
        blank_cache1 = copy.deepcopy(s_cache)
        blank_cache2 = copy.deepcopy(s_cache)

        print(f"FIFO  : {fifo(s_cache, s_inputs)[1]}")
        print(f"LRU   : {lru(blank_cache1, s_inputs)[1]}")
        print(f"OPTFF : {optff(blank_cache2, s_inputs)[1]}")
    print(f"\n{'*' * 20}\n")