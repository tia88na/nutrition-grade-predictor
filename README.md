# NutriScan - Nutrition Grade Analysis System 🍎

A machine learning web application that analyzes nutrition grades and health scores of food products from a dataset of 5,000 US food products.

## Overview

This project is part of the **COE305 Machine Learning Course** and aims to help consumers make better food choices by analyzing nutrition grades and health risk scores of food products based on their nutritional information.

The application uses a dataset of 5,000 US food products from Open Food Facts, allowing users to explore real product data and understand health implications of different food choices.

## Features

- 🔍 **Product Selection** - Browse and select from 4,026 food products with nutrition grades
- 📊 **Nutrition Analysis** - View detailed nutritional values per 100g
- 🎯 **Health Risk Score** - See health risk scores from 1 (Very Risky) to 5 (Very Healthy)
- 🎨 **Color-Coded Grades** - Visual representation of nutrition grades (A-E)
- 💡 **Nutritional Insights** - Get personalized insights about specific nutrients
- 🔬 **Ingredient Analysis** - View ingredients and food additives
- 🎛️ **Filtering Options** - Filter by nutrition grade and search by product name

## Nutrition Grade System

- **Grade A**: Best nutritional quality (Very Healthy - Score 5)
- **Grade B**: Good nutritional quality (Healthy - Score 4)  
- **Grade C**: Average nutritional quality (Moderate - Score 3)
- **Grade D**: Poor nutritional quality (Unhealthy - Score 2)
- **Grade E**: Lowest nutritional quality (Very Risky - Score 1)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/tia88na/needapp.git
cd needapp
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Extract the model (if not already extracted):
```bash
unzip model.pkl.zip
```

## Usage

Run the Streamlit app:
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## How to Use the Application

1. **Select a Product**: Choose from 4,026 products using the dropdown menu
2. **Filter Products**: Use the nutrition grade filter or search by product name
3. **View Nutritional Information**: See detailed nutritional values per 100g
4. **Analyze Health Score**: Review the health risk score (1-5 scale)
5. **Check Nutrition Score**: View the Nutri-Score value (lower is better)
6. **Explore Insights**: Expand the nutritional insights section for personalized recommendations
7. **Review Ingredients**: Check ingredients and additives in expandable sections

## Dataset Information

- **Source**: Open Food Facts - World Food Facts
- **Size**: 5,000 US food products
- **Products with Grades**: 4,026 products
- **Features**: 15 columns including nutritional values, ingredients, and additives
- **Nutrition Grades**: A, B, C, D, E

### Selected Columns:
- product_name
- countries
- categories
- ingredients_text
- additives_tags
- energy_100g
- fat_100g
- saturated-fat_100g
- sugars_100g
- salt_100g
- proteins_100g
- fiber_100g
- carbohydrates_100g
- nutrition_grade_fr
- nutrition-score-fr_100g

## Model Details

- **Algorithm**: Random Forest Classifier
- **Framework**: scikit-learn
- **Training Data**: 5,000 US food products
- **Input Features**: 8 numerical features (nutritional values per 100g)
- **Output**: Nutrition grade (A, B, C, D, or E)
- **Model File**: `model.pkl` (compressed in `model.pkl.zip`)

## Project Team

**COE305 Machine Learning - Stage 2**

- Eda Şahin (220901745) - Section 3
- Tuana Harmankaya (2309111029) - Section 2
- Zehra Özcan (2309011051) - Section 2

## Files

- `app.py`: Main Streamlit application
- `model.pkl.zip`: Trained Random Forest model (compressed)
- `nutrients_csvfile.csv`: Dataset with 5,000 food products
- `requirements.txt`: Python dependencies
- `README.md`: Project documentation
- `USAGE.md`: Quick start guide

## Technologies Used

- Python 3.12+
- Streamlit
- scikit-learn
- pandas
- numpy
- joblib

## Educational Purpose

This is an educational project for the COE305 Machine Learning course. The nutrition grades and health scores are based on the Nutri-Score system and should not replace professional nutritional advice.

## License

MIT License

## Acknowledgments

- Dataset: [Open Food Facts](https://www.kaggle.com/datasets/openfoodfacts/world-food-facts)
- Course: COE305 Machine Learning
- Nutri-Score System for nutrition grading methodology