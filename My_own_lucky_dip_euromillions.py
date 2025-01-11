import random
from itertools import combinations
import numpy as np

#List of numbers that have been selected in Jackpot combinations the most as of 30/08/2024
lucky_numbers = [23, 44, 19, 21, 50, 42, 17, 26, 10, 37, 29, 20, 38, 35, 27, 15, 25]
#remaining numbers - not so lucky
non_lucky_numbers =[45, 5, 7, 12, 14, 34, 13, 11, 4, 16, 30, 49, 24, 39, 3, 28, 6, 48, 1, 31, 2, 32, 9, 36, 43, 44, 8, 18, 47, 46, 41, 33, 22]
#list of star numbers
stars =[1,2,3,4,5,6,7,8,9,10,11,12]

#Empty list variables
semi_final_list = []
test_list = []
final_list = []

#all possible combinations of 3 individual non lucky numbers
combinations_set1 = list(combinations(non_lucky_numbers, 3))
#all possible combinations of 2 individual lucky numbers
combinations_set2 = list(combinations(lucky_numbers, 2))
#all possible combinations of 2 stars
combinations_set3 = list(combinations(stars, 2))

#all the possible combinations of each unique set of 3 non lucky numbers with each unique set of 2 lucky numbers
result_combinations = [(c1,c2) for c1 in combinations_set1 for c2 in combinations_set2]

#For each list of lists, flatten
for combination in result_combinations:
    flat_list = [num for sublist in combination for num in sublist]
    #empty variables to count the number of evens and odds
    even_count, odd_count = 0, 0
    #for each number in the flat list, add them to the tally of evens or odds
    for num in flat_list:
        if num % 2 ==0:
            even_count += 1
        else:
            odd_count += 1
    #if the combination of numbers is 2 odds and 3 evens or 3 odds and 2 evens then append to a final list after sorting
    if even_count ==2 and odd_count ==3 or even_count == 3 and odd_count ==2:
        flat_list.sort()
        semi_final_list.append(flat_list)

#some statistics about the number of orignal combinations vs. the number of combinations after the odds and evens parameters have been set.
print("Original number of combinations (not including lucky stars):", len(result_combinations))
print("Trimmed number of combinations (not including lucky stars):", len(semi_final_list))

#shuffle for extra randomness
random.shuffle(semi_final_list)

#combine the chosen combinations of main numbers with the random pairings of stars
numbers_and_stars = [(f1,c3) for f1 in semi_final_list for c3 in combinations_set3]

#for each final combination, append them to a final list if the sum of their numbers is more than 90 and less than 160
for final_combination in numbers_and_stars:
    flat_numbers_and_stars = [num for sublist in final_combination for num in sublist]
    if sum(flat_numbers_and_stars)>=90 and sum(flat_numbers_and_stars)<=160:
        final_list.append(flat_numbers_and_stars)

#select our final choice - 2 lucky dips
final_choice = random.sample(final_list, k=2)
print(final_choice)

#to ensure we are not using the same numbers as the latest draw, this is a check to ensure that our chosen random number doesn't match the last jackpot numbers
last_result = [1,8,11,42,47,4,11]
if any(list == last_result for list in final_choice):
    print("Matches previous results. Re-run code.")
else:
    print("Ok to use.")

#one final set of statistics to show the total number of combinations before the sum >90 and sum<160 parameters, and the total number of combinations after.
print("Orignal number of combinations (stars included):",len(numbers_and_stars))
print("Trimmed number of combinations (stars included):",len(final_list))