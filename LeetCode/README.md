# Daily Coding

This repository contains my daily coding practice.

Problem: 3Sum

Approach:
- Sort the array.
- Fix one element and use two pointers to find the remaining two elements.
- Skip duplicate values to ensure unique triplets.

Time Complexity: O(n²)
Space Complexity: O(1)

Day 3 - Squid Game (CodeChef Problem of the Day)

Problem:
There are N players in the game. When player i is eliminated, Ai money is added to the prize pool. Only one player survives and wins all the money in the prize pool.

Approach:
If player i is chosen as the winner, the prize received is:
    total_sum - Ai

To maximize the prize, we should choose the player with the minimum Ai value as the winner.

Formula:
    Answer = sum(A) - min(A)

Time Complexity: O(N)
Space Complexity: O(1)


# Valid Parentheses

## Problem
Given a string containing only `()[]{}`, determine whether it is valid.

## Approach
Use a stack:
- Push opening brackets.
- When a closing bracket is found, check whether it matches the top of the stack.
- If it doesn't match, return `False`.
- At the end, the stack must be empty.

## Complexity
- Time: O(n)
- Space: O(n)

## Python Solution
```python
# paste solution here