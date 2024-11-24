# app.py

from flask import Flask, render_template, request, jsonify
import model
import pandas as pd
app = Flask(__name__)
data = pd.read_csv(r'd:\program1\project\spam.csv', encoding='latin-1')
import pandas as pd
import numpy as np

@app.route('/predict', methods=['POST'])
def predict():
    # Get the symptoms from the user input
    symptoms = request.form['symptoms']
    symptoms_list = symptoms.lower().split(',')

    # Prepare input data for prediction (ensuring feature order)
    input_data = np.zeros(len(symptom_features))
    
    for i, feature in enumerate(symptom_features):
        if feature in symptoms_list:
            input_data[i] = 1
    
    # Convert input data to a DataFrame with the correct feature names
    input_df = pd.DataFrame([input_data], columns=symptom_features)
    
    # Make prediction
    prediction = model.predict(input_df)[0]
    
    # You can customize the results here based on your prediction output
    disease = get_disease_name(prediction)
    description, precautions, medications, workouts, diets = get_disease_details(disease)

    return render_template('index.html', prediction=disease, description=description, precautions=precautions, medications=medications, workouts=workouts, diets=diets)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    symptoms = request.form.get("symptoms")  # Get user input from form
    user_symptoms = [symptom.strip() for symptom in symptoms.split(',')]
    disease = model.get_predicted_value(user_symptoms)
    
    # Get detailed information for the predicted disease
    desc, pre, med, die, wrkout = model.helper(disease)

    response = {
        "disease": disease,
        "description": desc,
        "precautions": pre,
        "medications": med,
        "diet": die,
        "workout": wrkout
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
print(data.columns)
