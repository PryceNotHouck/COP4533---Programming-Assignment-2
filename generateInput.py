import math
from numpy import random


# trying cache size as square root of request size. no rigorous reason for this but it seems reasonable/representative
def generator(path, n_requests, temperature):
    with open(path, "w") as file:
        output = f"{int(math.sqrt(n_requests))} {n_requests}\n"
        requests = []

        # temperature controls how many times a certain frequent spread is present, default is 10% of total
        id = random.randint(100000, 999999)
        for i in range(temperature):
            requests.append(id)

        for i in range(n_requests):
            id = random.randint(100000, 999999)
            requests.append(id)

        random.shuffle(requests)
        for req in requests:
            output += f"{req} "
        output = output[:-1]  # remove last whitespace character
        file.write(output)
    return path

if __name__ == "__main__":
    path1 = r"Input Files/Input_1_050.txt"
    path2 = r"Input Files/Input_2_100.txt"
    path3 = r"Input Files/Input_3_150.txt"

    print(generator(path1, 50, 5))
    print(generator(path2, 100, 10))
    print(generator(path3, 150, 15))