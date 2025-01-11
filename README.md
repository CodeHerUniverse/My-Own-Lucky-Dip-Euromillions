# Catarina's README #

Hello! My name is Catarina and I am a current student enrolled in the CFG Degree Data Science Stream course! I am the owner of this Repository and will be maintaining the files provided.
Although not formally qualified, I have been dabling in Python and SQL for about a year and a half.
My current employer is very flexible in terms of letting employees self teach different Technologies and provides many tools for us to do so.
Because of that opportunity to try programming in a work environment I have pursued this CFG opportunity and am very excited to absorb all the knowledge.

## For this Assignment I will be using Github to: ##
+ Push a file I will have added and commited from my local repository.
+ In order to push myself I will also create the README.md file in my local via git and push it into Github.
+ I will also provide a transcript of the git commands used in my local environment as well as any relevant screenshots via this README.md file!
+ Add a .gitignore file
+ Add a requirements.txt file
+ Showcase all that I have learned in my first week of the course!


*Note: I will be using a dummy branch and merge it without a Reviewer just to gather evidence that I can merge a branch - the branch for the Assignment Marker to review, which will have all of the assignment documents, will be labelled as "Assignment_1"*

But first, let me introduce the file I will be using for this assignment.

## My own Lucky Dip ##

As an avid Euromillions player I tend to stick to the 2 x Lucky Dips twice a week. My goal, like many others, is to win the Jackpot and ~~buy 100 cats and a cottage in the woods~~ make the world a better place.
After reading some interesting pages and articles on the nature of numbers, it came to light that due to the nature of the numbers we can choose (1-50) had some quirks. 

For Example:

1. The most common combinations of odds and evens in the main number selection is 3 evens and 2 odds or 2 evens and 3 odds (roughly 50% either way, can only choose 5 numbers)
2. The sum of all 5 main numbers is often >90 of <160 - this is just the nature of the numbers when using a range of 1-50.

I also wanted to gain some practice using the **itertools** and **random** modules in Python so this particular scenario gave me the perfect opportunity. I would create my own Lucky Dip engine, which ensures each "Lucky Dip" is a combination of 3 odds + 2 evens or 2 odds + 3 evens, but the sum of the main numbers is also above or equal to 90 and lower or equal to 160. And thats how ***My_own_lucky_dip_euromillions.py** was born.

But before I get ahead of myself, here is the step-by-step process I have done for this assignment.

## Git Steps (Local) ##

1. Create a folder called __"Assignment 1 Repo"__ - this will be my local git Repository
3. Initialized git
4. Checked for any existing files in that local repository
5. Setup my remote repo origin using the SSH key for this Github Repo.
6. I manually added "My_own_lucky_dip_euromillions.py" into the folder "Assignment 1 Repo". *I will showcase the creation of a file with the README.md file*
7. Checked the git Status
8. Git added my file to the branch assignment_1
9. Checked my git status once more to ensure it worked.
10. ***my git add [filename] didn't work so I used "git add ."***
11. Checked my git status once more to ensure it worked - it did.
12. For the purpose of creating and using a .gitignore file that isn't empty, I added two excel documents:
    - "My Weekly Spend.xlsx" This is a mock file that would track how much I spend vs. the prizes I win - could enhance the code to provide some statistics on my returns and whether some of the patterns in the code impact the outcomes.
    - "Previous Draws Tracker.xlsx" This is also a mock file that would store the previous Draws winning numbers. With this file I could bypass the manual input of the previous Draw winning numbers into my code.
    - As the purpose of my Github is to simply display the Python code and not reveal ALL of my secrets, I will add these files to a gitignore file so they aren't pushed into my Github repo.
13. Created .gitignore file via Gitbash Terminal
14. Edited .gitignore file via Gitbash Terminal and set it to ignore ***ALL*** .xlsx files.
   
    [INSERT IMAGE AFTER PUSH TO GITHUB]
    
17. git added my .gitignore file
18. Checked the git status to see my new files, and to see if excel files are being ignored.
19. Created a requirements.txt file via Gitbash Terminal *Note: I know a requirements.txt file can be created using pip but I wanted to challenge myself and make most of the files via GitBash*
20. Edited requirements.txt file via Gitbash Terminal
   
    [INSERT IMAGE AFTER PUSH TO GITHUB]

21. git added my requirements.txt file
22. Checked my git status to ensure files added successfully.

**The next step is to commit and push my files. Before I do that I will create this README.md file, and will add, commit and push the file into Github. I will resume editing this README.md file directly on Github and add images as well. A second push will be carried out to add the code transcript to this branch. See you in a bit :+1:**

Here is a picture of me creating this README.md file (README-ception OoOooh! :exploding_head:) 

    [INSERT IMAGE AFTER PUSH TO GITHUB]
