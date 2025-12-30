# Quick Start Guide - NutriScan

## Running the Application

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Extract the Model (if needed)
If the `model.pkl` file is not present in the root directory:
```bash
unzip model.pkl.zip
```

### Step 3: Run the Streamlit App
```bash
streamlit run app.py
```

The app will automatically open in your default browser at `http://localhost:8501`

## Using the Application

### 1. Select a Product
- Use the dropdown menu to select from 4,026 US food products
- Each product shows its name and nutrition grade in the dropdown

### 2. Filter Products (Optional)
- **Filter by Nutrition Grade**: Select one or more grades (A, B, C, D, E) to narrow down the list
- **Search by Name**: Type part of a product name to find specific items

### 3. View Product Information
Once a product is selected, you'll see:
- **Product Details**: Name, category, country of origin
- **Ingredients**: Complete list of ingredients (expandable)
- **Additives**: Food additives present in the product (expandable)

### 4. Analyze Nutritional Values
The nutritional values table shows per 100g:
- Energy (kcal)
- Fat (g)
- Saturated Fat (g)
- Sugars (g)
- Salt (g)
- Proteins (g)
- Fiber (g)
- Carbohydrates (g)

### 5. Review Health Analysis
Three key metrics are displayed:
- **Nutrition Grade**: Letter grade from A (best) to E (worst)
- **Health Risk Score**: Numeric score from 1 (Very Risky) to 5 (Very Healthy)
- **Nutrition Score**: Nutri-Score value (lower numbers are better)

### 6. Check Nutritional Insights
Expand the "💡 Nutritional Insights" section to see:
- ✅ Positive nutritional attributes
- ⚠️ Nutrients to watch out for
- ℹ️ Additional information about the product

## Example: Finding Healthy Products

### To find the healthiest products:
1. Click on "Filter by Nutrition Grade"
2. Select "Grade A"
3. Browse through the filtered list
4. Select a product to see why it's healthy

### To find products to avoid:
1. Click on "Filter by Nutrition Grade"
2. Select "Grade E"
3. Browse through the filtered list
4. Check the nutritional insights to understand the health risks

## Understanding the Grades

### Grade A (Dark Green) - Very Healthy (Score 5)
- Low in unhealthy nutrients (saturated fats, sugars, salt)
- High in beneficial nutrients (fiber, protein)
- **Recommendation**: Excellent choice for regular consumption

### Grade B (Light Green) - Healthy (Score 4)
- Good nutritional balance
- Few unhealthy nutrients
- **Recommendation**: Safe for regular consumption

### Grade C (Yellow) - Moderate (Score 3)
- Average nutritional quality
- Some unhealthy nutrients present
- **Recommendation**: Consume in moderation

### Grade D (Orange) - Unhealthy (Score 2)
- Poor nutritional quality
- High in unhealthy nutrients
- **Recommendation**: Consider healthier alternatives, limit consumption

### Grade E (Red) - Very Risky (Score 1)
- Lowest nutritional quality
- Very high in saturated fats, sugars, or salt
- **Recommendation**: Avoid or consume rarely

## Understanding Nutrition Score

The Nutrition Score (Nutri-Score) is a numeric value:
- **Negative values to 2**: Excellent (Grade A)
- **3 to 10**: Good (Grade B)
- **11 to 18**: Average (Grade C)
- **19 to 26**: Poor (Grade D)
- **27+**: Very Poor (Grade E)

**Lower scores are better!**

## Nutritional Insights Explained

### Energy Levels
- **Low**: < 200 kcal/100g - Good for weight management
- **High**: > 500 kcal/100g - Consume in small portions

### Fat Content
- **Low-fat**: < 3g/100g
- **High-fat**: > 20g/100g

### Sugar Content
- **Low sugar**: < 5g/100g
- **High sugar**: > 22.5g/100g - Limit consumption

### Salt Content
- **Low salt**: < 0.3g/100g
- **High salt**: > 1.5g/100g - May affect blood pressure

### Fiber Content
- **High fiber**: > 6g/100g - Good for digestion
- **Low fiber**: < 3g/100g

### Protein Content
- **Good protein source**: > 10g/100g

## Search Tips

1. **Search by Brand**: Type the brand name in the search box
2. **Search by Food Type**: Try keywords like "yogurt", "cheese", "sauce"
3. **Combine Filters**: Use both grade filter and search together
4. **Clear Filters**: Remove all selections to see all 4,026 products again

## Troubleshooting

### Model Loading Error
- Make sure `model.pkl` exists in the root directory
- Extract it from `model.pkl.zip` if needed: `unzip model.pkl.zip`

### Dataset Not Found
- Ensure `nutrients_csvfile.csv` is in the root directory
- The file should be semicolon-separated (;)

### Missing Dependencies
- Run `pip install -r requirements.txt` to install all required packages

### Port Already in Use
- If port 8501 is already in use, run: `streamlit run app.py --server.port=8502`

### Browser Doesn't Open Automatically
- Manually navigate to the URL shown in the terminal (usually `http://localhost:8501`)

### Slow Performance
- The first time you select a product, the dataset loads (cached for future use)
- Subsequent selections will be faster

## Notes

- This application analyzes real food products from the Open Food Facts database
- The nutrition grades are based on the official Nutri-Score system
- Health risk scores are derived from nutrition grades (A=5, B=4, C=3, D=2, E=1)
- This is an educational project and should not replace professional nutritional advice
- Some products may have missing data for certain fields (will show as "N/A")

## Advanced Features

### Downloading Data
- Click the download button on the nutritional values table to export as CSV

### Viewing Full Ingredient Lists
- Click on "📝 View Ingredients" to see the complete ingredient list
- Useful for checking allergens or specific ingredients

### Checking Additives
- Click on "🧪 View Additives" to see food additives (E-numbers)
- Research specific additives if you have concerns

## Project Information

This is part of the **NutriScan Project** for COE305 Machine Learning Course:
- **Goal**: Predicting Health Risk from Food Product Labels
- **Dataset**: 5,000 US food products from Open Food Facts
- **Team**: Eda Şahin, Tuana Harmankaya, Zehra Özcan
