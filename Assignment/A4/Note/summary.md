# Machine learning techniques to diagnose breast cancer from image-processed nuclear features of fine needle aspirates 


+ what is "fine needle aspirates" ?
  + Fine needle aspiration (FNA) is a medical procedure used to collect cells from a lump or mass in the body for examination under a microscope.


## Abstract
  + data from 569 patients, 54 test data 
  + accuracy: 97%
  + 100% accuracyt on 54 test data

## Introduction
+ problem is: there is subjectivity of visual diagnosis.
+ what to do: the subjectivity can be minimized with computer-based digital image analysis and machine learning techniques.

## Patients and methods
about the patients and the FNA

## Nuclear feature characterzation
+ Image preparation: 
  + descript how to get the images and what had been done to the images.

+ The digital assessment process
  + specify the exact location of each cell nucleus.
  + UI allows user to select the approximate location of sufficient nucleus. 

+ Snakes
  + a method to figure out hte boundary.

+ Nuclear features
  + ten nuclear features were calculated for each cell.
    + these features were modeled such taht higher values are typically associated with malignancy.
    + the mean value, worst values, and standard error of each feature were computed . (resulting in a toatal of 30 features for each case.)
      + radius
      + perimeter
      + area
      + compactness
      + smoothness
      + concavity
      + concave points
      + symmetry
      + Fractal dimension
      + Texture

## Phantoms
generated images for assessments 


+ Classification  procedure
  + a variant on the multisurface method (MSM), MSM-Tree
    + uses linear programming iteratively to place a series of spearating planes in the feature space of the examples. 
  + minimize not onlyu the number of separating planes but also the number of features used.
    + as a rule, simpler classifiers perform better than more complex ones on new data.
    + the best single-plane classifiere separated benign from malignant points based on 3 nuclear feature: mean texture, the worst area, and the worst smoothness. 

  + estimate of predictive accuracy using tenfold cross-validation

## Results
(similar to that in abstrct)

## Discussion
other people using fewer feature get lower accuracy. 


summary:
- The study focuses on utilizing machine learning techniques for breast cancer diagnosis using image-processed nuclear features of fine needle aspirates (FNA).
- FNA is a medical procedure for cell collection from body masses or lumps.
- The research involves 569 patients, with 54 test data points, achieving an impressive 97% accuracy, with 100% accuracy on the test data.
- The introduction highlights the subjectivity in visual diagnosis and suggests minimizing it with computer-based digital image analysis and machine learning.
- Nuclear feature characterization involves image preparation, digital assessment processes, snake methods for boundary delineation, and calculation of ten nuclear features for each cell.
- The classification procedure, MSM-Tree, minimizes the number of separating planes and features used for better performance.
- Results underscore the superiority of using more features for higher accuracy.
- Overall, this approach presents promising advancements in breast cancer diagnosis, offering more objective and accurate assessments.


# The Mythos of Model Interpretablity

## Abstract
+ model should be not only good but also interpretable.
+ This article seeks to refine the discourse on 
interpretability.
+ examines the obejctive s of previous papers -> be diverse and discordant. 
+ explores model properties and tehniques thought to confer interpretability, identifying tansparency 

## INTRODUCTION
- Rapid progress in machine learning has led to the deployment of automatic decision processes.
- Most machine learning-based decisions operate by taking some input and predicting the corresponding output.
- Machine learning models do not understand why a given input should receive a certain label, only that certain inputs are correlated with that label.
- As machine learning penetrates critical areas like medicine, criminal justice, and finance, the inability of humans to understand these models seems problematic.
- Some suggest model interpretability as a remedy.
- In academic literature, few authors precisely articulate the meaning of interpretability or how their proposed solutions are precisely useful.
- The definition of interpretability is unclear, leading to claims regarding the interpretability of various models exhibiting a quasi-scientific nature.
- Objectives and methods proposed in the literature are diverse, indicating interpretability is not a unified concept but several distinct ideas that must be clarified before progress can be made.
`
## DESIDERATA OF INTERPRETABILITY RESEARCH 
when and why we want a interpretation. 

### Trust
The core of this paragraph is the exploration of the relationship between trust and interpretability. The authors suggest that trust can stem from confidence in the model's performance or from subjective perceptions of how well the model is understood. They also highlight that in real-world scenarios, trust may be linked to the model's ability to achieve actual objectives.

### Causality
The paragraph discusses the application of supervised learning models in inferring properties of the natural world, emphasizing their potential to generate hypotheses for scientific investigation. However, it cautions that associations learned by these models do not necessarily reflect causal relationships due to potential unobserved causes and the limitations of causal inference methods.

### Transferability
The core of this passage is about the application and limitations of supervised learning models in various environments. It discusses how these models, while performing well on training and test data, may encounter challenges when faced with non-stationary environments or actively adversarial manipulation. Examples are provided, such as errors in predicting patient mortality and susceptibility of models to adversarial attacks. Additionally, the passage highlights the issue of credit rating models being manipulated, leading to potential loss of predictive power.

### Informativeness
The core of this passage is to delineate two common paradigms in the real-world application of supervised learning models. Firstly, decision theory is sometimes applied directly to the outputs of these models to drive actions. Alternatively, these models are utilized to provide information to human decision-makers. While the primary objective of machine learning is often error reduction, the ultimate aim in real-world scenarios is to furnish useful information. Although models typically convey information through their outputs, in certain cases, interpreting these outputs can offer additional insights to human decision-makers.

### Fair and ethical decision making
The core concern is the ethical implications of algorithmic decisions, notably in using recidivism predictions to make fair decisions about releasing or detaining individuals.

## THE TRANSPARENCY NOTION OF INTERPRETABILITY 
- Techniques and model properties for interpretability fall into two categories: transparency (understanding how the model works) and post hoc explanations (additional insights from the model).
- Transparency, opposite of opacity or "black-boxness," entails understanding the model mechanism at different levels: entire model (simulatability), individual components (decomposability), and training algorithm (algorithmic transparency).
- Simulatability implies the ability to comprehend the entire model at once, suggesting interpretable models are simple; for instance, linear models are considered more interpretable than complex neural networks.
- Decomposability requires intuitive explanations for each part of the model, such as decision tree nodes correlating with plain text descriptions or linear model parameters indicating feature-label associations.
- Algorithmic transparency concerns understanding the learning algorithm itself; while linear models offer insights into error surfaces and convergence, modern deep learning lacks such transparency.


### Post hoc interpretability  
- Post hoc interpretations offer a distinct approach to extracting information from learned models, providing useful insights despite not fully revealing the model's workings.
- Common post hoc interpretation methods include natural language explanations, visualizations of learned representations, and explanations by example.
- Transparency, or the understanding of how a model works, is a key aspect of post hoc interpretations, encompassing simulatability, decomposability, and algorithmic transparency.
- Simulatability refers to the ability to comprehend the entire model at once, often achieved through simplicity and clarity in model structure and calculations.
- Decomposability involves intuitive explanations for each part of the model, such as plain text descriptions for decision tree nodes or parameter interpretations in linear models.
- Algorithmic transparency concerns understanding the learning algorithm itself, ensuring confidence in its behavior and performance, which is particularly relevant for complex models like deep neural networks.
- These post hoc interpretability techniques enable practitioners to gain insights into model behavior and decision-making processes, enhancing trust and usability in machine learning applications.

## Discussion
The concept of interpretability is both important and complex. Here are several key points from the analysis:

- Linear models are not necessarily more interpretable than deep neural networks; interpretability depends on the chosen concept.
- When choosing between linear and deep models, there's often a trade-off between algorithmic transparency and decomposability.
- Deep neural networks may have an advantage in post hoc interpretation, as they learn rich representations.
- Claims about interpretability must be qualified with specific definitions and evidence.
- Transparency may sometimes conflict with broader AI objectives, potentially hindering progress.
- Post hoc interpretations can be misleading if optimized to meet subjective demands, risking bias and misleading explanations.


summary:
1. **Importance of Interpretability**: Understanding why machine learning models make certain decisions is crucial, especially in critical fields like medicine and finance.

2. **Definition Clarity**: The meaning of interpretability lacks clear definition in academic literature, hindering progress in the field.

3. **Desiderata of Interpretability Research**:
   - Trust: Confidence in model performance and understanding contributes to trust.
   - Causality: Models can infer hypotheses for scientific investigation but may not reflect causal relationships.
   - Transferability: Models may face challenges in non-stationary environments or adversarial manipulation.
   - Informativeness: Models aim to provide useful information to human decision-makers.
   - Fair and Ethical Decision Making: Ethical implications of algorithmic decisions require consideration, especially in domains like criminal justice.

4. **Transparency and Post Hoc Interpretability**:
   - Transparency: Understanding the model mechanism at different levels, including simulatability, decomposability, and algorithmic transparency.
   - Post Hoc Interpretability: Extracting insights from learned models through methods like natural language explanations and visualizations.

5. **Complexity and Trade-offs**:
   - Linear vs. Deep Models: Interpretability depends on the chosen concept, with trade-offs between algorithmic transparency and decomposability.
   - Need for Specific Definitions and Evidence: Claims about interpretability must be supported with precise definitions and evidence.

6. **Challenges and Caution**:
   - Misleading Interpretations: Post hoc interpretations can be misleading if optimized to meet subjective demands, risking bias and misleading explanations.
   - Balancing Transparency with AI Objectives: Transparency may sometimes conflict with broader AI objectives, posing challenges for progress.

Overall, the article underscores the importance of addressing interpretability challenges in machine learning models through nuanced approaches and precise definitions.