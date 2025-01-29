# Kifiya-AIM-Week-6 

## Overview

This project aims to develop a Credit Scoring Model for Bati Bank, a leading financial service provider. The model will enable a buy-now-pay-later service in partnership with an eCommerce company. The project involves defining a proxy variable for categorizing users as high or low risk, selecting observable features that predict default, and developing models to assign risk probability, credit score, and optimal loan amount and duration.

## Business Need

Credit scoring is the process of assigning a quantitative measure to a potential borrower to estimate the likelihood of default. This project will help Bati Bank evaluate potential borrowers and provide credit scores based on their likelihood of defaulting.

## Data and Features

The dataset for this project is provided by the eCommerce platform and contains the following fields:

- `TransactionId`: Unique transaction identifier
- `BatchId`: Unique number assigned to a batch of transactions
- `AccountId`: Unique number identifying the customer
- `SubscriptionId`: Unique number identifying the customer subscription
- `CustomerId`: Unique identifier attached to Account
- `CurrencyCode`: Country currency
- `CountryCode`: Numerical geographical code of country
- `ProviderId`: Source provider of the item bought
- `ProductId`: Item name being bought
- `ProductCategory`: Broader product categories
- `ChannelId`: Identifies if customer used web, Android, IOS, pay later, or checkout
- `Amount`: Value of the transaction
- `Value`: Absolute value of the amount
- `TransactionStartTime`: Transaction start time
- `PricingStrategy`: Category of pricing structure for merchants
- `FraudResult`: Fraud status of transaction (1 - yes, 0 - no)

## Tasks

### Task 1 - Understanding Credit Risk

- Focus on understanding the concept of Credit Risk.
- Key references:
  - [Statistica Sinica](https://www3.stat.sinica.edu.tw/statistica/oldpdf/A28n535.pdf)
  - [HKMA](https://www.hkma.gov.hk/media/eng/doc/key-functions/financial-infrastructure/alternative_credit_scoring.pdf)
  - [World Bank](https://thedocs.worldbank.org/en/doc/935891585869698451-0130022020/original/CREDITSCORINGAPPROACHESGUIDELINESFINALWEB.pdf)
  - [Towards Data Science](https://towardsdatascience.com/how-to-develop-a-credit-risk-model-and-scorecard-91335fc01f03)
  - [Corporate Finance Institute](https://corporatefinanceinstitute.com/resources/commercial-lending/credit-risk/)
  - [Risk Officer](https://www.risk-officer.com/Credit_Risk.htm)

### Task 2 - Exploratory Data Analysis (EDA)

1. **Overview of the Data:**
   - Load the dataset and understand its structure.
   - Check the number of rows, columns, and data types.

2. **Summary Statistics:**
   - Calculate summary statistics for numerical and categorical features.

3. **Distribution of Numerical Features:**
   - Visualize the distribution of numerical features using histograms and KDE plots.

4. **Distribution of Categorical Features:**
   - Analyze the distribution of categorical features using bar plots.

5. **Correlation Analysis:**
   - Compute and visualize the correlation matrix for numerical features.

6. **Identifying Missing Values:**
   - Identify missing values and decide on appropriate imputation strategies.

7. **Outlier Detection:**
   - Use box plots to identify outliers in numerical features.

### Task 3 - Feature Engineering

1. **Create Aggregate Features:**
   - Total Transaction Amount: Sum of all transaction amounts for each customer.
   - Average Transaction Amount: Average transaction amount per customer.
   - Transaction Count: Number of transactions per customer.
   - Standard Deviation of Transaction Amounts: Variability of transaction amounts per customer.

2. **Extract Features:**
   - Transaction Hour: The hour of the day when the transaction occurred.
   - Transaction Day: The day of the month when the transaction occurred.
   - Transaction Month: The month when the transaction occurred.
   - Transaction Year: The year when the transaction occurred.

3. **Encode Categorical Variables:**
   - Convert categorical variables into numerical format using One-Hot Encoding and Label Encoding.

4. **Handle Missing Values:**
   - Use imputation or removal to handle missing values.

5. **Normalize/Standardize Numerical Features:**
   - Normalize or standardize numerical features to bring them onto a similar scale.

### Task 4 - Default Estimator and WoE Binning

1. **Construct a Default Estimator (Proxy):**
   - Visualize all transactions in the RFMS space and establish a boundary to classify users as high and low RFMS scores.
   - Assign all users the good and bad label.

2. **Perform Weight of Evidence (WoE) Binning:**
   - Use WoE binning to transform the features.

### Task 5 - Modelling

1. **Model Selection and Training:**
   - Split the data into training and testing sets.
   - Choose at least two models from Logistic Regression, Decision Trees, Random Forest, and Gradient Boosting Machines (GBM).
   - Train the models on the training data.

2. **Hyperparameter Tuning:**
   - Improve model performance using hyperparameter tuning techniques like Grid Search and Random Search.

3. **Model Evaluation:**
   - Assess model performance using metrics such as Accuracy, Precision, Recall, F1 Score, and ROC-AUC.

### Task 6 - Model Serving API Call

1. **Create a REST API:**
   - Choose a suitable framework for building REST APIs (e.g., FastAPI).
   - Load the trained machine-learning model.
   - Define API endpoints that accept input data and return predictions.
   - Implement logic to receive input data, preprocess it, and make predictions using the loaded model.
   - Format the predictions and return them as a response to the API call.

2. **Deployment:**
   - Deploy the API to a web server or cloud platform.

## How to Run the Project

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/teddyhabtamu/Kifiya-AIM-Week-6.git
   cd Kifiya-AIM-Week-6
