# to solve advent of code 2024 puzzles
# Sarah Livermore 2024-12-03

with open('input.txt') as file:
    input_data = file.readlines()

list_of_rows = [row.split() for row in input_data]

first_ids = [int(row[0]) for row in list_of_rows]

second_ids = [int(row[1]) for row in list_of_rows]

# sort both lists of IDs, smallest first
first_ids.sort()
second_ids.sort()

# find the distance between each ID pair - direction does not matter
id_diffs = [abs(id_1-id_2) for id_1,id_2 in zip(first_ids, second_ids)]

# total distance
total_dist = sum(id_diffs)
print('Total distance between all ID pairs: ', total_dist)

# DAY 2, PART 1 - LEVELS

def file_reader(file):
    with open(file) as f:
        for line in f:
            levels = line.split(' ')
            levels = [int(l) for l in levels]
            diffs = [t-s for s,t in zip(levels, levels[1:])]
            yield diffs

valid_diffs = 0
for diffs in file_reader('input2.txt'):
    if any(d==0 for d in diffs):
        continue
    if len(set(map(lambda x: x>0, diffs)))==1:
        if all(abs(d)>=1 and abs(d)<=3 for d in diffs):
            valid_diffs+=1

print('num valid levels', valid_diffs)

# DAY 2, PART 2

# DAY 3
import re

test_string = "-select()&how()''from()}what()mul(667,142);*when()*/%%+ &mul(139,116),,)mul(665,813)$>-+from()where(),from()mul(589,293))mul(832,177)mul(701,929)~([mul(300,986)from()mul(238,716)/~*~'what()when():}mul(437,789)mul(662,564)*)^,;%<}#'mul(567,346)"

with open('input3_mul.txt') as f:
    muls_string = f.read()
    muls = re.findall('mul\(\d{1,3},\d{1,3}\)', muls_string)

    sum_of_products = 0
    for m in muls:
        numbers = m[4:-1].split(',')
        product = int(numbers[0])*int(numbers[1])
        sum_of_products += product

    print('Sum of products: ', sum_of_products)
