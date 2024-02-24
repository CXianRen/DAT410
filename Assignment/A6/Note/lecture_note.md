
# History 
+ the mechanical turk 
+ chess computers
+ DoTA - OpenAI Five

# Formalizing games
## Zero-sum games
+ One player winning implies one player losing
## do we win at games?
+ Games are inherently about actions
+ our goal is to select actions that improve our chances of winning 
+ to win, we account for good/bad futures when selecting actions
### Branching paths
+ Eaxmple: Tic-Tac-Toe
To play optimally, we must pick the best path. But which is it?

#### Tree search
+ Terminal nodes: it looks so many nodes, but actually at some point in the tree, an end state is reached.
<!-- 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 -->
+ value of state: some state will win more possible. (?how to calculate/estimate it?)

+ by identifying good futueres(wins), we can backtrack - Which actions do we have to take to get to the good end?
(?maybe just calculate the number of win state). --- depend on your opponent!!!

+ in a stationary environment, we can do that, just following the probability of success, but what if your opponent adapts? --- Minimize the maximum success of your opponent. 
<!-- 计算不了自己，就计算别人， 问题从如何让自己成功，变成了让对面成功的机率最小 -->


## Games as decision processes
(what is the best move?)

+ taking actions At
+ according to a policy pi
+ in states St， observed Xt
+ which transition according to dynamics $p(S_t|S_{<t},A_{<t})$

<!-- 抽象层后本质就是 有 策略p 根据当前 观察X，和历史状态S 和 历史 操作A 做出 新的决策 a  -->

### Mini-Max games 
+ minimum the maximum probability of the opponent event if it takes the best choice for every step!
```math 
min max R(u,\pi)
```
### Minimax: Aoviding losses

### Minimax: drawbacks
+ huge chekc spaces
+ limited to discrete
+ can't find optimal

### Truncating at finite depth
+ but how do we know the value of non-terminal nodes?

### evaluating non-terminal nodes
#### Early game-playing AI
+ used human knowledge to evaluate states

## Monte-Carlo tree search
### Exploration/exploitation
## Machine learning
