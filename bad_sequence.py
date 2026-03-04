from LRU import lru
from FIFO import fifo
from OPTFF import optff
from Formatting import formatter
from numpy import random
import copy

def bad_sequence():
    lru_miss = 0
    fifo_miss = 0
    optff_miss = 1
    attempt_count = 1

    while optff_miss >= fifo_miss and optff_miss >= lru_miss:
        print(f"Attempt {attempt_count}")

        attempt = f"3 50\n"
        requests = []

        for i in range(5):
            special = random.randint(100000, 999999)
            for j in range(5):
                requests.append(special)

        for i in range(25):
            id = random.randint(100000, 999999)
            requests.append(id)
        random.shuffle(requests)

        for req in requests:
            attempt += f"{req} "
        attempt = attempt[:-1]

        attempt_cache, attempt_ids = formatter(attempt)
        blank_cache1 = copy.deepcopy(attempt_cache)
        blank_cache2 = copy.deepcopy(attempt_cache)

        lru_miss = lru(attempt_cache, attempt_ids)[1]
        fifo_miss = fifo(blank_cache1, attempt_ids)[1]
        optff_miss = optff(blank_cache2, attempt_ids)[1]

        if optff_miss < lru_miss and optff_miss < fifo_miss:
            print("Success\n")
            print(f"FIFO  : {fifo_miss}")
            print(f"LRU   : {lru_miss}")
            print(f"OPTFF : {optff_miss}\n")

            return attempt
        else:
            attempt_count += 1
            print("Failure\n")


if __name__ == "__main__":
    print(bad_sequence())