from flask import Flask, render_template, request
import pandas as pd
import xgboost as xgb
import warnings
from xgboost import XGBRegressor

app = Flask(__name__)

# Suppress XGBoost warnings about pickle
warnings.filterwarnings("ignore", category=UserWarning)

# Load the model
model = None
try:
    model = XGBRegressor()
    model.load_model('best_sales_model.json')
    print("✅ Model loaded successfully")
except Exception as e:
    print(f"❌ Error loading model: {str(e)}")
    try:
        import joblib
        model = joblib.load('best_sales_model.pkl')
        print("⚠️  Model loaded from pickle format")
    except Exception as e:
        print(f"❌ Failed to load model: {str(e)}")

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        if request.method == 'POST':
            if model is None:
                return render_template('index.html', 
                                    prediction="Error: Model not loaded",
                                    success=False)

            # Get form data with defaults
            input_data = {
                'Store_Type': request.form.get('store_type', 'S1'),
                'Location_Type': request.form.get('location_type', 'L1'),
                'Region_Code': request.form.get('region_code', 'R1'),
                'Holiday': int(request.form.get('holiday', 0)),
                '#Order': int(request.form.get('order', 10)),
                'Month': int(request.form.get('month', 1)),
                'Day': int(request.form.get('day', 1)),
                'Weekday': int(request.form.get('weekday', 0))
            }

            # Process data
            input_df = pd.DataFrame([input_data])
            input_df = pd.get_dummies(input_df, 
                                    columns=['Store_Type', 'Location_Type', 'Region_Code'],
                                    drop_first=True)

            expected_features = [
                'Holiday', '#Order', 'Month', 'Day', 'Weekday',
                'Store_Type_S2', 'Store_Type_S3', 'Store_Type_S4',
                'Location_Type_L2', 'Location_Type_L3', 'Location_Type_L4', 'Location_Type_L5',
                'Region_Code_R2', 'Region_Code_R3', 'Region_Code_R4'
            ]

            # Add missing columns
            for feature in expected_features:
                if feature not in input_df.columns:
                    input_df[feature] = 0

            # Predict
            prediction = model.predict(input_df[expected_features])[0]
            return render_template('index.html',
                                prediction=f"${prediction:,.2f}",
                                success=True)

        # GET request - show empty form
        return render_template('index.html', prediction=None)

    except Exception as e:
        return render_template('index.html',
                            prediction=f"Error: {str(e)}",
                            success=False)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)