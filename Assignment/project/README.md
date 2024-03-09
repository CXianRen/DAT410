# this folder is for the final project, a disease chatbot.

# motivation:
<!-- + 在医疗人员缺乏的地方，用户可以先行诊断，再根据诊断 进行分流，减少医疗接待区的服务压力和效率。 -->
+ In the region with limited medical resources,, users can conduct preliminary diagnositcs themselves before undergoing further diagnostic procedures with a doctor. This can help alleviate the strain on medicla services and improve efficiency in the healthcare reception desk. 


<!-- + 对线上医疗的一个扩展，再等待线上医生诊断的时候，可以由系统先进行对话，获得基本诊断情况，在分配到医生后，加速医生对病人情况的了解程度，并且给出 潜在的方向 -->
+ It's also an extension of online helthcare. While awaiting consultation with an online doctor or specialist, users can engage with a guiding chatbot obtain basic diagnostic information. This information will expedite the diagnostic process by providing potential diseases or conditions to the doctor, thus enhancing their understanding of the patient's situation.

<!-- + 有些人很懒，那怕能去看，也不愿意去看， 可以用来提醒预警他们 -->

+Some individuals are lazy or stubborn, and they may avoid going to the hospital even when they feel unwell. This system can assist them by providing alerts and reminders.

# Chatbot：
<!-- + 不需要很复杂，医院和医生其实有一个特定的问诊模式，用中国的一句话讲就是 问闻望切， 就是 通过一系列询问获取用户身体基本情况，再根据这个情况做基本判断，进一步详细检查 或者 做出结论。  -->

+ the chatbot designe doesn't need to be very complex, as doctors and the hosplitals follow a specific diagnostic pattern. In Chinese, it's referred to as "ask, smell, observe, and touch". This process involves obtaining basic physical information from users. With this information, doctors will decide whehter further biological checks are necessary or just give out the conclusions. 

<!-- + 根据这个情况 最后 给出 就医指导， 比如 附件有哪些医院，在什么时候开门，哪些医生推荐，是否预约。等 -->

+ And based on this information, the chatbot can also provide medical guidance to suers, such as information about available hispital, their operating hours, recommended doctors and assistance with making appointments. 


# scalable system：
<!-- + 基于多模型的预测系统，一个疾病或者多个疾病 一个模型，根据模型的数量可以动态扩展该系统的复杂性 -->

## scalable diagnostic models (back-end)
+ This systme is highly scalabe. One or more diseases can be predicted by a model, so, the system complexity entirely depeneds on the number of models and their complexity.

## scablable chatbot (front-end)



# dataset used in this project:




| Disease           | Dataset                                                                                  | Samples | Dimensions | Missing Values |
|-------------------|------------------------------------------------------------------------------------------|---------|------------|-----------|
| Breast Cancer     | [Breast Cancer Wisconsin (Diagnostic) Data Set](https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data)   |   569   |    33      |     No     |
| Kidney Disease    | [Chronic Kidney Disease dataset](https://archive.ics.uci.edu/dataset/336/chronic+kidney+disease)      |   400   |    26      |     Yes     |
| Diabetes          | [Pima Indians Diabetes Database](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)   |   768   |    9       |     Yes     |
| Liver Disease     | [Indian Liver Patient Records](https://www.kaggle.com/datasets/uciml/indian-liver-patient-records) |   583   |    11      |     Yes     |
| Heart Disease_1  | [Framingham Heart Study Dataset](https://www.kaggle.com/datasets/aasheesh200/framingham-heart-study-dataset) |   4240  |    16      |     x    |
| Heart Disease_2  | [UCI Heart Disease Data](https://www.kaggle.com/datasets/redwankarimsony/heart-disease-data)        |   920   |    16      |     x     |


## Breast Cancer
| Variable Name           | Description                                                             |
|-------------------------|-------------------------------------------------------------------------|
| id                      | ID number                                                               |
| diagnosis               | The diagnosis of breast tissues (M = malignant, B = benign)             |
| radius_mean             | Mean of distances from center to points on the perimeter                |
| texture_mean            | Standard deviation of gray-scale values                                |
| perimeter_mean          | Mean size of the core tumor                                            |
| area_mean               | Area of the cell                                                        |
| smoothness_mean         | Mean of local variation in radius lengths                               |
| compactness_mean        | Mean of perimeter^2 / area - 1.0                                        |
| concavity_mean          | Mean of severity of concave portions of the contour                     |
| concave points_mean     | Mean for number of concave portions of the contour                      |
| symmetry_mean           | -                                                                       |
| fractal_dimension_mean  | Mean for "coastline approximation" - 1                                  |
| radius_se               | Standard error for the mean of distances from center to points on the perimeter |
| texture_se              | Standard error for standard deviation of gray-scale values              |
| perimeter_se            | -                                                                       |
| area_se                 | -                                                                       |
| smoothness_se           | Standard error for local variation in radius lengths                    |
| compactness_se          | Standard error for perimeter^2 / area - 1.0                             |
| concavity_se            | Standard error for severity of concave portions of the contour          |
| concave points_se       | Standard error for number of concave portions of the contour            |
| symmetry_se             | -                                                                       |
| fractal_dimension_se    | Standard error for "coastline approximation" - 1                        |
| radius_worst            | "Worst" or largest mean value for mean of distances from center to points on the perimeter |
| texture_worst           | "Worst" or largest mean value for standard deviation of gray-scale values |
| perimeter_worst         | -                                                                       |
| area_worst              | -                                                                       |
| smoothness_worst        | "Worst" or largest mean value for local variation in radius lengths     |
| compactness_worst       | "Worst" or largest mean value for perimeter^2 / area - 1.0              |
| concavity_worst         | "Worst" or largest mean value for severity of concave portions of the contour |
| concave points_worst    | "Worst" or largest mean value for number of concave portions of the contour |
| symmetry_worst          | -                                                                       |
| fractal_dimension_worst | "Worst" or largest mean value for "coastline approximation" - 1         |

## Kidney Disease
| Variable Name | Role     | Type        | Demographic   | Description           | Units  | Missing Values |
|---------------|----------|-------------|---------------|-----------------------|--------|----------------|
| age           | Feature  | Integer     | Age           |                       | year   | yes            |
| bp            | Feature  | Integer     |               | blood pressure        | mm/Hg  | yes            |
| sg            | Feature  | Categorical |               | specific gravity      |        | yes            |
| al            | Feature  | Categorical |               | albumin               |        | yes            |
| su            | Feature  | Categorical |               | sugar                 |        | yes            |
| rbc           | Feature  | Binary      |               | red blood cells       |        | yes            |
| pc            | Feature  | Binary      |               | pus cell              |        | yes            |
| pcc           | Feature  | Binary      |               | pus cell clumps       |        | yes            |
| ba            | Feature  | Binary      |               | bacteria              |        | yes            |
| bgr           | Feature  | Integer     |               | blood glucose random  | mgs/dl | yes            |

## Diabetes
| Variable                   | Description                                            |
|----------------------------|--------------------------------------------------------|
| Pregnancies                | Number of times pregnant                               |
| Glucose                    | Plasma glucose concentration a 2 hours in an oral glucose tolerance test |
| BloodPressure              | Diastolic blood pressure (mm Hg)                       |
| SkinThickness              | Triceps skin fold thickness (mm)                       |
| Insulin                    | 2-Hour serum insulin (mu U/ml)                         |
| BMI                        | Body mass index (weight in kg/(height in m)^2)         |
| DiabetesPedigreeFunction   | Diabetes pedigree function                             |
| Age                        | Age (years)                                            |
| Outcome                    | Class variable (0 or 1), where 268 of 768 are 1, the others are 0 |


## Liver Disease
| Variable                     | Description                              |
|------------------------------|------------------------------------------|
| Age                          | Age of the patients                      |
| Gender                       | Sex of the patients                      |
| Total_Bilirubin              | Total Billirubin in mg/dL               |
| Direct_Bilirubin             | Conjugated Billirubin in mg/dL          |
| Alkaline_Phosphotase         | ALP in IU/L                              |
| Alamine_Aminotransferase     | ALT in IU/L                              |
| Aspartate_Aminotransferase   | AST in IU/L                              |
| Total_Protiens               | Total Proteins g/dL                     |
| Albumin                      | Albumin in g/dL                         |
| Albumin_and_Globulin_Ratio   | A/G ratio                                |


## Heart Disease 1

| Variable         | Description         |
|------------------|---------------------|
| male             | Gender (Male)       |
| age              | Age of the patient  |
| education        | Education level     |
| currentSmoker    | Current smoker      |
| cigsPerDay       | Number of cigarettes per day |
| BPMeds           | Blood pressure medications |
| prevalentStroke  | Prevalent stroke    |
| prevalentHyp     | Prevalent hypertension |
| diabetes         | Diabetes            |
| totChol          | Total cholesterol   |


## Heart Disease 2

| Variable  | Description                            |
|-----------|----------------------------------------|
| id        | Unique ID                              |
| age       | Age in years                           |
| sex       | Gender                                 |
| dataset   | Location of data collection            |
| cp        | Chest pain type                        |
| trestbps  | Resting blood pressure                 |
| chol      | Cholesterol measure                    |
| fbs       | Fasting blood sugar                   |
| restecg   | ECG observation at resting condition   |
| thalch    | Maximum heart rate achieved           |
