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