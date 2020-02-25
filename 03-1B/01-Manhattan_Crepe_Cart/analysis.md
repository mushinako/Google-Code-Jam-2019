#   Manhattan Crepe Cart: Analysis
##  My Approach
Consider x- and y-axis independently. People walking on the x-axis have no effect on the crepe cart's y-axis, and their y-position does not matter. The following analysis focuses on the x-coordinate. The y-coordinate can be obtained similarly.

Arrange all people going on the x-axis into 2 groups: Those going in the positive direction (N) and those going in the negative direction (S).

Given that the x- and y-coordinates of the crepe cart should be as small as possible, The potential positions of the cart should be **1 above the x-coordinates of those going in the positive direction (N)** or **0**. Iterate through these potential points. The number of people going there is the sum of **people with a strictly larger x-coordinate and going in the negative direction (S)** and **people with a strictly smaller x-coordinate and going in the positive direction (N)**. When the x-coordinates of these two categories are sorted, Python provides a helpful [bisect](https://docs.python.org/3/library/bisect.html) library.
