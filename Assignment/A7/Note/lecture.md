
# QA:
## what is a diagnouse system?

## What is the difficult in developing such a system? and how to solve it?
+ in spoken dialogue it can be difficult to know when a turn ends.

## How does it work?
+ early systems rule-based
+ Modern systems use a combination of rules and ML-based techniques. 

## Speech acts
<!-- 对话行为分类？ -->
+ constatives
<!-- 命令，计划，陈述 -->
+ directive

+ commissives
  <!-- 承诺 -->

+ Acknowledgments
<!-- express  -->

# Chatbot
## keyword-based 
+ ELIZA
  + Keyword based, higher rank for specific keywords, prefes response based on most specific keyword
  
+ PARRY
  + includes model of mental state that influences the conversation.

+ ALICE
  +  upgradedversion of ELIZA with ALML (AL markup language)

## Corpus-based chatbost
<!-- 语料 -->
+ Based on very large datasets of real converstations
+ response generation: not rules but signle response based on user's last turn or two

+ AIAOice

## IR-based chabots
+ return response to most similar user turn
+ return most similar response
+ based on word vector or word embedding

## ML-based encoder-decoder chatbot

# task-based dialogue systems for digital assistants

+ step-1 (NLU): extract meaning : rule-based or increasingly ML based
+ step-2 (DM): commercial dialogue: are mostly rule-based
+ step-3 (NLG): generate answer: are mostly template-based

## Natural language understanding (NLU)
+ classify domain
+ determin intent
+ extract relevant information

## dialogue management (DM)
+ why dialogue management?
  + otherwise the user must give all information in one statment (no dialogue)

### finite-state based DM
+ system-initiative 
+ no flexibility
+ works in simple cases
  + 像一个设计好的流程

### frame-based (form-based)
+ all common task-based systems use frames!
  + 本质上就是 一个个 特定情境

### frame-based with dialog state
+ keeps different aspects separate 
+ there can be multiple frames that the system moves between

### dialogue policy 
+ In priciple: based on entire previous diaglogue
+ simpler: current state of frame and last turns


