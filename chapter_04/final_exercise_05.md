# Final Exercise 05 - Spark RDD Exercises with Joker and Batman :black_joker: :bat:

## Overview
Welcome to the Spark RDD Exercises with a Joker and Batman twist! In this exercise session, you will tackle various Spark RDD. These exercises will help you sharpen your skills in Spark's core data structure and processing model. RDDs are your trusted allies in the world of Spark, and mastering them is essential for conquering big data challenges.

## Exercise 1: The Joker's Challenge - Calculate Factorial
The Joker has a mathematical puzzle for you! Write a Spark program that receives a number `N` and returns its factorial. Can you solve the Joker's riddle?

## Exercise 2: Batman's Mission - Filter and Sort Numbers
Batman is on a mission to clean up Gotham City. Write a Spark program that receives four integers `X1`, `X2`, `Y1`, and `Y2`. Your mission, should you choose to accept it:
   - Find all the numbers between `X1` and `X2` that can be divided by 3.
   - Find all the numbers between `Y1` and `Y2` that can be divided by 4.
   - Remove any criminal duplicates.
   - Sort the numbers in ascending order and restore peace to the city.

## Exercise 3: Joker's Mischief - Count Email Addresses
The Joker is causing chaos with spam emails! Write a Spark program that loads files from [./dataset/fake_spam_dataset.csv](./dataset/fake_spam_dataset.csv) and prints how many email addresses there are in the files for each email provider. The Joker is trying to trick you with his spam emails. Can you foil his plans?

## Exercise 4: The Battle of Broadcast - Find Common Soldier Names
In the dark and chaotic streets of Gotham City, the Joker is hatching a sinister plan to create chaos and confusion. He has enlisted his loyal henchmen, known as the "Joker's Henchclowns," while Batman has gathered his trusted allies, known as the "Gotham Protectors."

Your mission, should you choose to accept it, is to uncover the spies who secretly serve both the Joker and Batman. You have two lists: one containing the names of the Joker's Henchclowns and the other containing the names of the Gotham Protectors. Your task is to identify the double agents who appear on both lists.

To achieve this mission and save Gotham City from impending chaos, you must harness the power of broadcast variables. Make a strategic decision about which side to broadcast and why. The fate of Gotham hangs in the balance, and only you can thwart the Joker's sinister plan!

Good luck, detective!

## Exercise 5: Batman's Data Detective - Count Different HTTP Request Types
Batman needs your help to investigate the Joker's online activities! Analyze a log file of HTTP requests to Israelies news websiters located at [./dataset/access.log](./dataset/access.log). Your task is to find out how many different types of HTTP requests the Joker has made in the log file. Batman has provided you with an accumulator to tally the results. Can you bring the Joker to justice?

## Instructions
- For each exercise, craft a Spark program inspired by the Joker and Batman theme while adhering to the problem statement.
- Your code will be in Python.
- Test your programs on a Local Spark or cluster manager.
- Embrace performance optimization techniques like broadcast variables and accumulators when applicable.
- Document your code clearly, just as Batman keeps records of his battles.
- Feel free to consult the Spark documentation and resources for guidance.
- You can find the dataset for the exercises in the [./dataset](./dataset) folder.
- Write your code in solution files named `solution_01.py`, `solution_02.py`, etc.

## Tips
- Use RDD operations like `map`, `filter`, `reduce`, and `distinct` to tackle the exercises.
- In Exercise 1, the Joker may try to trick you with his factorial puzzle.
- In Exercise 4, make strategic use of broadcast variables to ensure victory.
- Exercise 5 requires the skills of a true detective, so employ the accumulator wisely to count different HTTP request types.

Join Batman in his quest for justice and outsmart the Joker with your Spark skills!
