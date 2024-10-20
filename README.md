## Movie Rental Refactoring

A classic refactoring problem from Chapter 1 of
_Refactoring: Improving the Design of Existing Code_ by Martin Fowler.  

This repository contains Python code translated from the Java version.

The runnable `main.py` creates a customer and prints a statement.


## Instructions

See [Movie Rental Refactoring, Part 1](https://cpske.github.io/ISP/assignment/movierental/movierental-part1) for description of the code and what to do.

Before and after each refactoring you should **run the unit tests**.

## Resources

See [Resources](https://cpske.github.io/ISP/assignment/movierental/movierental-part1#resources) in the assignment description.

## Rationale
2.1 Ans: Inappropriate Intimacy
2.2 Ans: Strive for loosely coupled objects

5.2 Ans: I choose to put price_code_for_movie inside Rental class because:
- Low couping: Rental doesn't need to coup data from anywhere else
- High Cohesion: only Rental that need to invoke price.
- SRP: Rental is responsible for assign price to each rental.
- Information Expert: price_code_for_movie required movie and Price and rental already has both.

