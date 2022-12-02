# The input file represents the Calories of the food carried by the Elves:
# In case the Elves get hungry and need extra snacks, they need to know which Elf to ask, they'd like to know how many
# Calories are being carried by the Elf carrying the most Calories. Find the Elf carrying the most Calories. How many
# total Calories is that Elf carrying?

with open('./input/Day1.txt', 'r') as file:
    lines = file.readlines()

# part 1
elves = [[]]
for line in lines:
    cals = line.strip()
    if not cals:
        elves.append([])
    else:
        elves[-1].append(int(cals))

cal_totals = []
for elf in elves:
    cal_totals.append(sum(elf))

most_cals = max(cal_totals)
elf = cal_totals.index(most_cals)
print(f'Elf #{elf} is carrying {most_cals} Calories.')

# part 2
# By the time you calculate the answer to the Elves' question, they've already realized that the Elf carrying the most
# Calories of food might eventually run out of snacks. To avoid this unacceptable situation, the Elves would instead
# like to know the total Calories carried by the top three Elves carrying the most Calories. That way, even if one of
# those Elves runs out of snacks, they still have two backups. Find the top three Elves carrying the most Calories.
# How many Calories are those Elves carrying in total?

cal_totals = sorted(cal_totals, reverse=True)
total_cals = sum(cal_totals[:3])
print(f'The total Calories of the top 3 elves is: {total_cals}')
