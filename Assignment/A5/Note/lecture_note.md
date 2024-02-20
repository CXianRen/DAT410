

# Introduction to natural language processing

+ processing language is central in AI research and applications
  + spoken and written language
  
+ AIN philosophy, many arguments involve language understanding 
  + Turing test, Chinese room, ...

## Some applications of NLP

+ spam filters (垃圾邮件)
+ spellchekers and grammar checkers
+ machine translation systems
+ spoken UIs, dialogue systems
+ (search engines?)

## what's different about language from other types of "data"?
+ discrete 
+ structured
+ diverse
+ sparse

## typology of tasks in NLP
+ categorization tasks
  + example: 
    + groups text according to their content.
    + the relation between the text, like contradction

+ tagging tasks

+ parsing tasks
  + example: 
    + grammer
    + coherence, the inner logic

+ generation tasks
  + example: translation

## high-level history of NLP techniques
+ early days, rule-based method 
+ late 80s, data-driven techniques
  + precursor in speech and IR
  + linear models (probabilistic)
  + linear models (dsicriminative)
  + neural models

## two way:

### way 1:
  + tagging 
  + parsing 

### way 2:
  + end to end

+ linear models are still strong baselines for many NLP tasks: very easy and fast to train!

# Machine translation: overview

given a text in asource langueag, gnerate a text in a target language. 

## interlingua-based translation

idea:
+ map the sour-language sentence into some "meaning representation" or interlingua. (超大模型是否就是这样子)
(是否只是编码了大部分概念?, 是否是无限的?)
+ then convert the representation into the target language.

## domain-specific MT systems
+ rule-based MT and interlingusa have turned out to be impractical for open-ended MT, but can be workable in restricted settings

## data-driven machine translations systems

### statistical MT systmes
+ word-based and phrase-based 

### neural MT systems

### about the data: parallel text data

+ some data set:
  + Europarl, http://www.statmt.org/europarl
  + Opus http://opus.nlpl.eu/
  + the Bible (?)

### fundamental idea in neural MT
+ the architecture used in neural MT systems (encoder-decoder or sequence-to-sequence):
  + encoder: "summarize" the information in the source sentence 
  + decoder: based on the encoding, generate the target-language output in a step bu step fashion.

# statistical machine translation with the IBM models

## word-based MT and the IBM models

+ the IBM models (Brown et al., 1993) are models for word-based statistical MT

+ there are 5 IBM models of increasing complexity

+ they revolutionized the field and were a part of most MT systems until the introduction of neural models


## probabilistic machine translation: goals

+ select the most probable English sentence, given F
```math
E^* = max_E P(E|F)
```

## decomposing the probability

```math
E^* = max_E P(E)P(F|E)
```

+ division of labor
  + P(F|E) (tanslation model) can make sure we have the right content, P(E)(language model) can take care of the fluency.

+ easiser to train：
  + P(E) just need English text

In other word, you can train the probability of each language, then train the relationship between two languanges.


## a probabilistic language module
a language model assigns a probability to a sequence of words

+ base on condition probability. probability of the next word:

```math
P(W_n|W_1,...,W_{n-1}) = P(door| please, open, the)
```

+ can rewrite using the chain rule:
```math
  P(w_1,...w_n) = P(w_n|w_1,...,w_{n-1})P(w_1,...,w_{n-1})
```

### the Markov assumption

the next word depends on the current word, but not the rest of the history.

P(door|please, open, the) $\approx$ P(door|the)


### a bigram language model
using markov prabability to replace the conditional probabitilty memntioned above, such a model called bigram model.

### estimating the probabilities in a bigram model
```math
P_{MLE}(w_n|w_{n-1}) = \frac{w_{n-1},w_n}{count(w_{n-1})}
```
example:
```math
P_{MLE}(open|please) = \frac{please open}{please}
```

## the translation model

### word alignments
+ every French word is aligned with one English word.

+ (what if it is not aligned ?): using dummy null word. 

### parameters and independence assumptions
+ each French word dependes only on the English word it is aligned to, e use a WORD translation probability t(f |e)
+ alignments are independent of each other

### estimating translation probabilites

+ ? how do we estimate the WORD tanslation probabilites t(f|e)?
  + the maximum likehood:
```math
t_{MLE}(chat|cat) = \frac{c(\text{cat -> chat})}{\text{cat}}
```

### what if alignments aren't available?
+  Expectation–Maximization algorithm to the rescue


## EM in general 
EM solves the “chicken-and-egg” problem of estimating parameters when some parts of the model are latent (hidden).

### two steps

+ E-step: compute "soft counts" based on expected values of latent variables

+ M-step: re-estimate parameters, based on the "soft counts"

## EM in the IBM models
see lecture ppt page 63-65

1. E-step compute “soft counts” c(f → e) and c(e) based on posterior word alignment probabilities
2. M-step re-estimate t(f |e), based on the “soft counts”


### word alignment probabilities
+ random initial the t(f|e) 
+ update P(a_n), a is word in target sentence, n is the position of in source stenctenc. 
```math
  P(a_1=1|...) = \frac{t(f|e)}{\sum t(f|e_j)}
```
+ update $c(e_j,f)$ = $c(e_j,f)$ + P(a_f = e_j|)  

+ update t
```math
  t(f|e) = \frac{c(f,e)}{c(e)}
```

Q: what does word-based mean?