#   Golf Gophers: Analysis
##  My Approach
Three words: [Chinese remainder theorem](https://en.wikipedia.org/wiki/Chinese_remainder_theorem). Using coprime integers (I used power of primes), this script can recognize up to 12,252,240 gophers. Please consult the previous Wikipedia article if you're not familiar with the theorem. Each day, a power of the prime is used as the number of blades for all windmills, to get the remainder of the number of gophers modulo number of blades, and then Chinese remainder theorem is used to calculate the number of gophers.
