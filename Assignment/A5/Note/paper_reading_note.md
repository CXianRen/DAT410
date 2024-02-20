# A history of machine translation from the Cold War to deep learning
[paper is here](https://www.freecodecamp.org/news/a-history-of-machine-translation-from-the-cold-war-to-deep-learning-f1d335ce8b5/)

# In the beginning 
+ 1933 Soviet Troyanskii
+ 1954 IBM 701 
<!-- 
(受限制于时代的局限性, 当时的方法在现在看起来都很幼稚，和不可靠，但是为什么还会有 这种行为? 因为 1.人类奇怪的求知欲望，创新欲望 2. 军备竞赛) -->

# The race for machine translation 
+ 1966， one report from US ALPAC called machine translation expensive, inaccurate, and upromising -> then focusing on dictionary development. 
<!-- (看清时代的受限制，暂时的脱离并没有 让US 错过这个机会，但是如何能看清是个问题) -->

# Ruled-based machine translation (RBMT) 1950-1980

Scientisits peered over the interpreters' work and then try to compel the computers to repeat those actions. These systems consisted of:
+ Bilinguial dictionary (RU-EN)
+ A set of linguistic rules for each language

example:
+ PROMPT and Systran

## Direct Machine Translation
It divides the text into words, translates them, and then corrects them. 
<!-- 本质上都是在模仿人的思考过程。 基于词法, 最基本的思想-->

## Transfer-based Machine Translation
It first determine the grammatical structure of the sentence, then manipulate whole constructions, not words. 
<!-- 既然单个词法效果不好，那么就加上组合 和 语法结构的 -->

## Interlingual Machine Translation
In this method, the source text is transformed to the intermediate representation, (is unified for all the world's languanges (interlingua)).  Then interlingua would convert to any target language. 

It is hard to create sunch universal interlingua. 
<!-- 进一步尝试模仿人对世界的认知过程。 将所有概念统一抽象化（人脑的理解）-> 输出 到 不同的语言 -->

## END
RBMT is for specific casese like weather report tanslation, and so on. 

why rules are not work for all cases. 
Because the irregualr verbs and other exceptions. 

homonyms: same word can have a different meaning in a different context.

# Example-based Machine Translation (EBMT)
using ready-made phrases instead of repeated translation.

+ figure out the difference between the two sentences, translate the missing word, and the nnot screw it up.

EBMT showed the light of day to scientists from all over the world: it turns out, you can just feed the machine with existing translations and not spend years forming rules and exceptions. 
<!-- 启发性的思考于 革命可能还差一步之遥 -->
# Statistical Machine Translation (SMT)
using statistic and probability
(see more in the lecture_note.md)

## Word-based SMT
IBM:
+ Model 1: didn't take the position into account 
+ Model 2: take the position into account 
+ Model 3: two more step to add new words that is not on the source sentence.
+ Model 4: took into accounte the so-called "relative order" - the model learned if two words always switched places.
+ Model 5: bugfixes

Faile: Every single word was translated in a single-true way, according to the machine.

## Phrase-based SMT
it split the text not only into words but also phrases. 

For the word-based translation, the exact match of the sources was critical, which excluded any literary or free translation. The phrase-based translation had no problem learning from them. To improve the translation, researchers even started to parse the news websites in different languages for that purpose.
<!-- Phrase based SMT 运行的时间远比想象的久，到2016年 -->

## Syntax-based SMT

# Neural Machine Translation (NMT)
the idea was close to transferring the style between photos.
something like the interlingua, but using model to replace it!!!

+ RNN (recurrent neural networks)
  + reular one 
  + bi-directional
  + attention 

<!-- 模型的进化 都是以 如何更高效率 去利用信息 为方向的 -->

## Google Translate （since 2016）
consists of 8 encoder and 9 decoder layers of RNNs, as well as attention connections from the decoder network.

## Yandex Translate (since 2017)
Yandex combines neural and statistical approaches to translate the sentence, and then it choose the best one with its favorite CatBoost algorithm.

 neural translation often fails when translating short phrases, since it uses context to choose the right word. It would be hard if the word appeared very few times in a training data. In such cases, a simple statistical translation finds the right word quickly and simply.


Q:
(a) As you can see, automatic translation has been one of the "holy grails" of AI research for several decades, and attempts at solutions have been proposed using many diverse approaches, based on radically different computational techniques. Can you think of other AI problems where we can see a similarly wide range of approaches?

<!--  -->



(b) Can you think of similarities between some rule-based translation systems and the state-of-the-art neural systems?




(c) Can you think of situations where it could be preferable to use an "old-school" rule-based solution instead of a modern (neural or statistical)?

Google Translate used for website translation in the browser still uses the old phrase-based algorithm.
Google will always translate this phrase that way and mark it with a special badge. This works fantastically for short everyday phrases such as, “Let’s go to the cinema,” or, “I’m waiting for you.”