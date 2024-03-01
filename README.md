# Obesity Level Estimation

## Overview

This machine learning project aims to estimate the obesity level of an individual based on various features and metrics. Obesity is a significant health concern globally, and predicting an individual's obesity level can assist in early intervention and personalized health recommendations.

## Table of Contents

- [Introduction](#introduction)
- [Dataset](#dataset)
- [Features](#features)
- [Data Preprocessing](#data-preprocessing)
- [Training](#training)
- [Evaluation](#evaluation)
- [Usage](#usage)
- [Contributing](#contributing)

## Introduction

Obesity is a complex health issue influenced by multiple factors such as diet, physical activity, genetics, and lifestyle. This project utilizes machine learning techniques to develop a model that estimates the obesity level of an individual based on relevant features.

## Dataset

The dataset used in this project contains a diverse set of individuals with associated features such as age, gender, BMI, and various health metrics. The data has been preprocessed to handle missing values and ensure uniformity.

## Features

The features used for obesity level estimation include:



- **Gender**
- **Age**
- **Height**
- **Weight**
- **Family History with Overweight**
- **Frequency of Consumption of Vegetables (FCVC)**
- **Frequency of Consumption of Fruits (FAVC)**
- **Number of Main Meals (NCP)**
- **Consumption of Food between Meals (CAEC)**
- **Smoking Status (SMOKE)**
- **Daily Water Consumption (CH2O)**
- **Calories Consumed from Saturated Fat and Cholesterol (SCC)**
- **Physical Activity Frequency (FAF)**
- **Time Using Technology Devices (TUE)**
- **Calories Consumed from Alcohol (CALC)**
- **Mode of Transportation (MTRANS)**



These features provide a comprehensive representation of an individual's health and lifestyle.

## Data Preprocessing

The dataset undergoes preprocessing to handle missing values, normalize numerical features, and encode categorical variables. Exploratory Data Analysis (EDA) is performed to gain insights into the data distribution and relationships.



## Training

The model is trained on a labeled dataset using an appropriate loss function and optimization algorithm. The training process involves iterating over the dataset multiple times to minimize the prediction error.

## Evaluation

The model's performance is evaluated using metrics such as Mean Accuracy, Precision, and others. Cross-validation techniques may be employed to ensure robustness and prevent overfitting.

## Usage

To use the trained model for obesity level estimation, follow these steps:

1. Install the required dependencies listed in the `requirements.txt` file.
2. Load the pre-trained model using the provided script.
3. Input the relevant features for the individual in question.
4. Obtain the predicted obesity level.

## Contributing

Contributions to the project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
