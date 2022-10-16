# Computational-Intelligence

### Lab1 Results

The reduction parameter (RP) introduces a reduction of the least probably significant solution space, removing at each step those nodes who have a low heuristic score.
The smaller the parameter is, the more aggressive the reduction will be. In this way the most interesting combination will be explored, at the price of a slightly
less complete solution. RP=1 means no reduction, but it doesn't follow a mathemtatical precise proportion.

- N = 5; w=5; nodes visited = 3 (RP=1)
- N = 10; w=10; nodes visited = 3 (RP=1)
- N = 20; w=23; nodes visited = 4541 (RP=2/3)
- N = 50; w=66; nodes visited = 113080 (RP=1/2)
