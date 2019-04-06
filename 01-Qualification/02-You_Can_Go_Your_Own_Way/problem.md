#   [You Can Go Your Own Way (5pts, 9pts, 10pts)](https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/00000000000881da)

##  Problem
You have just entered the world's easiest maze. You start in the northwest cell of an **N** by **N** grid of unit cells, and you must reach the southeast cell. You have only two types of moves available: a unit move to the east, and a unit move to the south. You can move into any cell, but you may not make a move that would cause you to leave the grid.

You are excited to be the first in the world to solve the maze, but then you see footprints. Your rival, Labyrinth Lydia, has already solved the maze before you, using the same rules described above!

As an original thinker, you do not want to reuse any of Lydia's moves. Specifically, if her path includes a unit move from some cell `A` to some adjacent cell `B`, your path cannot also include a move from `A` to `B`. (However, in that case, it is OK for your path to visit `A` or visit `B`, as long as you do not go from `A` to `B`.) Please find such a path.

In the following picture, Lydia's path is indicated in blue, and one possible valid path for you is indicated in orange:
<svg width="400px" height="400px" viewBox="0 0 502 502" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><defs></defs> <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd"><g id="All" transform="translate(1.000000, 1.000000)"><g id="All-without-circles"><g id="Back" stroke-width="2" stroke="#000000"><g id="Group"><rect id="Rectangle-2" x="0" y="0" width="100" height="100"></rect> <rect id="Rectangle-2" x="100" y="0" width="100" height="100"></rect> <rect id="Rectangle-2" x="200" y="0" width="100" height="100"></rect> <rect id="Rectangle-2" x="300" y="0" width="100" height="100"></rect> <rect id="Rectangle-2" x="400" y="0" width="100" height="100"></rect></g> <g id="Group" transform="translate(0.000000, 100.000000)"><rect id="Rectangle-2" x="0" y="0" width="100" height="100"></rect> <rect id="Rectangle-2" x="100" y="0" width="100" height="100"></rect> <rect id="Rectangle-2" x="200" y="0" width="100" height="100"></rect> <rect id="Rectangle-2" x="300" y="0" width="100" height="100"></rect> <rect id="Rectangle-2" x="400" y="0" width="100" height="100"></rect></g> <g id="Group" transform="translate(0.000000, 200.000000)"><rect id="Rectangle-2" x="0" y="0" width="100" height="100"></rect> <rect id="Rectangle-2" x="100" y="0" width="100" height="100"></rect> <rect id="Rectangle-2" x="200" y="0" width="100" height="100"></rect> <rect id="Rectangle-2" x="300" y="0" width="100" height="100"></rect> <rect id="Rectangle-2" x="400" y="0" width="100" height="100"></rect></g> <g id="Group" transform="translate(0.000000, 300.000000)"><rect id="Rectangle-2" x="0" y="0" width="100" height="100"></rect> <rect id="Rectangle-2" x="100" y="0" width="100" height="100"></rect> <rect id="Rectangle-2" x="200" y="0" width="100" height="100"></rect> <rect id="Rectangle-2" x="300" y="0" width="100" height="100"></rect> <rect id="Rectangle-2" x="400" y="0" width="100" height="100"></rect></g> <g id="Group" transform="translate(0.000000, 400.000000)"><rect id="Rectangle-2" x="0" y="0" width="100" height="100"></rect> <rect id="Rectangle-2" x="100" y="0" width="100" height="100"></rect> <rect id="Rectangle-2" x="200" y="0" width="100" height="100"></rect> <rect id="Rectangle-2" x="300" y="0" width="100" height="100"></rect> <rect id="Rectangle-2" x="400" y="0" width="100" height="100"></rect></g></g> <g id="Group-5" transform="translate(60.000000, 40.000000)"><path d="M0,10 L80,10" id="Line" stroke="#4990E2" stroke-width="5" stroke-linecap="square"></path> <polygon id="Triangle-2" fill="#4990E2" transform="translate(78.000000, 10.000000) rotate(-270.000000) translate(-78.000000, -10.000000) " points="78 0 88 20 68 20"></polygon> <polygon id="Triangle-2" fill="#4990E2" transform="translate(190.000000, 98.000000) rotate(-180.000000) translate(-190.000000, -98.000000) " points="190 88 200 108 180 108"></polygon> <polygon id="Triangle-2" fill="#4990E2" transform="translate(190.000000, 198.000000) rotate(-180.000000) translate(-190.000000, -198.000000) " points="190 188 200 208 180 208"></polygon> <polygon id="Triangle-2" fill="#4990E2" transform="translate(190.000000, 298.000000) rotate(-180.000000) translate(-190.000000, -298.000000) " points="190 288 200 308 180 308"></polygon> <polygon id="Triangle-2" fill="#4990E2" transform="translate(290.000000, 398.000000) rotate(-180.000000) translate(-290.000000, -398.000000) " points="290 388 300 408 280 408"></polygon> <polygon id="Triangle-2" fill="#4990E2" transform="translate(178.000000, 10.000000) rotate(-270.000000) translate(-178.000000, -10.000000) " points="178 0 188 20 168 20"></polygon> <polygon id="Triangle-2" fill="#4990E2" transform="translate(278.000000, 310.000000) rotate(-270.000000) translate(-278.000000, -310.000000) " points="278 300 288 320 268 320"></polygon> <polygon id="Triangle-2" fill="#4990E2" transform="translate(378.000000, 410.000000) rotate(-270.000000) translate(-378.000000, -410.000000) " points="378 400 388 420 368 420"></polygon> <path d="M100,10 L180,10" id="Line" stroke="#4990E2" stroke-width="5" stroke-linecap="square"></path> <path d="M200,310 L280,310" id="Line" stroke="#4990E2" stroke-width="5" stroke-linecap="square"></path> <path d="M300,410 L380,410" id="Line" stroke="#4990E2" stroke-width="5" stroke-linecap="square"></path> <path d="M190,20 L190,100" id="Line" stroke="#4990E2" stroke-width="5" stroke-linecap="square"></path> <path d="M190,120 L190,200" id="Line" stroke="#4990E2" stroke-width="5" stroke-linecap="square"></path> <path d="M190,220 L190,300" id="Line" stroke="#4990E2" stroke-width="5" stroke-linecap="square"></path> <path d="M290,320 L290,400" id="Line" stroke="#4990E2" stroke-width="5" stroke-linecap="square"></path></g> <g id="Group-5" transform="translate(40.000000, 60.000000)" stroke="#F6A623"><path d="M20,90 L100,90" id="Line" stroke-width="5" stroke-linecap="square"></path> <polygon id="Triangle-2" fill="#F6A623" transform="translate(98.000000, 90.000000) rotate(-270.000000) translate(-98.000000, -90.000000) " points="98 80 108 100 88 100"></polygon> <polygon id="Triangle-2" fill="#F6A623" transform="translate(10.000000, 77.000000) rotate(-180.000000) translate(-10.000000, -77.000000) " points="10 67 20 87 0 87"></polygon> <polygon id="Triangle-2" fill="#F6A623" transform="translate(310.000000, 177.000000) rotate(-180.000000) translate(-310.000000, -177.000000) " points="310 167 320 187 300 187"></polygon> <polygon id="Triangle-2" fill="#F6A623" transform="translate(310.000000, 277.000000) rotate(-180.000000) translate(-310.000000, -277.000000) " points="310 267 320 287 300 287"></polygon> <polygon id="Triangle-2" fill="#F6A623" transform="translate(410.000000, 377.000000) rotate(-180.000000) translate(-410.000000, -377.000000) " points="410 367 420 387 400 387"></polygon> <polygon id="Triangle-2" fill="#F6A623" transform="translate(198.000000, 90.000000) rotate(-270.000000) translate(-198.000000, -90.000000) " points="198 80 208 100 188 100"></polygon> <polygon id="Triangle-2" fill="#F6A623" transform="translate(398.000000, 290.000000) rotate(-270.000000) translate(-398.000000, -290.000000) " points="398 280 408 300 388 300"></polygon> <polygon id="Triangle-2" fill="#F6A623" transform="translate(298.000000, 90.000000) rotate(-270.000000) translate(-298.000000, -90.000000) " points="298 80 308 100 288 100"></polygon> <path d="M120,90 L200,90" id="Line" stroke-width="5" stroke-linecap="square"></path> <path d="M220,90 L300,90" id="Line" stroke-width="5" stroke-linecap="square"></path> <path d="M320,290 L400,290" id="Line" stroke-width="5" stroke-linecap="square"></path> <path d="M10,0 L10,80" id="Line" stroke-width="5" stroke-linecap="square"></path> <path d="M310,100 L310,180" id="Line" stroke-width="5" stroke-linecap="square"></path> <path d="M310,200 L310,280" id="Line" stroke-width="5" stroke-linecap="square"></path> <path d="M410,300 L410,380" id="Line" stroke-width="5" stroke-linecap="square"></path></g></g></g></g></svg>

##  Input
The first line of the input gives the number of test cases, **T**. **T** test cases follow; each case consists of two lines. The first line contains one integer **N**, giving the dimensions of the maze, as described above. The second line contains a string **P** of 2**N** - 2 characters, each of which is either uppercase `E` (for east) or uppercase `S` (for south), representing Lydia's valid path through the maze.

##  Output
For each test case, output one line containing `Case #x: y`, where `x` is the test case number (starting from 1) and `y` is a string of 2**N** - 2 characters each of which is either uppercase `E` (for east) or uppercase `S` (for south), representing your valid path through the maze that does not conflict with Lydia's path, as described above. It is guaranteed that at least one answer exists.

##  Limits
1 ≤ **T** ≤ 100.

Time limit: 15 seconds per test set.

Memory limit: 1GB.

**P** contains exactly **N** - 1 `E` characters and exactly **N** - 1 `S` characters.

### Test set 1 (Visible)
2 ≤ **N** ≤ 10.

### Test set 2 (Visible)
2 ≤ **N** ≤ 1000.

### Test set 3 (Hidden)
For at most 10 cases, 2 ≤ **N** ≤ 50000.

For all other cases, 2 ≤ **N** ≤ 10000.

##  Sample
### Input
```
2
2
SE
5
EESSSESE
```

### Output
```
Case #1: ES
Case #2: SEEESSES
```

In Sample `Case #1`, the maze is so small that there is only one valid solution left for us.

Sample `Case #2` corresponds to the picture above. Notice that it is acceptable for the paths to cross.
