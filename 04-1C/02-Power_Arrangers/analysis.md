#   Power Arrangers: Analysis
##  My Approach
Each letter should appear 24 times at each position, and if a letter appears fewer than 120, the letter at that position is missing.

1. Check all 119 letters at the first position. Find the letter that has only 23 entries. That is the first one of the missing combination
2. For the 23, check their second position. The letter with 5 entries is the second letter of the missing. (Other letters have 6)
3. For the 5, check their third position. The letter with only 1 entry is the third letter of the missing. (Other letters have 2)
4. Check the fourth position. The letter is the **fifth** letter of the missing.
5. The letter not present in the previous four is the fourth letter of the missing.
