#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#This calculator works
# Same code without calling a function so instead of using return , we use print 
""" 
Advantages of This Approach:
Simplicity: No need to define or call a function.

Direct Output: Results are printed immediately, making it easier to understand for beginners.

When to Use This Approach:
If your program is small and doesn't require reusing the evaluation logic elsewhere.

If you prefer a straightforward, linear flow of code.


"""
# Input: Number of wins and total games played
wins = int(input("Enter the total number of games won: "))
total_games = int(input("Enter the total number of games played: "))

# Calculate win rate
win_rate = (wins / total_games) * 100

# Evaluate win rate and print results directly
if win_rate < 40:
    print(f"Your win rate is: {win_rate:.2f}%")
    print("Category: Low Performance")
    print("Advice: Needs significant improvement. Focus on strategy, mechanics, and teamwork.")
elif 40 <= win_rate < 50:
    print(f"Your win rate is: {win_rate:.2f}%")
    print("Category: Below Average")
    print("Advice: Room for improvement. Analyze gameplay and identify weaknesses.")
elif 50 <= win_rate < 55:
    print(f"Your win rate is: {win_rate:.2f}%")
    print("Category: Average")
    print("Advice: Solid performance. Consistent but can refine skills for higher ranks.")
elif 55 <= win_rate < 60:
    print(f"Your win rate is: {win_rate:.2f}%")
    print("Category: Above Average")
    print("Advice: Strong performance. Demonstrates good understanding of the game.")
elif 60 <= win_rate < 70:
    print(f"Your win rate is: {win_rate:.2f}%")
    print("Category: High Performance")
    print("Advice: Skilled player. Likely ranked in the upper tiers of competitive play.")
elif 70 <= win_rate < 80:
    print(f"Your win rate is: {win_rate:.2f}%")
    print("Category: Exceptional")
    print("Advice: Elite performance. Dominates most matches and understands advanced strategies.")
else:
    print(f"Your win rate is: {win_rate:.2f}%")
    print("Category: Pro Level")
    print("Advice: Top-tier player. Exceptional skill, strategy, and consistency. Potential for professional play.")

