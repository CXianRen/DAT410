# The Netflix Prize 
+ what is the problem ?
+ how does the problem was solved ?
+ what are the advantages and disadvantage ?
+ can do it better?

Introduction:
  Cinematch recommendation system:  
    1. give out a list of "similiar movies" based on accumulated movie ratings (why use accunulated?)
    2. base on the list, provide a unique personalized prediction.
    3. Fallback: if no personalized prediction is avaible, using the average rating based on all ratings.

THE NETFLIX PRIZE
  what is it, and what is it expecting.
  information about the data set:
    1. 100 million ratings from 480 thousand subscribers
    2. 18 thousand movie titles.
    3. ratings are on a scale from 1 to 5 (integral)
    4. 3 milling qualifying set.
  
FORMATION OF THE TRAINING SET
  what are included in the data set. and how is it created.

  Prize dataset (the training set)
  1. probe subset (used for?)
  2. qualifying set
     1. quiz and test subsets

# Lessons from the Netflix Prize Challenge

## INTRODUCTION
1. it was importnat to utilize a variety of models that complement the shortcomings of eacher.
    1. KNN (nearest neightbor models)
    2. latent factor modesls such as SVD 
    3. restricted Boltzmann machines.
2. it was importnant to include models that incorporated infomration beyond the ratings themselves
   1. what movies a particular user rated.
3. improved existing collaborative filtering methods.
   1. A new method for computing nearset neightbor interpolation weights (how?) (what about the original one)
   2. A negithborhood-aware factorization method. (what is this?)
   3. integration of information about which movies a user rated into latent factor models. (what is this?) 

## UTILIZAING A COMPLEMENTARY SET OF MODELS
+ KNN
  + are most ffective at detecting very localized relationships.
  + The item meighborhood approach : predit an unrated item based on similar items by the same user.  (a user rated A, and B is similar to A but not rated, the ratings of B by this user can be predict according to A (but need a algotithm to identify the similiar items))
  + The user approach: try to find out similar users. (be not used in this paper.)
+ Latent factor models
  + good at estimating overall structure (most or all movies), are poor at detecting strong associations among a sall set of closely related movies such as The Lord of the Rings trilogy. (KNN models do best)
  + SVD (for not missing data)
  + Restricted Boltzmann machines ()
+ predict which movies users rate, regardless of how they rated. (using infomration out of ratings (like what moives they rated!!!))

## IMPROVING EXISTING METHODS

### Weights for Neighborhood Models

```math
r_{ui} \lArr b_{ui} + \frac{\sum_{j \in N(i,u)} s_{ij} (r_{uj} - b_{uj}) } { \sum_{j \in N(i,u)} s_{ij} }
```

  + (?) how to define similarity $s_{ij}$ ?
    + Pearson correlation coefficient 
    + closely related cosine similarity.
  + baseline predictor $b_{ij}$ (what and how ?)
    + mean rating of user u
    + or mean rating of item i
    + a more comprehensive approach 

#### advantage:
+ are intuitive (easy to understand)
+ relatively simple to implement
  + do not require tuning many parameters or an extensive training stage.
  + provide a concise and intuitive justification for the computed prediction

#### disadvantage:

+ There are some problems using standard method to estimate similarity  
+ do not account for interactions among neighbors.
+ should ignore the neighborhood information if there is no useful neightbors. but standard method doesn't.
+ maynot work well if variability differs substantially among neightbors.

QA: what is interpolation weights ?
+ here, it is the base line score $b_{i}$. 

#### how to solve it
+ new function with $w$ allowing downplay neightborhood information when lacking infomrative negithbors.
+ learn $w$ by solvig a least suqares problems.
  + (?) how to cope with the missing values.



### Latent Factor Models
to extract the feature matrix. (for movies and users) and to estimate rating.

+ 3 different way to improve
  + deepen the foundations of the model by assuming a more flexible and realistic probabilistic model.
  + introducing complementing perspectives of the data into the model: local view or the binary view (best result in the paper).

### Regularization

+ shrinkage to improve similarity scores used for nearest neighbor selection.
[Modeling Relationships at Multiple Scales to Improve Accuracy of Large Recommender Systems]()

+ shrkinkage of estimated inner products (interpolation weights) 
[Improved Neighborhood based Collaborative Filtering]()

+ use ridge regression for regularization.

+ remove of global effects used empirical Bayes shrinkage 
[[Improved Neighborhood based Collaborative Filtering]()
]()

###

QA: What is Pearson correlation coefficient:
[Pearson correlation coefficient](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient)

calculate Pearson corrleation coeeficient with Python3.
```python3
import numpy as np

# Two example vectors
vector1 = np.array([1, 2, 3, 4, 5])
vector2 = np.array([2, 3, 4, 5, 6])

# Calculate the Pearson correlation coefficient
correlation_coefficient = np.corrcoef(vector1, vector2)[0, 1]

print("Vector 1:", vector1)
print("Vector 2:", vector2)
print("Pearson correlation coefficient:", correlation_coefficient)
```

QA: What is "the closely related cosine similarity" ?
[cosine similarity](https://en.wikipedia.org/wiki/Cosine_similarity)

```python3
import numpy as np

# Example vectors
vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])

# Calculate cosine similarity
dot_product = np.dot(vector1, vector2)
norm_vector1 = np.linalg.norm(vector1)
norm_vector2 = np.linalg.norm(vector2)

cosine_similarity = dot_product / (norm_vector1 * norm_vector2)

print(f"Cosine Similarity: {cosine_similarity}")
```