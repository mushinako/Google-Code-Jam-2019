#   Dat Bae: Analysis
##  Extra Files
* `testing_tool-mod.py`: Focuses on the (**N**, **B**, **F**) = (1024, 15, 5) case

##  My Approach
The key here is that there can be at most `15` errors. Therefore, divide all machines into groups of 16. Then, the following is true:

* At most 15 groups contain faulty machines
* No single group can be all faulty

Therefore, for the 1st query, we send alternating `0` and `1` blocks of size 16 (like `000000000000000011111111111111110000`), and we check the response for each group. The number of decreases in `0` or `1` is the number of errors in that group, and no groups can be empty

Now we have at most 15 groups of at most 16 (the final group may have less than 16 machines, depending on the total number of machines). For each group, the machines can be id-ed by a 4-bit number `0000b` to `1111b` Check for each digit once, and all 15 (at most) groups can be done simultaneously

### More detailed explanation
The binaries of numbers are as follows (The first query is the alternating 16-sized blocks):

| Query   | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  | 11  | 12  | 13  | 14  | 15  |
| :-----: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| **2nd** | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 1   | 1   | 1   | 1   | 1   | 1   | 1   | 1   |
| **3rd** | 0   | 0   | 0   | 0   | 1   | 1   | 1   | 1   | 0   | 0   | 0   | 0   | 1   | 1   | 1   | 1   |
| **4th** | 0   | 0   | 1   | 1   | 0   | 0   | 1   | 1   | 0   | 0   | 1   | 1   | 0   | 0   | 1   | 1   |
| **5th** | 0   | 1   | 0   | 1   | 0   | 1   | 0   | 1   | 0   | 1   | 0   | 1   | 0   | 1   | 0   | 1   |

If a machine is broken, the returning value would miss the position for all 4 queries

E.g., `0`, `4`, `7`, `10`, and `15` are broken, then the results would be:

| Query   | Result      | Description                          |
| :-----: | :---------: | :----------------------------------: |
| **2nd** | 00000111111 | ~~0~~000~~0~~00~~0~~11~~1~~1111~~1~~ |
| **3rd** | 00011000111 | ~~0~~000~~1~~11~~1~~00~~0~~0111~~1~~ |
| **4th** | 01101001001 | ~~0~~011~~0~~01~~1~~00~~1~~1001~~1~~ |
| **5th** | 10110011010 | ~~0~~101~~0~~10~~1~~01~~0~~1010~~1~~ |

To parse the output, convert each column back to numbers. These are the working machines:

| Query      |       |       |       |       |       |       |       |        |        |        |        |
| :--------: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :----: | :----: | :----: | :----: |
| **2nd**    | 0     | 0     | 0     | 0     | 0     | 1     | 1     | 1      | 1      | 1      | 1      |
| **3rd**    | 0     | 0     | 0     | 1     | 1     | 0     | 0     | 0      | 1      | 1      | 1      |
| **4th**    | 0     | 1     | 1     | 0     | 1     | 0     | 0     | 1      | 0      | 0      | 1      |
| **5th**    | 1     | 0     | 1     | 1     | 0     | 0     | 1     | 1      | 0      | 1      | 0      |
| **Base10** | **1** | **2** | **3** | **5** | **6** | **8** | **9** | **11** | **12** | **13** | **14** |

The broken machines have ID's **not** present in the result. As the ID's range from `0` to `15` (incl.), the broken ones are `0`, `4`, `7`, `10`, and `15` **in this group**. To get their real position, add their relative positions in the group to the number of machines before this group
