#   Foregone Solution: Analysis
##  My Approach
This is rather straightforward. The input number is scanned character-by-character as a string. If the character is `4`, then `A` gets `1` and `B` gets `3`. Else, `A` gets `0` and `B` gets the number. `A` is converted to integer at the end to eliminate preceding `0`'s

To simplify more, just replace all the `4`'s as `3`'s, and the other number is the difference
