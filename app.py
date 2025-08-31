import gradio as gr
import pandas as pd
import pickle
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("model_columns.pkl", "rb") as f:
    model_columns = pickle.load(f)
def predict_life_expectancy(*args):
    input_data = pd.DataFrame([args], columns=model_columns)
    prediction = model.predict(input_data)[0]
    return prediction
inputs = [gr.Number(label=col) for col in model_columns]
outputs = gr.Number(label="Predicted Life Expectancy")

gr.Interface(
    fn=predict_life_expectancy,
    inputs=inputs,
    outputs=outputs,
    title="Life Expectancy Predictor 🌍",
    description="Predict life expectancy based on socio-economic and health features."
).launch()
