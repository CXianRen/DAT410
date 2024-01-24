### Type of problem (modelleing method)(有什么类型的问题 一般来说)

#### Fuction 
+ give some input and then get some output. this type of problem can be seen as trying to seach a function mapping input to output.
##### Regression Problems
  + to predict continuse output.
  + M: 
    + linear regression, 
    + polynomial regression. 
    + support vector regression (SVR), 
    + Ridge regression.
  + E:
    + to predict the house prices base on the feature
      + input : the areas, location
      + output : the price 

##### Classification Problems
  + to classificate data into different classes. 
  + M:
    + Logistic Regression
    + Decision Trees
    + Random Forests
    + Support Vector Machines
    + Neural Networks
  + E:
    + using logistic regression, according the content of email to block spam eamil

##### Optimization problems
  + used to find the optimal solution in a system.
  + M:
    + Linear Programming
    + Nonlinear Programming
    + Interger Programming
    + Genetic Algorithms
  + E:
    + to make the maximum profit with limited resource. using linear programming, considering production costs and sales revenu, find the optimal level of product output.

##### Fuction Approximating Problem
  + Used to approximated complex functions or curves.
  + M: 
    + Polynomial Fitting
    + Spline Interpolation
    + Kernel Methods

##### Time Series Prediction Problem (vs Regession problems?)
  + used for prediction variables that change over time.
  + M:
    + autoregressive integrated moving average (ARIMA)
    + Long Short-Term Memory (LSTM)
    + Neural Network Time Series (NNTS)
  + E:
    + predict the temperature. 
    + using ARIMA model, based on the past week's temperature data, predict the temparatue for the upcoming day. 

##### Control System Problems
  + used for designing automatic control systems to meet performance requirments
  + M:
    + state-spacee models 
    + PID controllers 
    + linear quadratic regulator  线性二次调节器
  + E:
    + airplane controlling system
    + using state-space model and PID controller, ensure that the aircraft maintains a specific filight altitude.

##### Feature Selection Problems
  + used for selecting the most informativer input features
  + M:
    + Variance threshilding 
    + recursive feature elimination
    + Tree-based Feature Importance
  + E:
    + using Tree-based Fretur Importance model, based on genetic data, selected the most significant gene to predict a disease. 

#### QA
(1) what is the different between regression and time series prediction problem?
  + time series prediction is a subset of regression problem. 



#### Optimization Problem 

+ this type of problem is trying to select the best solution from a set of possible solutions

##### Unconstrained Optimization Problems.
+ try to find the soultion yieilding the maximium or minimum result, without considering any constraints.  

##### Constrained Optimization Problem

##### Integer Programming Problem

##### Linear Programming Problem 

##### Nonlinear Programming Problem

##### Multi-Objective Optimization Problems

##### Global Optimization Problems

##### Convex Optimization Problems

##### Discrete Optimization Problems



#### Dynamic system
+ dynamic systems: the state of the system evolves with respect to time and the behavior of the system is influnenced by various factors and interactions. these problems often deal with understanding how a system's state changes, predicting future states, or designing control strategies to achieve desired outcomes.

+ example:
  + Control system: like temperature control in a furnace or altitude control in an aircraft.
  + Economic systems: modeling economic systems to understand how factors such as interest rates, inflation, and government policies influence economic growth over time.
  + Biological system: studying the dynamics of populations in ecology, the spread of disease, or the behavior of bioligcial organisms over time.
  + Mechanical system: analyzing the motion of objects subjected to forces, such as the movement of a pendulum or the response of a vibrating structure. 


#### Discrete algorithmic problem 
+ A discrete algorithmic problem refers to a computational problem that deals with discrete, often countable, elements or values. In this context, "discrete" means individual and separate rather than continuous. These problems typically involve finding an algorithmic solution or making decisions based on a set of discrete data points or objects.

+ Key feature:
  + Countable Elements:The problem involves working with data or variables that can be enumerated or counted individually.

  + Decision-Making: The goal is often to make decisions or solve problems based on discrete choices or conditions.

  + Algorithmic Solution: Discrete algorithmic problems require the design and implementation of algorithms to solve them. These algorithms may involve step-by-step procedures for decision-making or computation.

+ Example:
  + Sorting Algorithms: Arranging a list of items in a particular order (e.g., alphabetical or numerical).
  + Graph Algorithms: Solving problems related to graphs, such as finding the shortest path, detecting cycles, or determining connectivity.
  + Combinatorial Optimization: Finding the best combination of discrete elements to optimize a certain objective, like the traveling salesman problem.
  + Search Algorithms: Locating a specific element or value within a collection of data.
  + Boolean Logic Problems: Solving problems involving binary decision variables and logical operations.

#### Constraint satisfaction problem
+ A Constraint Satisfaction Problem (CSP) is a computational problem where the goal is to find a solution to a set of variables, each with specific domains, that satisfies a given set of constraints. In other words, it involves finding values for variables within specified domains such that all constraints are satisfied simultaneously.

