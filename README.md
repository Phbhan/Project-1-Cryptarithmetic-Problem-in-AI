# Project-1-Cryptarithmetic-Problem-in-AI
## Problem statement:
Cryptarithmetic Problem is a type of constraint satisfaction problem where the
game is about digits and its unique replacement either with alphabets or other
symbols. In cryptarithmetic problem, the digits (0-9) get substituted by some
possible alphabets or symbols. The task in cryptarithmetic problem is to
substitute each digit with an alphabet to get the result arithmetically correct

In Google Play, you can find some game with cryptarithmetic puzzle. The Cryptogram is
an example. You can enjoy it for some early experience but not be immersed in it.

![Screenshot](https://user-images.githubusercontent.com/62047983/162348331-bb9b43d3-e8c1-438e-87a4-50e107f78ff3.png)

We can perform all the arithmetic operations on a given cryptarithmetic problem. The
rules or constraints on a cryptarithmetic problem are as follows:
* There should be a unique digit to be replaced with a unique alphabet.
* The result should satisfy the predefined arithmetic rules, i.e., `2+2 =4`, nothing else.
Digits should be from 0-9 only.
* There should be only one carry forward, while performing the addition operation
on a problem.
* The problem can be solved from both sides, i.e., left-hand side (L.H.S), or righthand side (R.H.S)
## Code general mechanism:
Combine Backtracking and CSP methods.
Step by step:
* Step 1:
  * Initialize variables taken from input file, append carry numbers and blank
character ‘’ where necessary.
  * Initialize sign with a plus (+) always at first to do additional operators
between carry numbers and first row character candidates. For instance,
sign will be [‘+’, ‘+’] following the example input below. In case of
parenthesis, they will be removed and perform changes on the included
operators where needed.
* Step 2:
  * Create a CSP with the above variable and domain ranges from 0 to 9.
  * Apply unary constraint to remove illegal values in domain through these
restrictions:
    * First candidate character does not hold value 0 in the domain.
    * Domain of ‘’ and c0 only hold value 0.
* Step 3:
  * Apply Backtracking.
  * Consider each variable from the rightmost to leftmost and from above to
down.

![Screenshot](https://user-images.githubusercontent.com/62047983/162346524-2e700fa7-3d7c-40f3-aa0b-22203a28aa7e.png)

If the variable during the execution of algorithm experiences these following
situations:
* Variable exists within the formula (before equal sign):
   * No value has been assigned to variable: Assign a suitable value and
change the result on that column operation result based on the
recently assigned value. Then, perform Backtracking.
   * Value has been assigned to variable: Change the result on that column
operation result based on the assigned value. Then, perform
Backtracking.
* Variable is the result value:
   * If variable has yet been assigned and the operation result from that
column without another variable assigned, then we assign this
variable and perform backtrack to the memorized location.
   * If variable has been assigned and the result from the considering
column equals to the value assigned before, simply apply backtrack
until memorized location reached.
* Variable happens to be the carry number:
  * Memorized value (or carry number) does not have constraint except
for c0 must be value 0.

If Backtrack suceeds, returns true. Otherwise, we must execute the value from which
we receive from the resulting operation from the column back to its original state.

At the end if Backtrack can no longer be performed, return false (or fail), which
means the formula has no result.
To calculate an operation on a column:
* For addition (+) and subtraction (-):
Every time a variable is traversed during the operation, we add or subtract
that value of variable with the result of the considering column. After
implementation, if column result larger than 10, we minus it by 10 and carry
number will hold 1 after applying addition, if column result less than 0, we
increase it by 10 before applying subtraction and make carry number holds - 1.

* For multiplication (*):
These algorithms are implemented based on how multiplication table is applied in
real life, we would like to present our explaination on this matter using that table:

![Screenshot](https://user-images.githubusercontent.com/62047983/162346537-cc3428d2-fc58-4d91-9d55-8ff1e8d0cae2.png)

C3, C2, C1 are column 3, 2, 1 on row 1 (A B C) consecutively. Similarly, C2, C1 as
column 2, column 1 on row 2 (D E).

In reality, we multiply each candidate and the next leftwise but a column backward:

![Screenshot](https://user-images.githubusercontent.com/62047983/162346541-61966867-b7d6-4229-9c4d-bef561bbc8b1.png)

So, we come up with a strategy: To use indices to calculate these character candidate
in order. The strategy follows like this:

![Screenshot](https://user-images.githubusercontent.com/62047983/162346544-5cc0061f-3f46-4843-addb-536755b3ed3c.png)

We multiply their value at the corresponding indices (E.g. `3*1` being `A * E`), then for
each column and row, we decrease and increase by 1 consecutively (E.g `3*1`
decrease 3 by 1 and increase 1 by 1 we have `2*2` at the next line).
It should result in:

![Screenshot](https://user-images.githubusercontent.com/62047983/162346546-81ff11cf-d6ee-4698-a3a3-059469a96319.png)

However, `2*3` and `1*3` do not exist because there is no third candidate character at row D E.

Afterward, apply addition by column to receive the result we seek for.

Thê following component sections are the names (a, b, c and so on…) of files and their
included functions (i, ii, iii and so on…) which is submitted along with this report.
