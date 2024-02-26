
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

# Learning to play
+ two problems with large state spaces
  + we can't explore every state
  + we can't store the value of each state

+ what if we try only some actions?
  + How do we make sure we don't leave out good ones.
## Monte-Carlo tree search
### step-1: Selection
+ finding unexplored nodes - state-action pairs that haven't been tried
+ based on what we know so far, traverse down until an unexplored child node is reached 
+ traversal uses a tree policy for selection

detail example see ppt page 40.

+ ? we know some rewards and visit, how do we traverse the tree
  + tree policy
+ ? what is a good tree policy
  + selecting nodes randomlu is very inefficient
  + the statistics we collect can be used to improve selection during MCTS and the action we choose to play in the end.
    + ? how should we balance trying new things and using knowledge

#### greedy policies
+ **Problem**: this leads to no exploration
<!-- 因为总是根据已知的选最好的，可能在次优里面有好的 -->
+ this is good when Q is a very good approximation of value, but it is not that good in most cases. 

#### e-greedy policies 
+ An e-greedy polocy chooses the greedy action with probability 1-e, and a random action with probability e.
+ trades off exploration and exploitation a little.
+ **Problem**: May try an action known to be bad, by chacne

#### Upper confidence bounds (UCB)
+ why have such idea? 
  + it is based on [concentration inequalities](https://en.wikipedia.org/wiki/Concentration_inequality) 
+ Bound on the true Q-value for an action a in node v
  + ??? how to know true Q value ? - no needed
```math 
  Q(v_a)_{true} \le Q_t(v_a)_{estimated} + U_t(v_a)
```
+ see more in ppt page 52,53

### step-2: expansion 
<!-- 扩张 -->
+ Once a node has been selected, it is expanded.
+ an univisted child node is selected 
+ this is critical to avoid leaving out good moves
+ we must now evaluate this node - ???? how ???

### step-3: simulation/roll-out
+ once an unvisited child node is selected, we simulate the game starting here
+ Based on a simulation policy, typically a simple random policy, we continute playing from the expansion node until a terminal node
+ At the terminal node, we know the value!

### step-4: backpropagation
+ once we know the value of a terminal node, we backpropagate it through the tree
+ we update our idea of how good moves were 
+ the expanded node is marked as visited
+ statistics of nodes are updated, for example
  + number of visists, N(v) ???? 
  + total reward starting there, Q(v)

### fiishing the search
+ MCTS is repeated until sufficient statistics have been gathered. 
  + ???? how to know the iteration number is sufficient ??? 

+ choose the action corresponding to the most visited state. 
  + ??? why 

### Function approximation
+ the details of each state matter less, the more information there is. there are similarities
+ we recognize these similarities and disregard irrelevant information.

+ instead of storing the Q value of each node in the tree, we let a fuction approximate it. Q(s,a): the average reward after taking action a in state s.
+ we use machine learning to learn the value of states

+ this means:
  + dont have to manually encode the quality of actions.
  + dont have to explore every state to predict its value.

### Exploration/exploitation


## Machine learning
