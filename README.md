# My own Lucky Dip - Euromillions #

## Overview
As an avid Euromillions player I tend to stick to the 2 x Lucky Dips twice a week. My goal, like many others, is to win the Jackpot and ~~buy 100 cats and a cottage in the woods~~ make the world a better place.
After reading some interesting pages and articles on the nature of numbers, it came to light that due to the nature of the numbers we can choose (1-50) had some quirks. 

I also wanted to gain some practice using the **itertools** and **random** modules in Python so this particular scenario gave me the perfect opportunity. I would create my own Lucky Dip engine, which ensures each "Lucky Dip" is a combination of 3 odds + 2 evens or 2 odds + 3 evens, but the sum of the main numbers is also above or equal to 90 and lower or equal to 160. And thats how ***My_own_lucky_dip_euromillions.py** was born.

***NOTE: In no way does this enhance anyone's chance of winning (trust me - I wish)***

## Features
- **Custom Number Generation:** Generates combinations of numbers based on:
  - **Odds and Evens Distribution:** Ensures each combination contains either 3 evens + 2 odds or 2 evens + 3 odds, which are statistically common patterns.
  - **Sum Constraints:** Filters combinations where the sum of the five main numbers is between 90 and 160.
- **Lucky Star Pairing:** Adds two randomly selected Lucky Star numbers to each main number combination.
- **Avoid Recent Draws:** Includes a check to ensure selected combinations don’t match the latest Euromillions jackpot result.
- **Statistics:** Provides insights into the total number of combinations generated and filtered at two stages of the process.

## How It Works

**Define Inputs:**

  - A predefined list of "lucky numbers" (frequent numbers in past jackpot results).
  - A list of "non-lucky numbers" (less frequent numbers).
  - All possible Lucky Star numbers (1-12).

**Generate Combinations:**

  - All possible combinations of:
    - 3 non-lucky numbers.
    - 2 lucky numbers.
    - 2 Lucky Star numbers.
  
**Apply Filters:**

  - Retain only combinations with a valid odds/evens distribution.
  - Further filter combinations based on their sum constraints (90 ≤ sum ≤ 160).

**Random Selection:**

  - Randomly select two final Lucky Dip combinations from the filtered list.
  
**Validation:**

  - Check the selected combinations against the latest jackpot numbers to avoid duplicates.

**Output:**

  - Display the selected Lucky Dip combinations, along with statistics about the filtering process.

## Installation

Clone this repository:
```
git clone https://github.com/yourusername/my-lucky-dip-euromillions.git
cd my-lucky-dip-euromillions
```
Ensure you have Python installed (version 3.7 or higher).

## Usage
Run the script:
```
python my_own_lucky_dip_euromillions.py
```
Review the generated Lucky Dip combinations displayed in the terminal.

## Example Output
```
Original number of combinations (not including lucky stars): 123456
Trimmed number of combinations (not including lucky stars): 78910
Orignal number of combinations (stars included): 345678
Trimmed number of combinations (stars included): 56789
Selected Lucky Dip combinations: 
[[23, 19, 42, 5, 10, 4, 11], [50, 26, 17, 14, 7, 8, 12]]
Ok to use.
```

## Insights and Learnings
- **Probability Patterns:** The script incorporates statistical trends in lottery draws, such as the tendency for certain odds/evens distributions and sum ranges to appear more frequently.
- **Practical Python:** This project was a great way to practice Python programming, including libraries like itertools and random.
- **Code Optimization:** Handling large combinations efficiently and applying filters demonstrated the importance of performance tuning.

## Limitations

- **No Guaranteed Win:** While this script uses statistical patterns, it **DOES NOT** improve your odds of winning the Euromillions. This is merely a way to practice, and a bit of fun.
- **Fixed Parameters:** The filtering criteria (odds/evens distribution, sum range) are based on observed patterns and might not always reflect future trends.

## Future Enhancements
- **Interactive Input:** Allow users to input their own "lucky" and "non-lucky" numbers.
- **Advanced Filters:** Incorporate additional statistical analyses (e.g., frequency analysis of pairs or triplets).
- **Web Interface:** Develop a web-based version of the tool for broader accessibility.

## License
This project is open-source and available under the MIT License.

## Contact
For questions or feedback, feel free to contact me:

GitHub: CodeHerUniverse
