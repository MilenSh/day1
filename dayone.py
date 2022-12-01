import os
import io

def max_calories(input_file,elves_amount):
    total = [0]
    with io.open(input_file,"r") as input:
        for line in input:
            if line is os.linesep:
                total.append(0)
            else:
                total[-1] += int(line)
    total.sort(reverse=True)
    print(f'Max cal: {sum(total[:elves_amount])}')

max_calories("input.txt", 1)
max_calories("input.txt", 3)