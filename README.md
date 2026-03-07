# Programming Assignment 2: Greedy Algorithms
###### Pryce Houck, Trevor DeBored

### Question 1: Empirical Comparison
| Input File | k | m | FIFO | LRU | OPTFF |
|---|---|---|---|---|---|
| Input_1_050 | 7 | 50 | 39 | 38 | 30 |
| Input_2_100 | 10 | 100 | 74 | 66 | 55 |
| Input_3_150 | 12 | 150 | 103 | 92 | 80 |

### Question 2: Bad Sequence for LRU or FIFO
FIFO  : 43  
LRU   : 43  
OPTFF : 37  

3 50  
681295 901572 937107 681295 916551 681295 949962 393130 500786 744685 798711 469738 520967 798711 665199 977385 624940 847559 500786 520967 133222 265048 428767 265048 500786 265048 798711 465135 798711 500786 520967 265048 285238 288787 615055 604460 520967 681295 439118 681295 882473 798711 500786 394707 520967 249532 265048 731796 921194 307640

### Question 3: Prove OPTFF is Optimal
[PROOF\]

 Let S be a reduced schedule that makes the same eviction decisions as $S_{FF}$ through the first j items in the sequence, for a number j. Then there is a reduced schedule $S'$ that makes the same eviction decisions as $S_{FF}$ through the first j + 1 items, and incurs no more misses than S does.

- Suppose $S$ and $S_{FF}$ have identical cache contents up to step $j + 1$.
- Consider the first time that $S$ and $S_{FF}$ diverge in behavior, say at step $j + 2$, where $S$ evicts the element $n_{\text{soon}}$ and $S_{FF}$ evicts the element $n_{\text{far}}$.
- Perform an exchange such that the modified schedule $S'$ evicts $n_{\text{far}}$ instead to resemble the behavior of $S_{FF}$. This gives rise to two cases:
	- Case 1: $n_{\text{soon}}$ is not requested before $n_{\text{far}}$
		- Then $S'$ has at most as many misses as $S$ because $n_{\text{soon}}$ stays in the cache for longer.
	- Case 2: $n_{\text{soon}}$ is requested before $n_{\text{far}}$
		- Then $S$ would have missed $n_{\text{soon}}$ sooner since $S'$ would still have it in the cache at that point. $S'$ may eventually need to bring $n_{\text{far}}$ back into the cache, so $S'$ would have at most as many misses as $S$.
- By both of these cases, $S' = S_{FF}$ will never incur more misses than any other schedule $S$, and is thus optimal.