# Programming Assignment 2: Greedy Algorithms
###### Pryce Houck, Trevor DeBored
remove __pycache__ if you're having issue compiling

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

We believe Proof attempt 2 is more precise but may be unnecessarily verbose. We belive both are correct and included both to cover our bases and get feedback.

Proof attempt 1:
 Let S be a reduced schedule that makes the same eviction decisions as $S_{FF}$ through the first j items in the sequence, for a number j. Then there is a reduced schedule $S'$ that makes the same eviction decisions as $S_{FF}$ through the first j + 1 items, and incurs no more misses than S does.

- Suppose $S$ and $S_{FF}$ have identical cache contents up to step $j + 1$.
- Consider the first time that $S$ and $S_{FF}$ diverge in behavior, say at step $j + 2$, where $S$ evicts the element $n_{\text{soon}}$ and $S_{FF}$ evicts the element $n_{\text{far}}$.
- Perform an exchange such that the modified schedule $S'$ evicts $n_{\text{far}}$ instead to resemble the behavior of $S_{FF}$. This gives rise to two cases:
	- Case 1: $n_{\text{soon}}$ is not requested before $n_{\text{far}}$
		- Then $S'$ has at most as many misses as $S$ because $n_{\text{soon}}$ stays in the cache for longer.
	- Case 2: $n_{\text{soon}}$ is requested before $n_{\text{far}}$
		- Then $S$ would have missed $n_{\text{soon}}$ sooner since $S'$ would still have it in the cache at that point. $S'$ may eventually need to bring $n_{\text{far}}$ back into the cache, so $S'$ would have at most as many misses as $S$.
- By both of these cases, $S' = S_{FF}$ will never incur more misses than any other schedule $S$, and is thus optimal.

Proof attempt 2:
Consider an arbitrary list of elements A. Let S_FF denote the schedule produced by OPTFF and let S* denote the optimal schedule with the minimum possible number of misses. If S_FF = S* and has the same number of misses, then S_FF must be optimal.

Consider the schedule S = S_FF for the first j elements. Consider the j+1 iteration for element a, which is the the (j+1)st element in A. 
Consider the following 3 cases
**Case 1 a is in the cache for S and S_FF**
	no eviction decision is necessary
**Case 2 a is not in the cache for S or S_FF and both S and S_FF evict the same element**
	S and S_FF still match for the (j+1)st element, S = S_FF.
**Case 3 a is not in the cache for S or S_FF and S eviction differs from S_FF eviction**
	S now has some a_1 element in the cache, while S_FF has some a_2 element in the cache, but they match up until that point.
	Let S' = S for the first j iterations, have S' decide to evict a_2, now matching S_FF for the (j+1)st elements. S' = S_FF for the first j+1 iterations. Both S and S' have the same number of misses up to this point.

Consider the following 2 cases within case 3 for the (j+2)nd element to ensure there S' has no more misses than S
**Case 3_1 S' and S both evict an element to make room for an element a_3**
Consider now the (j+2)nd element in A for S' and S, where there is a request for element a_3, not within S' or S. If S chooses to evict a_1 to make room for a_3, then S' can choose to evict a_2, making S' = to S, and thus, S_FF = S via the transitive property. Let S_FF behave like S for the rest of the sequence, so S_FF must have the same number of misses as S, proving that S_FF is optimal.
**Case 3_2 S evicts some element a_4 = a_2 to make room for a_1**
 Consider a request for a_1. S evict an item a_4. If a_4 = a_2, then S' can evict a_2 for a_1, making S' = S, with the same number of misses.
 
**Case 3_3 S evicts some element a_4 != a_2 to make room for a_1** 
S' evicts a_2 to make room for a_1, so S and S' now have the same caches, but S' is no longer reduced. Let S' = S'', a reduced schedule, such that it doesn't increase the number of items brought in by S', but still agrees with S_FF for the first j+1 iterations. This will not come up by nature of the Farthest in Future Algorithm due to the previous eviction of a_1.

For all possible cases, S' agrees with S_FF for the first j+1 iterations and incurs no more misses than S, and based on the Farthest in Future algorithm, one of these cases, 3_1, 3_2, will arise before case 3_3 because in step j+1 the algorithm evicted a_1 in order of which would be needed farthest in the future, so there would have to be a request to a_2 beforehand, and thus case 3_2 would apply.

Therefore, for any optimal schedule S*, there will be some schedule S which agrees with S_FF for some j+1 iterations, which continues inductively producing some S' = S and thus equating S = S' = S_FF for all elements in A. Each schedule S' incurs no more misses than the previous one. Thus S_FF incurs no more misses than any other optimal schedule S* and hence, is optimal itself.