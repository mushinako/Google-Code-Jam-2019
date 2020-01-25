#   Draupnir: Analysis
##  My Approach
For the large set, we only have 2 chances to ask the well of knowledge. Therefore, we have to get at least 4 values not directly from solving the equations.

Notice that each `Rᵢ` is at most 100 < 128 = 2⁷, thus ![2^mR_i&plus;2^nR_j=y](https://latex.codecogs.com/svg.latex?2^mR_i&plus;2^nR_j=y) is solvable if the difference between m and n is at least 7

I chose days 56 and 170. On day 56, `R₁` and `R₂` can be isolated from the rest. On day 170, `R₃` and `R₄` can be isolated from the rest. Then `R₅` and `R₆` can be solved via regular equation-solving techniques.

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

### Further Explanations
#### Day 56
On day 56 (hopefully this is clear):

![2^{47}R_1+2^{19}R_2+2^9R_3+2^5R_4+2^2R_5+R_6=d_{56}/2^9](https://latex.codecogs.com/svg.latex?2%5E%7B47%7DR_1&plus;2%5E%7B19%7DR_2&plus;2%5E9R_3&plus;2%5E5R_4&plus;2%5E2R_5&plus;R_6%3Dd_%7B56%7D/2%5E9)

If we divide 2⁴⁷ on both sides:

![R_1+2^{-28}R_2+2^{-38}R_3+2^{-42}R_4+2^{-45}R_5+2^{-47}R_6=\frac{d_{56}/2^9}{2^{47}}](https://latex.codecogs.com/svg.latex?R_1&plus;2%5E%7B-28%7DR_2&plus;2%5E%7B-38%7DR_3&plus;2%5E%7B-42%7DR_4&plus;2%5E%7B-45%7DR_5&plus;2%5E%7B-47%7DR_6%3D%5Cfrac%7Bd_%7B56%7D/2%5E9%7D%7B2%5E%7B47%7D%7D)

As `Rᵢ` ≤ 100 < 2⁷:

![2^{-28}R_2\le2^{-28}\cdot100<2^{-28}\cdot2^7=2^{-21}\approx4.77\times10^{-7}](https://latex.codecogs.com/svg.latex?2%5E%7B-28%7DR_2%5Cle2%5E%7B-28%7D%5Ccdot100%3C2%5E%7B-28%7D%5Ccdot2%5E7%3D2%5E%7B-21%7D%5Capprox4.77%5Ctimes10%5E%7B-7%7D)

The contributions by `R₃` to `R₆` will be even smaller, thus:

![2^{-28}R_2+2^{-38}R_3+2^{-42}R_4+2^{-45}R_5+2^{-47}R_6\ll1](https://latex.codecogs.com/svg.latex?2%5E%7B-28%7DR_2&plus;2%5E%7B-38%7DR_3&plus;2%5E%7B-42%7DR_4&plus;2%5E%7B-45%7DR_5&plus;2%5E%7B-47%7DR_6%5Cll1)

Therefore `R₂` through `R₆` cannot contribute to the integer part of d₅₆/2⁹/2⁴⁷, so `R₁` **is** the integer part of d₅₆/2⁹/2⁴⁷.

***Rule: We can isolate `Rᵢ` if the coefficients of `Rᵢ` and `Rᵢ₊₁` (e.g., `R₁` in `R₁` and `R₂`, or `R₂` in `R₂` and `R₃`) differ by a factor of 2⁷ or more. (It is a little complicated than that, as I did not prove that the sum of these less-than-1 numbers is still less than 1. At least it works here ¯\_(ツ)_/¯)***

(In the previous case, coefficients of `R₁` and `R₂` differ by 2²⁸)

Similarly, we can derive `R₂`, now that `R₁` is known. (Coefficients of `R₂` and `R₃` differ by 2¹⁰)

#### Day 170
On day 170:

![2^{170}R_1+2^{85}R_2+2^{56}R_3+2^{42}R_4+2^{34}R_5+2^{28}R_6=d_{170}](https://latex.codecogs.com/svg.latex?2%5E%7B170%7DR_1&plus;2%5E%7B85%7DR_2&plus;2%5E%7B56%7DR_3&plus;2%5E%7B42%7DR_4&plus;2%5E%7B34%7DR_5&plus;2%5E%7B28%7DR_6%3Dd_%7B170%7D)

Notice that:

![2^{170}R_1+2^{85}R_2=2^{63}(2^{107}R_1+2^{22}R_2)](https://latex.codecogs.com/svg.latex?2%5E%7B170%7DR_1&plus;2%5E%7B85%7DR_2%3D2%5E%7B63%7D%282%5E%7B107%7DR_1&plus;2%5E%7B22%7DR_2%29)

As there's a factor of 2⁶³:

![2^{170}R_1+2^{85}R_2\equiv0\mod 2^{63}](https://latex.codecogs.com/svg.latex?2%5E%7B170%7DR_1&plus;2%5E%7B85%7DR_2%5Cequiv0%5Cmod%202%5E%7B63%7D)

(If you're not sure why, think about the definition of [modulo operation](https://en.wikipedia.org/wiki/Modulo_operation)).

Anyhow, the judge now, modding the result by 2⁶³, conveniently got rid of `R₁` and `R₂` for us. Using the ***Rule*** above, we can figure out `R₃` and `R₄`. (Coefficients of `R₃` and `R₄` differ by 2¹⁴, and coefficients of `R₄` and `R₅` differ by 2⁸).

The only unknowns left are `R₅` and `R₆`, and there are two independent equations that can be used...
