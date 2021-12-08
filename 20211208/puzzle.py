#%%
import csv
from collections import Counter

segments = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9,
}

displays = []

with open("input.csv", "r") as f:
    reader = csv.reader(f, delimiter="\n")
    for i, line in enumerate(reader):
        input, output = line[0].split("|")
        input = input.strip().split(" ")
        output = output.strip().split(" ")
        displays.append((input, output))

output_lengths = [len(digit) for i in displays for digit in i[1]]
output_counter = Counter(output_lengths)
print(
    f"1:{output_counter[2]}, 4:{output_counter[4]}, 7:{output_counter[3]}, 8:{output_counter[7]}"
)


nums = []
for display in displays:
    transform = {}
    input = display[0]
    output = display[1]
    char_count = Counter()
    num_count = {}
    for i, pattern in enumerate(input):
        char_count += Counter(pattern)
        num_count[len(pattern)] = i

    transform["b"] = [i for i in char_count if char_count[i] == 6][0]
    transform["e"] = [i for i in char_count if char_count[i] == 4][0]
    transform["f"] = [i for i in char_count if char_count[i] == 9][0]
    transform["c"] = [i for i in input[num_count[2]] if i not in transform.values()][0]
    transform["a"] = [i for i in input[num_count[3]] if i not in transform.values()][0]
    transform["d"] = [i for i in input[num_count[4]] if i not in transform.values()][0]
    transform["g"] = [
        i for i in ["a", "b", "c", "d", "e", "f", "g"] if i not in transform.values()
    ][0]

    transform = {i: k for k, i in transform.items()}
    output = ["".join(sorted([transform[i] for i in num])) for num in output]
    num = int("".join([str(segments[i]) for i in output]))
    nums.append(num)

print(sum(nums))
