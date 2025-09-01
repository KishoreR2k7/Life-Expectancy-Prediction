## Live Demo :


## https://huggingface.co/spaces/KishoreR123/Life-Expectancy-Prediction


## App Photo :


<img width="1895" height="780" alt="image" src="https://github.com/user-attachments/assets/8686feb4-ca74-4a4e-8802-1c927f4a228d" />


# 🌍 Life Expectancy Predictor

This project predicts **life expectancy** using socio-economic and health-related factors.  
It leverages **Machine Learning (Random Forest Regressor)** trained on the **WHO Life Expectancy dataset** and provides an **interactive Gradio app** for predictions.

---

## 📂 Project Structure

.
├── Life Expectancy Data.csv # Raw dataset
├── Cleaned_Data.csv # Preprocessed dataset
├── model.pkl # Trained ML model
├── model_columns.pkl # Column names used for training
├── app.py # Gradio app for predictions
└── README.md # Project documentation

yaml
Copy code

---

## ⚙️ Installation

1. **Clone the repository**
```bash
git clone https://github.com/your-username/life-expectancy-predictor.git
cd life-expectancy-predictor
Create a virtual environment & activate it

bash
Copy code
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows
Install dependencies

bash
Copy code
pip install -r requirements.txt
📊 Dataset
The dataset contains 22 features related to health, economy, and education.

Key columns include:

Schooling

Income composition of resources

BMI

Alcohol

Adult Mortality

HIV/AIDS

thinness 1-19 years

Life expectancy (target variable)

After cleaning:

Original dataset: 2938 rows × 22 columns

Cleaned dataset: 1649 rows × 22 columns

🧹 Data Preprocessing
Removed missing values (dropna)

Removed duplicate rows

Checked constant / low-variance features

Encoded categorical columns (Country, Status) using One Hot Encoding

Saved cleaned dataset as Cleaned_Data.csv

🤖 Model Training
Two models were tested:

Linear Regression

R² Score: 0.63

Random Forest Regressor (n_estimators=300)

R² Score: 0.95 ✅ (chosen model)

The trained model and column names were saved as:

model.pkl

model_columns.pkl

🚀 Run the App
Launch the Gradio interface:

bash
Copy code
python app.py
This opens a local web app where you can input features and get the predicted life expectancy.

Example inputs:

Schooling: 12

Income composition of resources: 0.65

BMI: 22

Alcohol: 3

Adult Mortality: 200

HIV/AIDS: 0.1

thinness 1-19 years: 5

Output → Predicted Life Expectancy

🖼️ App Preview
Gradio app interface:

Input boxes for health & socio-economic factors

Output: Predicted Life Expectancy (years)

📦 Requirements
nginx
Copy code
numpy
pandas
matplotlib
seaborn
scikit-learn
gradio
Install with:

bash
Copy code
pip install -r requirements.txt
📈 Results
Random Forest outperformed Linear Regression with R² = 0.95

Top correlated features with life expectancy:

Schooling

Income composition of resources

BMI

GDP

Alcohol

✨ Future Improvements
Add more feature engineering

Use XGBoost / LightGBM for better accuracy

Deploy the Gradio app on Hugging Face Spaces or Streamlit Cloud
