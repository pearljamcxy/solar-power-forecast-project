# Solar Power Forecast Project

This repository presents a solar power generation forecasting project built with Python.
The objective of this project is to predict solar power output using historical environmental and meteorological data through time-series analysis and machine learning methods.

Accurate solar power forecasting plays an important role in renewable energy systems. It helps mitigate the inherent variability of solar generation and supports grid scheduling and energy management decisions.

## Project Overview

Solar power generation is influenced by multiple external factors, including solar irradiance, weather conditions, and atmospheric variables. As a result, the data exhibits strong variability and seasonal patterns.
By constructing predictive models, future power generation can be estimated at different time horizons, contributing to improved planning and operational efficiency in energy systems.

This project covers a complete workflow from exploratory data analysis and feature engineering to model training and evaluation. It also includes an optional API example for simple model deployment.

## Project Structure

The repository is organized to reflect the end-to-end forecasting pipeline:

notebooks/
Contains multiple Jupyter Notebooks documenting the full analysis and modeling process, including:

- Exploratory data analysis (EDA) of raw solar power data

- Data cleaning and preprocessing

- Feature engineering and feature selection

- Training and evaluation of forecasting models

## Analysis and Modeling Workflow

The project follows the steps below:

1. **Data Loading and Preparation**
Load historical solar power generation data along with relevant environmental and meteorological features.

2. **Exploratory Data Analysis (EDA)**
Analyze data distributions, missing values, seasonal patterns, and correlations among features.

3. **Feature Engineering**
Construct time-based features and core physical features to help models capture temporal and domain-specific patterns.

4. **Model Training and Selection**
Train multiple forecasting models using the processed dataset, including:

- Baseline models (e.g., Linear Regression)

- Machine learning models (e.g., XGBoost)
Model performance is evaluated using metrics such as MAE, RMSE, and R².

5. **Model Evaluation and Comparison**
Compare model performance across different forecast horizons to analyze strengths and limitations.

## Key Findings

- The project demonstrates performance differences among various models for solar power forecasting tasks.

- Proper data preprocessing and feature engineering significantly improve prediction accuracy compared to simple baseline models.

- Models capable of capturing nonlinear relationships show more stable performance in short-term and medium-term forecasts.