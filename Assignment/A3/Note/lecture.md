# AI tool

## Data represnetation & processing

+ What is "typical" ML data?
  + most of time, data is stored in matrices/vectors

+ More general data
  + do not have natural tabular representations.

+ Image 

+ Graphs
  + represent relations of people,atoms, cities, ...

+ The ubiquity of matrices
  + matrices and vectos are used to represnet (test,images and speech data)

+ Why matrices?
  + Almost all ML builds heavily on linear algebra 
    + Linear regression
    + Deep neural networks
    + Linear programming
  + Matrix/vecotr multiplications are fast, well-understaood.

+ !! Exceptions 
  + the decision trees

+ Data frames
  + a drawback of pure matrix/tensor: columns and rows are "anonymous"
  + Data frames add indices and names, much like a spreadsheet

+ Hndling different kinds of data
  + Machine learning is staill at a point where each data type is handled by slightly different methods

+ Data is not stored in matrices 
  + Most data is not stored with ML in mind.

+ Missing values 
  + how to handle it?
    + represent missing values by a missingness mask M

  + Two common solutions
    + 1. Imputation
      + attempt to impute missing values
        + reconstruct X from $\~X$
        + predict Y from reconstructed X
      + any method that works for X works for reconstruction ?
    + Informative missingness
      + make use of missingnes itself
        + predict Y using both $\~X$ and M
      + two common approaches:
        + method sensitive to M 
        + simple impuation + missing indicators
  
+ Single imputation
  + the basic idea: to predict the missing value from observed values of other variables
    + can be leared by regression on complete observations or observations with less missingness
  
+ Multiple iterative imputation
  + (MICE) Multiple Imputation by Chained Equations
  + Multiple impuation:
    + Greates more than one smaple of each missing value to account for variance.
  + Chained equations: Imputes one value based on imputations of other variables - works without any complete observations.

+ Predicting with missingness indicators
  + When data is not missing at random (MAR), imputation methods may fail.
  + A common method:
    + stich a simple imputation and M as binary indicators, together for prediction.

## Model development

+ Fit, predict, score pattern

```python3 
class Classifier():
  def fit(x,y):
    pass
  def predict(x):
    pass
  def score(x,y):
    pass

C = Classifier()
C.fit(X_train, Y_train)
C.predict(x_new)
```

+ Scikit-learn (sklearn)


+ Standardize
  + to make them have mean 0 and standard deviation 1
```math
  X' = \frac{X-u(X)}{\sigma(X)}
```

+ transformations
  + Scikit-learn implements data preprocessing in transformations

## Differentiable systems
+ Empirical risk minimization (ERM)
  + to find optimal $\theta$, but how?
    + based on ERM in differentiable systems.

+ Gradient descent (GD)

+ Automating gradient descent
  + how to compute the gradient.
    + back-propagation
    +  