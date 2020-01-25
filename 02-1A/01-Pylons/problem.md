#   [Pylons (8pts, 23pts)](https://codingcompetitions.withgoogle.com/codejam/round/0000000000051635/0000000000104e03)

##  Problem
Our Battlestarcraft Algorithmica ship is being chased through space by persistent robots called Pylons! We have just teleported to a new galaxy to try to shake them off of our tail, and we want to stay here for as long as possible so we can buy time to plan our next move... but we do not want to get caught!

This galaxy is a flat grid of **R** rows and **C** columns; the rows are numbered from 1 to **R** from top to bottom, and the columns are numbered from 1 to **C** from left to right. We can choose which cell to start in, and we must continue to jump between cells until we have visited each cell in the galaxy exactly once. That is, we can never revisit a cell, including our starting cell.

We do not want to make it too easy for the Pylons to guess where we will go next. Each time we jump from our current cell, we must choose a destination cell that does not share a row, column, or diagonal with that current cell. Let (`i`, `j`) denote the cell in the `i`-th row and `j`-th column; then a jump from a current cell (`r`, `c`) to a destination cell (`r'`, `c'`) is invalid if and only if any of these is true:

* `r` = `r'`
* `c` = `c'`
* `r` - `c` = `r'` - `c'`
* `r` + `c` = `r'` + `c'`
Can you help us find an order in which to visit each of the **R** × **C** cells, such that the move between any pair of consecutive cells in the sequence is valid? Or is it impossible for us to escape from the Pylons?

##  Input
The first line of the input gives the number of test cases, **T**. **T** test cases follow. Each consists of one line containing two integers **R** and **C**: the numbers of rows and columns in this galaxy.

##  Output
For each test case, output one line containing `Case #x: y`, where `y` is a string of uppercase letters: either `POSSIBLE` or `IMPOSSIBLE`, according to whether it is possible to fulfill the conditions in the problem statement. Then, if it is possible, output **R** × **C** more lines. The `i`-th of these lines represents the `i`-th cell you will visit (counting starting from 1), and should contain two integers `rᵢ` and `cᵢ`: the row and column of that cell. Note that the first of these lines represents your chosen starting cell.

##  Limits
* Time limit: 20 seconds per test set.
* Memory limit: 1GB.

### Test set 1 (Visible)
* **T** = 16.
* 2 ≤ **R** ≤ 5.
* 2 ≤ **C** ≤ 5.

### Test set 2 (Hidden)
* 1 ≤ **T** ≤ 100.
* 2 ≤ **R** ≤ 20.
* 2 ≤ **C** ≤ 20.

##  Sample
### Input
```
2
2 2
2 5
```

### Output
```
Case #1: IMPOSSIBLE
Case #2: POSSIBLE
2 3
1 1
2 4
1 2
2 5
1 3
2 1
1 5
2 2
1 4
```

In Sample `Case #1`, no matter which starting cell we choose, we have nowhere to jump, since all of the remaining cells share a row, column, or diagonal with our starting cell.

In Sample `Case #2`, we have chosen the cell in row 2, column 3 as our starting cell. Notice that it is fine for our final cell to share a row, column, or diagonal with our starting cell. The following diagram shows the order in which the cells are visited:

<table>
  <tr>
    <td>2</td>
    <td>4</td>
    <td>6</td>
    <td>10</td>
    <td>8</td>
  </tr>
  <tr>
    <td>7</td>
    <td>9</td>
    <td>1</td>
    <td>3</td>
    <td>5</td>
  </tr>
</table>


