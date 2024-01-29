
### Motivation:
how to sell something if you have tons of product?(which you need to display to users to make them place an order?)

### Solution 1 (A uniform strategy):

displayer the best sell product to everyone!

Disadvantage:
might work, but not everyone like it. Can we do better?

### Solution 2 (A personalized policy)

each user is assigned their own recommendations. (how?)
+ try to figure out what the user are thinking about.
+ try to figure the good match (product  to consumer)

#### Models of user preference
+ To distinguish users, we must know somthing about them
  + we could ask them what they like, but not always a good indicator (? why? people don't know what they really like)
  + collect data **passively** (really?)
    + purchase logs  -> predicting future purchases

#### Recommendation systems

##### Objectives & proxies 
###### Objective:
  What do we want?
  Should be the subject of evaluation
  + E:
    + Profit
    + Number of users 
    + User engagement
    + User satisfaction
  + Long-term (delayed) objectives are hard to optimize directly.

  ###### Example 
  ```
  For the bookstore example:
  1. pick an objective 
    + brand awarenees
    + profit 
    + 
  2. how would you measure it ?
    + number of visitor on the site or interaction
    + segement user (for example non members and member, where they are from(IP), )
  3. how would you optimize it?
    + improving ads 
    + suggest high probability items
  ```

###### Proxies
What can we measure and optimize. Something some abstract concept is hard to measure, like engagement. Thus we can use something to indicate it (proxy)

+ A common proxy for user engagement is user ratings
  + ratings are easy to measue. 
    + how many people have rated it
    + how many product a people have rated
    + what type of products a people have rated
    + how often a people rate a product
  + Maximizing user rating
    + how can we recommend products that will be highly rated ?
    + First predict ratings (how to predict?) then pick highly rated product (from the predicted product?)
    + Maximize profit -> maximize engagement -> maximize ratings -> maximize predicted ratings. (就是说得一步一步的分析)

##### Learning to recommend 
###### How does AI fit in ?
1. (Goal) We are looking for a personal mapping fucntion f to map books X to ratings Y. (More specific, to predict a book X will be rated hight score (Y) by a person. if it is, then the book might should be recommanded to this person.?) (Question: different people might have different ratings for different book)

2. (Training) 
   1. we don't know the function f when we start.
   2. but we have records of purchased books X and ratings Y (both belong to a specific customer. Someone buy it and rate it, then there is a pair of data f(x)=y)
   3. then how to figure out which kind of books should be recommand
      1. using historical data (we can know waht kind of catogogy a person like)(user tast) (clustering problem?) (the relation between different books?)

    4. how to model a book (X).
3. recommender
   1. based on user ratings Y, user preferences Θ and product features X
   2. different systems make different assumptions 
   3. A common assuption $Y \sim f(X;θ)$ has a particular form 
   4. For example: $Y=θX$ (matrix multiplication / linear form)

4. example
   1. Linear ratings
   2. Content filtering

+ Recommenders in practice
+ Evaluation and deployment

