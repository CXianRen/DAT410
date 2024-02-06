 Hidden Technical Debt in Machine Learning Systems
 
 This paper talks about manily in software engineering framework of technical debt. 

# Abstract
+ why maintaining the ML system is difficult and expensive.
  + what is techinical debt, what it will cause?
    + the long term costs incuured by moving quickly in software engineering.
      + deferring such payments results in comounding costs
      + hidden debt is dangerous
  + this kind of debt for ML system may be difficult to detect because
    + it exists at the system level rather than the code level
    + traditional abstractions and boundaries may be subtly corrupted or invalidated by the fact that data inluences ML system behavior.
  
# Complex Models Erode Boundaries
## Entanglement
  + No inputs are ever really independent.
  + CACE: changing anything changes everthing.
  
  + solution:
    + ioslate models and serve ensembles.
    + focus on detecting changes in prediction behavior

## Correction Cascades
  + using an extrac model to correct the output of a using model.
  + complicate the system


## Undeclared consumers
  + actually is visibility debt in more classical software engineering.
  + solution:
    + well desgined system. (access restrictions)


# Data Dependencise Cost More than Code Dependencies 
+ no tool like static analysis (compiler and linker) to identify the dependencise in ML system.

## Unstable Data Dependencies
+ some input signals are unstable  (qualitaively or quantitatively change behavior over time)
  
+ solution:
  + !!! copy the original data localy.

## Underutilized Data Dependencise
+ can not provide large benefit and can be removed without detriment (oftentimes)

+ From serveral ways
  + Legacy Features
  + Bundled Features
  + $\epsilon$-Features
  + Correlated Features

+ solution:
  + can be detected via exhasutive leave-one-feature-out evaluations.

## Static Analysis of Data Dependencies
+ new tools are needed!

# Feedback Loops
+ ML systems is updated frequently, which might leads to a form of analsysis debt, difficult to predict the behaior of a given model befor it is released.

## Direct Feedback Loops
+ A model may directly influence the selection of its own future training data. 

+ solution:
  + radomization!
  + ioslating


## Hidden Feedback Loops
+ two systems influence each other indirectly through the world.

# ML-System Anti-Patterns
+ It is unfortunately common for systems that incorporate machine learning methods to end up with high-debt design patterns.

## Glue Code
+ solution: wrap black-box packages into common API’s.


## Pipeline Jungle
+ often appear in data preparation
+  can evolve organically, as new signals are identified and new information sources added incrementally


## Dead Experimental Codepaths
+ solution: re-examine each experimental branch periodically.

## Abstraction Debt
+ there is not a commonly acceptable abstraction of ML system.

## Common Smells
+ Plain-Old-Data Type Smell
+ Multiple-Language Smell
+ Prototype Smell

# Configuration Debt
+ Any large system has a wide range of configurable options, including which features are used, how data is selected, a wide variety of algorithm-specific learning settings potential pre- or post-processing, verification methods, etc. 

# Dealing with Changes in the External World 
## Fixed Thresholds in Dynamic Systems
+ if a model updates on new data, the old manually set threshold may be invalid.

## Monitoring and Testing
+ What to monitor?
  + Prediction Bias.
  + Action Limits
  + Up-Stream Producers

# Other Areas of ML-related Debt

+ Data Testing Debt
+ Reproducibility Debt
+ Process Mangement Debt
+ Cultural Debt
