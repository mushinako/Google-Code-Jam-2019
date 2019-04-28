#   Draupnir: Analysis
##  My Approach
For the large set, we only have 2 chances to ask the well of knowledge. Therefore, we have to get at least 4 values not directly from solving the equations.

Notice that each `Rᵢ` is at most 100 < 128 = 2⁷, thus ![2^mR_i&plus;2^nR_j=y](https://latex.codecogs.com/svg.latex?2^mR_i&plus;2^nR_j=y) is solvable if the differece between m and n is at least 7

I chose days 56 and 170. On day 56, `R₁` and `R₂` can be isolated from the rest. On day 170, `R₃` and `R₄` can be isolated from the rest. Then `R₅` and `R₆` can be solved via regular equation-solving techiniques.

### Calculation Details
On day 56:

![2^{56}R_1+2^{28}R_2+2^{18}R_3+2^{14}R_4+2^{11}R_5+2^9R_6=d_{56}](https://latex.codecogs.com/svg.latex?2%5E%7B56%7DR_1&plus;2%5E%7B28%7DR_2&plus;2%5E%7B18%7DR_3&plus;2%5E%7B14%7DR_4&plus;2%5E%7B11%7DR_5&plus;2%5E9R_6%3Dd_%7B56%7D).

![2^{47}R_1+2^{19}R_2+2^9R_3+2^5R_4+2^2R_5+R_6=d_{56}/2^9](https://latex.codecogs.com/svg.latex?2%5E%7B47%7DR_1&plus;2%5E%7B19%7DR_2&plus;2%5E9R_3&plus;2%5E5R_4&plus;2%5E2R_5&plus;R_6%3Dd_%7B56%7D/2%5E9)

Then:

`R₁` is the integer part of ![\frac{d_{56}/2^9}{2^{47}}](https://latex.codecogs.com/svg.latex?%5Cfrac%7Bd_%7B56%7D/2%5E9%7D%7B2%5E%7B47%7D%7D)

`R₂` is the integer part of ![\frac{d_{56}/2^9\mod2^{47}}{2^{19}}](https://latex.codecogs.com/svg.latex?%5Cfrac%7Bd_%7B56%7D/2%5E9%5Cmod2%5E%7B47%7D%7D%7B2%5E%7B19%7D%7D)

For the rest:

![2^9R_3+2^5R_4+2^2R_5+R_6=d_{56}/2^9\mod2^{19} \ \ \ \ \ \ \ \ \ \ \ \ (1)](https://latex.codecogs.com/svg.latex?2%5E9R_3&plus;2%5E5R_4&plus;2%5E2R_5&plus;R_6%3Dd_%7B56%7D/2%5E9%5Cmod2%5E%7B19%7D%20%5C%20%5C%20%5C%20%5C%20%5C%20%5C%20%5C%20%5C%20%5C%20%5C%20%5C%20%5C%20%281%29)

On day 170:

![2^{170}R_1+2^{85}R_2+2^{56}R_3+2^{42}R_4+2^{34}R_5+2^{28}R_6=d_{170}](https://latex.codecogs.com/svg.latex?2%5E%7B170%7DR_1&plus;2%5E%7B85%7DR_2&plus;2%5E%7B56%7DR_3&plus;2%5E%7B42%7DR_4&plus;2%5E%7B34%7DR_5&plus;2%5E%7B28%7DR_6%3Dd_%7B170%7D)

As the judge mods everything by 2⁶³, `R₁` and `R₂` disappear:

![2^{56}R_3+2^{42}R_4+2^{34}R_5+2^{28}R_6=d_{170}](https://latex.codecogs.com/svg.latex?2%5E%7B56%7DR_3&plus;2%5E%7B42%7DR_4&plus;2%5E%7B34%7DR_5&plus;2%5E%7B28%7DR_6%3Dd_%7B170%7D)

![2^{28}R_3+2^{14}R_4+2^6R_5+R_6=d_{170}/2^{28}](https://latex.codecogs.com/svg.latex?2%5E%7B28%7DR_3&plus;2%5E%7B14%7DR_4&plus;2%5E6R_5&plus;R_6%3Dd_%7B170%7D/2%5E%7B28%7D)

Then:

`R₃` is the integer part of ![\frac{d_{170}/2^{28}}{2^{28}}](https://latex.codecogs.com/svg.latex?%5Cfrac%7Bd_%7B170%7D/2%5E%7B28%7D%7D%7B2%5E%7B28%7D%7D)

`R₄` is the integer part of ![\frac{d_{170}/2^{28}\mod2^{28}}{2^{14}}](https://latex.codecogs.com/svg.latex?%5Cfrac%7Bd_%7B170%7D/2%5E%7B28%7D%5Cmod2%5E%7B28%7D%7D%7B2%5E%7B14%7D%7D)

For the rest:

![2^6R_5+R_6=d_{170}/2^{28}\mod2^{14} \ \ \ \ \ \ \ \ \ \ \ \ (2)](https://latex.codecogs.com/svg.latex?2%5E6R_5&plus;R_6%3Dd_%7B170%7D/2%5E%7B28%7D%5Cmod2%5E%7B14%7D%20%5C%20%5C%20%5C%20%5C%20%5C%20%5C%20%5C%20%5C%20%5C%20%5C%20%5C%20%5C%20%282%29)

Then substitute the `R₃` and `R₄` in `(1)` with numbers, and `R₅` and `R₆` can be solved from `(1)` and `(2)` via common operations.
