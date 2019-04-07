#   Cryptopangrams: Analysis
##  Extra Files
* `primes.txt`: List of primes up to 500,000
* `test-gen.py`: Generate some test cases using `primes.txt` into a new file `test.in`, and respective solutions into `sol.txt`. Use `python3 test-gen.py n`, where `n` is the number of test cases you want

##  My Approach
Adjacent products must have a unique common divisor that is a prime, unless that these products are the same. To avoid the same-value scenario when calculating the common divisor, any duplicates are moved to another list to be considered later. The first common divisor is retrieved using [Euclidean algorithm](https://en.wikipedia.org/wiki/Euclidean_algorithm), and once one prime is got, the rest can be got via simple division. A list of primes is obtained, and the unique ones are sorted to establish the prime-letter correspondence. The only thing left is to replace the primes with the letters.
