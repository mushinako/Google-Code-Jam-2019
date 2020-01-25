#   [Manhattan Crepe Cart (9pts, 18pts)](https://codingcompetitions.withgoogle.com/codejam/round/0000000000051706/000000000012295c)

##  Problem
There are a lot of great streetside food vendors in Manhattan, but without a doubt, the one with the tastiest food is the Code Jam Crepe Cart!

You want to find the cart, but you do not know where it is, except that it is at some street intersection. You believe that people from across Manhattan are currently walking toward that intersection, so you will try to identify the intersection toward which the most people are traveling.

For the purposes of this problem, Manhattan is a regular grid with its axes aligned to compass lines and bounded between 0 and **Q**, inclusive, on each axis. There are west-east streets corresponding to gridlines `y` = 0, `y` = 1, `y` = 2, …, `y` = **Q** and south-north streets corresponding to gridlines `x` = 0, `x` = 1, `x` = 2, …, `x` = **Q**, and people move only along these streets. The points where the lines meet — e.g., `(0, 0)` and `(1, 2)` — are intersections. The shortest distance between two intersections is measured via the [Manhattan distance](https://en.wikipedia.org/wiki/Taxicab_geometry) — that is, by the sum of the absolute horizontal difference and the absolute vertical difference between the two sets of coordinates.

You know the locations of **P** people, all of whom are standing at intersections, and the compass direction each person is headed: north (increasing `y` direction), south (decreasing `y` direction), east (increasing `x` direction), or west (decreasing `x` direction). A person is moving toward a street intersection if their current movement is on a shortest path to that street intersection within the Manhattan grid. For example, if a person located at `(x₀, y₀)` is moving north, then they are moving toward all street intersections that have coordinates `(x, y)` with `y` > `y₀`.

You think the crepe cart is at the intersection toward which the most people are traveling. Moreover, you believe that more southern and western parts of the island are most likely to have a crepe cart, so if there are multiple such intersections, you will choose the one with the smallest non-negative `x` coordinate, and if there are multiple such intersections with that same `x` coordinate, the one among those with the smallest non-negative `y` coordinate. Which intersection will you choose?

##  Input
The first line of the input gives the number of test cases, **T**. **T** test cases follow. Each test case starts with one line containing two integers **P** and **Q**: the number of people, and the maximum possible value of an `x` or `y` coordinate in Manhattan, as described above. Then, there are **P** more lines. The `i`-th of those lines contains two integers **Xᵢ** and **Yᵢ**, the current location (street corner) of a person, and a character **Dᵢ**, the direction that person is headed. **Dᵢ** is one of the uppercase letters `N`, `S`, `E`, or `W`, which stand for north, south, east, and west, respectively.

##  Output
For each test case, output one line containing `Case #t: x y`, where t is the test case number (starting from 1) and `x` and `y` are the horizontal and vertical coordinates of the intersection where you believe the crepe cart is located.

##  Limits
* 1 ≤ **T** ≤ 100.
* Time limit: 20 seconds per test set.
* Memory limit: 1GB.
* 1 ≤ **P** ≤ 500.
* 0 ≤ **Xᵢ** ≤ **Q**, for all `i`.
* 0 ≤ **Yᵢ** ≤ **Q**, for all `i`.
* For all `i`, if **Xᵢ** = 0, **Dᵢ** ≠ `W`.
* For all `i`, if **Yᵢ** = 0, **Dᵢ** ≠ `S`.
* For all `i`, if **Xᵢ** = Q, **Dᵢ** ≠ `E`.
* For all `i`, if **Yᵢ** = Q, **Dᵢ** ≠ `N`.

### Test set 1 (Visible)
* **Q** = 10.

### Test set 2 (Hidden)
* **Q** = 10⁵.

##  Sample
### Input
```
3
1 10
5 5 N
4 10
2 4 N
2 6 S
1 5 E
3 5 W
8 10
0 2 S
0 3 N
0 3 N
0 4 N
0 5 S
0 5 S
0 8 S
1 5 W
```

### Output
```
Case #1: 0 6
Case #2: 2 5
Case #3: 0 4
```

In Sample `Case #1`, there is only one person, and they are moving north from `(5, 5)`. This means that all street corners with `y` ≥ 6 are possible locations for the crepe cart. Of those possibilities, we choose the one with lowest `x` ≥ 0 and then lowest `y` ≥ 6.

In Sample `Case #2`, there are four people, all moving toward location `(2, 5)`. There is no other location that has as many people moving toward it.

In Sample `Case #3`, six of the eight people are moving toward location `(0, 4)`. There is no other location that has as many people moving toward it.
