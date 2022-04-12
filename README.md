# "Four Equations" Puzzle and Solution

## TL;DR
A children's puzzle embarrassingly stumped me, so I brute-forced it with a Python program.

## Background
During a visit to The Oregon Museum of Science and Industry (a.k.a. [OMSI](https://omsi.edu/)), I noticed a puzzle that had a 3 x 3 grid and some wooden blocks labeled 1 through 9.
The grid looked like this:
```
☐ - ☐ = ☐
        ×
☐ ÷ ☐ = ☐
        =
☐ + ☐ = ☐
```

The puzzle was called `Four Equations`, and the goal of it was to arrange the numbered blocks in a pattern that met the following constraints:

| Row or Column    | Constraint |
| ---------------- | ---------- |
| Row 1    | The first number *minus* the second number equals the third number. |
| Row 2    | The first number *divided by* the second number equals the third number. |
| Row 3    | The first number *plus* the second number equals the third number. |
| Column 1 | The first number *times* the second number equals the third number. |

Here's a picture of the puzzle with its blocks jumbled:
![image of the "Four Equations" puzzle at OMSI](https://github.com/bxbrenden/puzzle-grid/blob/main/four-equations.png)

## Motivation
As you might infer from the picture of the wooden blocks and simple, gigantic print on the sign, this was a puzzle for children, and yet I couldn't solve it in the 5-10 minutes I tried.
Slightly annoyed, I gave up, sanitized my hands, and vowed I'd solve it later with a computer.

## Number of Possible Solutions
The way to calculate the total number of possible solutions to this puzzle is to use factorials.
There are 9 starting blocks to choose from.
After you choose one, there are 8 remaining blocks to choose from.
After you choose another, there are 7 remaining, and so on until you run out.

That means that the number of possible solutions is `9!` or "nine factorial".
This can also be written as:
```
9 x 8 x 7 x 6 x 5 x 4 x 3 x 2 x 1
```

When you evaluate the expression `9!`, you get the number 362,880.
That's the number of naive guesses it would take to guarantee that you either get the answer or prove there isn't one.

I say "naive" because not every permutation in our huge list is really a potential solution.
The possibilities shrink when you consider the mathematical relationships among the numbers.
For example, the second row divides its first number by its second.
Because 2, 3, 5, and 7 are prime numbers, none of them can be the first number in row two.
The ninth box is the product of two numbers, so none of the primes can go there either, as we don't have any duplicates, and a prime number only has two factors: one and the prime itself.

You could solve the Four Equations problem like a Sudoku, given that it has so many logical constraints that eliminate a lot of possible solutions.
But, I have a computer, and I don't have the patience for that!

## Solving it with Python
I chose the Python programming language to build my puzzle solver.
Python is a powerful language, and it's also the one I'm most comfortable using.

There are two main pieces to my Python program:
1. Generate a list of all possible permutations of the numbers 1 through 9.
2. See if a given permutation solves the puzzle, and print it if so.

### Getting All Possible Permutations
Rather than reinvent the wheel, I used the `permutations` function from Python's `itertools` module.
This function returns all possible permutations of a list of numbers.

Here's some example code that tells me every way the numbers 1 through 9 can be scrambled:
```
from itertools import permutations

one_thru_nine = list(range(1, 10))

all_perms = list(permutations(one_thru_nine))
```

In the above code, I first generate a list of all numbers 1 through 9 with Python's `range` function.
`range` takes two arguments here: the lower bound (starting number) and upper bound (ending number).
Confusingly, `range` is inclusive on the lower bound and exclusive on the upper bound.
That means that if I run `range(1, 5)`, it'll give me the numbers 1, 2, 3, and 4, but **not** 5.
Therefore, I use `range(1, 10)` in the example to get 1 through 9.

After I get the list of numbers, I use `permutations` to create a generator of all permutations.
This generator is a special object in Python, because it isn't really a list by itself.
Instead, it's a piece of code that can be *asked* for a list, one item at a time.
In order to get the generator to spit out all elements of the list at once, I put the generator into the built-in `list` function.

### Constraint Checking
Equipped with a comprehensive list of possible solutions (and many erroneous ones), it's time to solve the puzzle.
To check if a given permutation solves the puzzle, the code uses Python assertions.
An assertion is just a statement that is either true or false.
If it's true, Python does nothing and moves on to executing the next line of code.
However, if an assertion is false, Python raises an error.
This error is called an `AssertionError`.

Here's a snippet that uses an assertion to check if the difference of the first two elements equals the third element:
```
def check_solution(p):
    try:
        assert p[0] - p[1] == p[2]
    except AssertionError:
        return False
    else:
        return True
```

In the above code, we make a function called `check_solution`.
This function takes an arbitrary list called `p`.
In order to grab an item out of a Python list, you refer to the item by its index.
An index is the numerical label that represents the item's place in the list.
The first element has an index of 0, so if my list were `[1,2,3]`, the number 1 would be at index 0, the number 2 would be at index 1, and 3 would be at index 2.
Our list is called `p`, so that means the first element in the list is called `p[0]`, and the second one is `p[1]`, and the third is `p[2]`.

In the code, we assert that `p[0] - p[1] == p[2]`.
If this is true, as in the example case `6 - 4 == 2` then the function skips to the `else` section and returns a value of `True`.
If that assertion is false, for example `4 - 2 == 7` then an `AssertionError` is raised by our function.
We "handle" that error by simply returning `False`.

The above example only solves one of the four constraints, but we can use assertions to test addition, division, and multiplication just like we did for subtraction.
Those assertions are included in the code, but I've omitted them here to stop the reader from falling asleep.

## Solving the Puzzle
With all the math riff-raff out of the way, we can solve this puzzle.
Assuming you have Python 3 installed, you can run my accompanying script called `grid_puzzle.py` using this command from the CLI:
```
python3 grid_puzzle.py
```

The answer gets rendered to the screen as follows:
```
Solution found! 🟢
---------
9 - 5 = 4
        x
6 ÷ 3 = 2
        =
1 + 7 = 8
---------
Solution found! 🟢
---------
9 - 5 = 4
        x
6 ÷ 3 = 2
        =
7 + 1 = 8
---------
The total number of solutions is 2
```

## Conclusion
To my surprise, there were two solutions to the problem.
My program started its guesses with the number 1 in the first box, and the real solutions both started with a 9 in the first box, so it took a lot of attempts for the computer to get it right.
Specifically, it took exactly 345,295 guesses to get the first solution and two more for the second!

I am now armed with the computational power to brute-force a children's puzzle.
The next time someone asks me if I'm smarter than a fifth grader, I can respond more confidently than ever with a resounding, "probably!".
