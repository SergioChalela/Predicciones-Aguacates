# Car Price Prediction

This project aims to predict car prices based on various features such as mileage, year, make, and model. We used data preprocessing, feature engineering, and applied machine learning models to achieve a robust prediction model.

## Table of Contents

- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Data Preprocessing](#data-preprocessing)
- [Feature Engineering](#feature-engineering)
- [Modeling](#modeling)
- [Results](#results)
- [Next Steps](#next-steps)

## Project Overview

The goal of this project is to build a predictive model that can estimate the price of a car based on its characteristics. Using machine learning techniques, we improved the model’s performance to explain a significant portion of the variability in car prices.

## Dataset

The dataset contains various features about cars, including:
- **Price**: Target variable, indicating the car price.
- **Mileage**: The distance the car has been driven.
- **Year**: The manufacturing year of the car.
- **Make**: The brand of the car.
- **Model**: The model of the car.

## Data Preprocessing

1. **Dropped Irrelevant Columns**: We removed columns like `City`, `State`, and `Vin`, as they do not significantly impact car price.
2. **Encoding Categorical Variables**: Used `LabelEncoder` to transform `Make` and `Model` into numerical values.
3. **Scaling Features**: Applied `MinMaxScaler` to scale `Mileage` between 0 and 1.

## Feature Engineering

1. **Log Transformation of Price**: To reduce skewness, we applied a log transformation to the `Price` variable, creating a new column `Log_Price` to be used as the target variable.
2. **Vehicle Age**: Calculated the age of each car by subtracting the year of manufacture from the current year (2024).
3. **Standardization**: Standardized `Mileage` and `Vehicle_Age` for improved model performance.

## Modeling

We tested two main models:
1. **Linear Regression**: Provided a baseline but had limited performance (R² Score ≈ 0.42).
2. **Random Forest Regressor**: Achieved significant improvements, with an R² Score of approximately 0.898, capturing about 90% of the variability in car prices.

### Model Performance

- **Linear Regression**:
  - MSE: 0.181
  - R² Score: 0.417

- **Random Forest Regressor**:
  - MSE: 0.0315
  - R² Score: 0.898

## Results

The Random Forest model performed much better than linear regression, indicating complex, non-linear relationships in the data. The final model explains a large portion of the variance in car prices, making it suitable for practical applications.

## Next Steps

1. **Hyperparameter Tuning**: Use techniques like Grid Search or Random Search to optimize the Random Forest model further.
2. **Feature Importance Analysis**: Identify which features contribute most to the model's performance.
3. **Cross-Validation**: Implement cross-validation to ensure model robustness.

---

Feel free to explore the code and run the models. If you have any questions or suggestions, please reach out!






