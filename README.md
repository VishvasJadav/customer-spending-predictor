# Customer Spending Predictor ML App
## Streamlit app
```
https://customer-spending-predictor-x.streamlit.app/
```

## Overview

The **Customer Spending Predictor** is a Machine Learning application designed to predict how much a customer is likely to spend based on historical customer data and relevant features. The application helps businesses understand customer spending behavior, identify high-value customers, and make data-driven marketing and business decisions.

## Features

- **Customer Spending Prediction:** Predict the expected spending amount of a customer using a trained ML model.
- **Data Preprocessing:** Handle missing values, encode categorical variables, and prepare data for model training.
- **Machine Learning Model:** Train and evaluate predictive models using historical customer data.
- **Interactive User Interface:** Enter customer details and view predicted spending.
- **Model Evaluation:** Measure model performance using appropriate regression metrics.


## Technologies Used

- **Programming Language:** Python
- **Data Analysis:** Pandas, NumPy
- **Data Visualization:** Matplotlib, Seaborn
- **Machine Learning:** Scikit-learn
- **Web Framework:** Streamlit
- **Development Environment:** Jupyter Notebook / VS Code

## Project Structure

```
customer-spending-predictor/
├── assest
│   └──images.png
|
├── Datasets/
│   └── customer_spendings.csv
│   └── cleaned_data.csv
|
├── best_model/
│   └── best_model_pipeline.pkl
│
├── notebooks/
│   └── EDA.ipynb
│
├── app.py
├── requirements.txt
├── README.md

```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/customer-spending-predictor.git
cd customer-spending-predictor
```

### 2. Create a Virtual Environment (Optional)

```bash
python -m venv myenv
```

Activate the environment:

**Windows**
```bash
myenv\Scripts\activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### Run the Application

Application is built with Streamlit, run:

```
streamlit run app.py
```

# About Dataset
```
Use a suitable customer dataset containing the columns below. If a dataset has not been provided, create or obtain a CSV file with realistic sample records. The target column must be Amount_Spent.
    Column	            Type	            Description
    Age	                    Numerical	        Customer age
    Annual_Income	    Numerical	        Customer annual income
    Website_Visits	    Numerical	        Number of website visits per month
    Previous_Purchases	    Numerical	        Number of previous purchases
    Membership_Type	    Categorical	        Bronze, Silver, or Gold
    Preferred_Category	    Categorical	        Electronics, Fashion, Home, or Beauty
    City_Tier	            Categorical	        Tier 1, Tier 2, or Tier 3
    Discount_Used	    Categorical	        Yes or No
    Amount_Spent	    Numerical(target)	Customer spending amount to predic
```

## Author

- GitHub: [Vishvas Jadav](https://github.com/VishvasJadav)

---

