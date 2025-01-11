## My own Lucky Dip ##

As an avid Euromillions player I tend to stick to the 2 x Lucky Dips twice a week. My goal, like many others, is to win the Jackpot and ~~buy 100 cats and a cottage in the woods~~ make the world a better place.
After reading some interesting pages and articles on the nature of numbers, it came to light that due to the nature of the numbers we can choose (1-50) had some quirks. 

For Example:

1. The most common combinations of odds and evens in the main number selection is 3 evens and 2 odds or 2 evens and 3 odds (roughly 50% either way, can only choose 5 numbers)
2. The sum of all 5 main numbers is often >90 of <160 - this is just the nature of the numbers when using a range of 1-50.

I also wanted to gain some practice using the **itertools** and **random** modules in Python so this particular scenario gave me the perfect opportunity. I would create my own Lucky Dip engine, which ensures each "Lucky Dip" is a combination of 3 odds + 2 evens or 2 odds + 3 evens, but the sum of the main numbers is also above or equal to 90 and lower or equal to 160. And thats how ***My_own_lucky_dip_euromillions.py** was born.
