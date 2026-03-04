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

for input_path in input_paths:
    print(input_path, ":")
    with open(input_path, "r") as file:
        sample = file.read()

        s_cache, s_inputs = formatter(sample)
        blank_cache1 = copy.deepcopy(s_cache)
        blank_cache2 = copy.deepcopy(s_cache)

        output_path = f"Output Files/Output_{input_path[18:23]}.txt"
        with open(output_path, "w") as out_file:
            fifo_miss = fifo(s_cache, s_inputs)[1]
            print(f"FIFO  : {fifo_miss}")
            print(f"FIFO  : {fifo_miss}", file = out_file)

            lru_miss = lru(blank_cache1, s_inputs)[1]
            print(f"LRU   : {lru_miss}")
            print(f"LRU   : {lru_miss}", file = out_file)

            optff_miss = optff(blank_cache2, s_inputs)[1]
            print(f"OPTFF : {optff_miss}")
            print(f"OPTFF : {optff_miss}", file = out_file)
    print(f"\n{'*' * 20}\n")