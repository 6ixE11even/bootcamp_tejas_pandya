# Project Title

Predicting next day close price of (AMZN) Amazon.Inc

## Problem Statement

Global.Inc is a global asset management firm. Dave is one of the best portfolio manager of the firm. One of his HNI client has specifically asked him to only trade in Amazon.Inc (only intraday).

Dave wants to create a price model which predicts next day close price of the stock which will enable him to ensure better profits for his client.

## Stakeholders and Users

- **Who decides?** Global.Inc
- **Who uses the output?** Dave
- **Timings** Daily (to predict next day close price)

## Useful Answers and Decision

- **Type:** Predictive - as we need to forecast price of the stock
- **Deliverable:** Python generated price model

## Folder Structure

- **data/** → All homework contributions will be submitted here.
- **project/** → All project contributions will be submitted here.
- **class_materials/** → Local storage for class materials. Never pushed to
GitHub.

## Homework Folder Rules

- Each homework will be in its own subfolder (`homework0`, `homework1`, etc.)
- Include all required files for grading.

## Project Folder Rules

- Keep project files organized and clearly named.

## Data Storage (Homework 5)

- **Folder Structure:**
  - data/raw
  - data/processed
- **Formats used and why?**
  - CSV:
        1. human-readable
        2. file size is large compared to Parquet
        3. use-case: basic and better for small to medium data size
  - Parquet:
        1. faster loading and reading time
        2. file size is very small compared to CSV
        3. use-case: for storing large scale data

## env Variables (Homework 5)

- raw and processed data paths are stored in .env, making it more portable and secured
- api_keys are also stored in the .env file
- .env.example file is stored in the repo for easy replication of .env file

## Data Cleaning (Homework 6)

### 1. Handling Missing Data

We fill missing numbers with the median when data are missing randomly. For time series, we fill missing values by using nearby points. If missing data isn’t critical, we may drop those rows. Any filling method changes the data’s averages and patterns.

### 2. Types of Missing Data

Missing values can be random (MCAR: safe to fill or drop), related to other data (MAR: can fill using related info), or dependent on unseen factors (MNAR: needs expert insight). Mistakes in understanding these can skew results.

### 3. Cleaning the Data

We remove impossible or out-of-range values assuming they’re errors. If a column or row has too much missing data, we drop it, assuming it’s not important. But this leads to removing some rare cases where the data is valid.

### 4. Scaling Data

StandardScaler assume data follow a normal pattern, MinMaxScaler expect minimum and maximum values to be typical.

### 5. Making It Reproducible

Cleaning.py is designed assuming the future datasets will adhere to similar dataframe structure.
