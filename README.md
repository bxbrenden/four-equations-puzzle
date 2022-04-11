# "Four Equations" Puzzle and Solution

## Background
During a recent visit to The Oregon Museum of Science and Industry ([OMSI](https://omsi.edu/) for short), I came across a puzzle that had a 3 x 3 grid and some wooden blocks with the numbers 1 through 9 printed on them.
The problem was called `Four Equations`, and the goal of the puzzle was to arrange the numbered blocks in a certain pattern that met the following constraints:

| Row or Column    | Constraint |
| ---------------- | ---------- |
| Row 1    | The first number minus the second number equals the third number. |
| Row 2    | The first number divided by the second number equals the third number. |
| Row 3    | The first number plus the second number equals the third number. |
| Column 1 | The first number times the second number equals the third number. |

To better visualize this, see the below picture of the puzzle with its blocks jumbled:
![image of the "Four Equations" puzzle at OMSI](https://github.com/bxbrenden/puzzle-grid/blob/main/four-equations.png)

## Motivation
As you might infer from the picture of the wooden blocks and simple, giant print, this was a puzzle for children, and yet I couldn't solve it in the 5-10 minutes I tried.
Slightly annoyed, I gave up, sanitized my hands, and said I'd solve it later with a computer.

## Number of Possible Solutions
The way to calculate the total number of possible solutions to this puzzle is to use factorials.
There are 9 starting blocks to choose from.
After you choose one, there are 8 remaining blocks to choose from.
After you choose another, there are 7 remaining blocks, and so on until you run out.

That means that the number of possible solutions is `9!` or "nine factorial".
This can also be written as:
```
9 x 8 x 7 x 6 x 5 x 4 x 3 x 2 x 1
```

When you evaluate the expression `9!`, you get the number 362,880.
So, that's the number of  "naive guesses" it would take to guarantee that you either get the answer or prove there isn't one.

Of course, not every permutation in our huge list is truly a potential solution.
The number of possible solutions goes way down when you consider the relationships among the numbers and their operators.
For example, row two divides its first number by its second, i.e. `n1 / n2`.
Since 2, 3, 5, and 7 are prime numbers, none of them can be the first number in row two.
In that same vein, the ninth box (row 3, box 3) is the product of two numbers `n1 * n2`, so none of the primes can go there since we don't have any duplicates, and a prime number only has two factors: one and the prime itself.

You could solve the Four Equations problem like a Sudoku or any other logic puzzle, given that it has so many logical constraints that help to eliminate a lot of possible solutions.
But, I have a computer, and I don't have the patience for that!

## Solving it with Python

There are two main pieces to my simple Python program:
1. Generate a list of all possible permutations of the numbers 1 through 9.
2. See if a given permutation meets the constraints, thereby solving the puzzle, and print it to the screen if so.

### Getting All Possible Permutations
Rather than reinvent the wheel, I used the `permutations()` function from Python's `itertools` module.
This function returns all possible permutations of a list of numbers.
Here's an example of the code that gets me the list of every way the numbers 1 through 9 can be scrambled:
```
from itertools import permutations

# Generate a list of 1-9 (up to but excluding 10)
one_thru_nine = list(range(1, 10))

all_perms = list(permutations(one_thru_nine))
```

In the above code, I first generate a list of all numbers 1 through 9 using Python's `range` function.
`range` takes two arguments in this case: the lower bound (starting number) and upper bound (ending number).
Confusingly, `range` is inclusive on the lower bound and exclusive on the upper bound, which means that if I run `range(1, 5)`, it will give me the numbers 1, 2, 3, and 4, but **not** 5.

After I get the list of numbers, I use `permutations` to create a generator of all permutations.
This generator isn't really a list by itself.
Instead, it's a piece of code that can be *asked* for a list, one item at a time.
In order to get the generator to spit out all elements of the list at once, I put the generator into the `list` function.

### Constraint Checking
Equipped with a comprehensive list of possible solutions, we now turn to solving the puzzle.
To check if a given permutation solves the puzzle, the code uses Python assertions.
An assertion is just a statement that, if true, does nothing and moves on.
However, if an assertion proves to be false, it raises an error.
This error is called an `AssertionError`.

Here's a snippet that shows how to check if the first element plus the second element equals the third:
```
def check_solution(p):
    """Given a list "p", return True if the first element
       minus the second element equals the third."""

    try:
        assert p[0] - p[1] == p[2]
    except AssertionError:
        return False
    else:
        return True
```

In the above code, we make a function called `check_solution`.
This function takes a list called `p`.
Since `p` is a `list` object, the first element has an index of 0.
That means the first element in the list is called `p[0]`, and the second one is `p[1]`, and the third is `p[2]`.

So, we assert that `p[0] - p[1] == p[2]`.
If this is true, as in the case `3 - 2 == 1` then the function skips to the `else` section and returns a value of `True`.
If that assertion is false, for example `4 - 2 == 7` then an `AssertionError` is raised by our function.
We "handle" that error by simply returning `False`.

The above example only solves one of the three constraints, but we can use assertions to test addition, division, and multiplication just like we did for subtraction (skipping here for brevity).

## Solving the Puzzle
With all the math riff-raff out of the way, you can solve this puzzle by using Python 3 to run my accompanying script called `grid_puzzle.py`.

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
```

## Conclusion
Since my list of possible solutions grew sequentially from 1 in the first box, and since the real solution started with a 9 in the first box, it took a lot of guesses for the computer to get it right.
Specifically, it took exactly 345,295 guesses!

I am now armed with the computational power to brute-force a childrens' puzzle.
The next time someone asks me if I'm smarter than a fifth grader, I can respond more confidently than ever with a resounding, "probably!".
