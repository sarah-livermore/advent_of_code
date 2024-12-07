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

invalid_diffs = 0
for diffs in file_reader('input2.txt'):
    print('diff in question', diffs)
    if False in [abs(i)<=3 and abs(i)>0 for i in diffs] or len(set(i<0 for i in diffs)) > 1:
        print('invalid')
        invalid_diffs+=1

print('num invalid levels', invalid_diffs)