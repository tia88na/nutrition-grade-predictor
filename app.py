"""
NutriScan - Predicting Health Risk from Food Product Labels
A Streamlit web application for analyzing nutrition grades and health scores of food products
"""

import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="NutriScan - Nutrition Analysis",
    page_icon="🍎",
    layout="wide"
)

# Load the dataset
@st.cache_data
def load_dataset():
    """Load the food products dataset"""
    try:
        # Skip the first row which is a description, use second row as header
        df = pd.read_csv('nutrients_csvfile.csv', sep=';', skiprows=1)
        # Remove rows with missing nutrition grades
        df = df.dropna(subset=['nutrition_grade_fr'])
        return df
    except Exception as e:
        st.error(f"Error loading dataset: {e}")
        return None

# Load the model
@st.cache_resource
def load_model():
    """Load the trained Random Forest model"""
    try:
        model = joblib.load('model.pkl')
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

# Title and description
st.title("🍎 NutriScan - Nutrition Grade Analysis System")
st.markdown("""
This application analyzes **nutrition grades** (A, B, C, D, or E) and **health scores** of food products 
from a dataset of 5,000 US food products.

- **Grade A**: Best nutritional quality (Very Healthy - Score 5)
- **Grade B**: Good nutritional quality (Healthy - Score 4)
- **Grade C**: Average nutritional quality (Moderate - Score 3)
- **Grade D**: Poor nutritional quality (Unhealthy - Score 2)
- **Grade E**: Lowest nutritional quality (Very Risky - Score 1)

Select a product from the dataset to view its nutritional information and health score.
""")

st.divider()

# Load data
df = load_dataset()

if df is not None:
    # Product selection section
    st.subheader("🔍 Select a Food Product")
    
    # Filter options
    filter_col1, filter_col2 = st.columns(2)
    
    with filter_col1:
        # Grade filter
        grade_filter = st.multiselect(
            "Filter by Nutrition Grade",
            options=['a', 'b', 'c', 'd', 'e'],
            default=[],
            format_func=lambda x: f"Grade {x.upper()}"
        )
    
    with filter_col2:
        # Search by product name
        search_term = st.text_input("Search Product Name", "")
    
    # Apply filters
    filtered_df = df.copy()
    if grade_filter:
        filtered_df = filtered_df[filtered_df['nutrition_grade_fr'].isin(grade_filter)]
    if search_term:
        filtered_df = filtered_df[filtered_df['product_name'].str.contains(search_term, case=False, na=False)]
    
    # Product selection
    if len(filtered_df) > 0:
        # Create a display name with nutrition grade
        filtered_df['display_name'] = filtered_df.apply(
            lambda row: f"{row['product_name']} (Grade: {str(row['nutrition_grade_fr']).upper()})", 
            axis=1
        )
        
        selected_product_display = st.selectbox(
            f"Choose from {len(filtered_df)} products:",
            options=filtered_df['display_name'].tolist(),
            index=0
        )
        
        # Get the selected product data
        selected_idx = filtered_df[filtered_df['display_name'] == selected_product_display].index[0]
        product = df.loc[selected_idx]
        
        st.divider()
        
        # Display product information
        st.subheader(f"📦 {product['product_name']}")
        
        # Product details in columns
        detail_col1, detail_col2 = st.columns(2)
        
        with detail_col1:
            st.markdown("### Product Information")
            if pd.notna(product['categories']):
                st.write(f"**Category:** {product['categories']}")
            else:
                st.write("**Category:** Not specified")
            st.write(f"**Country:** {product['countries']}")
            
            if pd.notna(product['ingredients_text']):
                with st.expander("📝 View Ingredients"):
                    st.write(product['ingredients_text'])
            
            if pd.notna(product['additives_tags']):
                with st.expander("🧪 View Additives"):
                    additives = product['additives_tags'].split(',') if isinstance(product['additives_tags'], str) else []
                    for additive in additives:
                        st.write(f"- {additive}")
        
        with detail_col2:
            st.markdown("### Nutritional Values (per 100g)")
            
            # Create nutritional table
            nutrition_data = {
                'Nutrient': [
                    'Energy',
                    'Fat',
                    'Saturated Fat',
                    'Sugars',
                    'Salt',
                    'Proteins',
                    'Fiber',
                    'Carbohydrates'
                ],
                'Value': [
                    f"{product['energy_100g']:.2f} kcal" if pd.notna(product['energy_100g']) else "N/A",
                    f"{product['fat_100g']:.2f} g" if pd.notna(product['fat_100g']) else "N/A",
                    f"{product['saturated-fat_100g']:.2f} g" if pd.notna(product['saturated-fat_100g']) else "N/A",
                    f"{product['sugars_100g']:.2f} g" if pd.notna(product['sugars_100g']) else "N/A",
                    f"{product['salt_100g']:.2f} g" if pd.notna(product['salt_100g']) else "N/A",
                    f"{product['proteins_100g']:.2f} g" if pd.notna(product['proteins_100g']) else "N/A",
                    f"{product['fiber_100g']:.2f} g" if pd.notna(product['fiber_100g']) else "N/A",
                    f"{product['carbohydrates_100g']:.2f} g" if pd.notna(product['carbohydrates_100g']) else "N/A",
                ]
            }
            
            nutrition_df = pd.DataFrame(nutrition_data)
            st.dataframe(nutrition_df, hide_index=True, use_container_width=True)
        
        st.divider()
        
        # Display nutrition grade and health score
        st.subheader("📊 Nutrition Analysis")
        
        result_col1, result_col2, result_col3 = st.columns([1, 1, 1])
        
        with result_col1:
            st.markdown("#### Nutrition Grade")
            
            # Get the actual grade from dataset
            actual_grade = str(product['nutrition_grade_fr']).lower()
            
            # Color coding for grades
            grade_colors = {
                'a': '#038141',  # Dark green
                'b': '#85BB2F',  # Light green
                'c': '#FECB02',  # Yellow
                'd': '#EE8100',  # Orange
                'e': '#E63E11'   # Red
            }
            
            color = grade_colors.get(actual_grade, '#888888')
            
            st.markdown(f"""
            <div style="
                background-color: {color};
                padding: 30px;
                border-radius: 15px;
                text-align: center;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            ">
                <h1 style="color: white; font-size: 60px; margin: 0; font-weight: bold;">
                    {actual_grade.upper()}
                </h1>
            </div>
            """, unsafe_allow_html=True)
        
        with result_col2:
            st.markdown("#### Health Risk Score")
            
            # Map grade to health score (1=Very Risky, 5=Very Healthy)
            health_score_mapping = {
                'a': 5,
                'b': 4,
                'c': 3,
                'd': 2,
                'e': 1
            }
            
            health_score = health_score_mapping.get(actual_grade, 3)
            
            # Color for health score
            score_colors = {
                5: '#038141',
                4: '#85BB2F',
                3: '#FECB02',
                2: '#EE8100',
                1: '#E63E11'
            }
            
            score_color = score_colors.get(health_score, '#888888')
            
            st.markdown(f"""
            <div style="
                background-color: {score_color};
                padding: 30px;
                border-radius: 15px;
                text-align: center;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            ">
                <h1 style="color: white; font-size: 60px; margin: 0; font-weight: bold;">
                    {health_score}/5
                </h1>
            </div>
            """, unsafe_allow_html=True)
        
        with result_col3:
            st.markdown("#### Nutrition Score")
            
            # Display the nutrition score from dataset
            nutrition_score = product['nutrition-score-fr_100g']
            
            if pd.notna(nutrition_score):
                # Determine color based on score (lower is better)
                if nutrition_score < 0:
                    score_display_color = '#038141'
                elif nutrition_score < 3:
                    score_display_color = '#85BB2F'
                elif nutrition_score < 11:
                    score_display_color = '#FECB02'
                elif nutrition_score < 19:
                    score_display_color = '#EE8100'
                else:
                    score_display_color = '#E63E11'
                
                st.markdown(f"""
                <div style="
                    background-color: {score_display_color};
                    padding: 30px;
                    border-radius: 15px;
                    text-align: center;
                    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                ">
                    <h1 style="color: white; font-size: 60px; margin: 0; font-weight: bold;">
                        {nutrition_score:.0f}
                    </h1>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.info("Score not available")
        
        # Explanation section
        st.divider()
        st.subheader("📖 Health Risk Assessment")
        
        health_explanations = {
            'a': "**Very Healthy (Score 5)** - This product has excellent nutritional quality. It's low in unhealthy nutrients (saturated fats, sugars, salt) and high in beneficial ones (fiber, protein). Recommended for regular consumption.",
            'b': "**Healthy (Score 4)** - This product has good nutritional quality. It's a healthy choice for most people with a balanced nutrient profile. Safe for regular consumption.",
            'c': "**Moderate (Score 3)** - This product has average nutritional quality. Consider consuming in moderation as part of a balanced diet. Not harmful but not optimal for health.",
            'd': "**Unhealthy (Score 2)** - This product has poor nutritional quality. It may be high in unhealthy nutrients. Consider healthier alternatives when possible and limit consumption.",
            'e': "**Very Risky (Score 1)** - This product has the lowest nutritional quality. It's likely high in saturated fats, sugars, or salt. Limit consumption and opt for healthier choices."
        }
        
        explanation = health_explanations.get(actual_grade, "Health assessment not available.")
        st.info(explanation)
        
        # Additional nutritional insights
        with st.expander("💡 Nutritional Insights"):
            st.markdown("#### Key Nutritional Indicators")
            
            insights = []
            
            # Energy analysis
            if pd.notna(product['energy_100g']):
                energy = product['energy_100g']
                if energy < 200:
                    insights.append("✅ Low in energy - suitable for weight management")
                elif energy > 500:
                    insights.append("⚠️ High in energy - consume in small portions")
            
            # Fat analysis
            if pd.notna(product['fat_100g']):
                fat = product['fat_100g']
                if fat < 3:
                    insights.append("✅ Low-fat product")
                elif fat > 20:
                    insights.append("⚠️ High in fat content")
            
            # Sugar analysis
            if pd.notna(product['sugars_100g']):
                sugar = product['sugars_100g']
                if sugar < 5:
                    insights.append("✅ Low in sugar")
                elif sugar > 22.5:
                    insights.append("⚠️ High in sugar - limit consumption")
            
            # Salt analysis
            if pd.notna(product['salt_100g']):
                salt = product['salt_100g']
                if salt < 0.3:
                    insights.append("✅ Low in salt")
                elif salt > 1.5:
                    insights.append("⚠️ High in salt - may affect blood pressure")
            
            # Fiber analysis
            if pd.notna(product['fiber_100g']):
                fiber = product['fiber_100g']
                if fiber > 6:
                    insights.append("✅ High in fiber - good for digestion")
                elif fiber < 3:
                    insights.append("ℹ️ Low in fiber")
            
            # Protein analysis
            if pd.notna(product['proteins_100g']):
                protein = product['proteins_100g']
                if protein > 10:
                    insights.append("✅ Good source of protein")
            
            if insights:
                for insight in insights:
                    st.write(insight)
            else:
                st.write("No specific insights available for this product.")
    
    else:
        st.warning("No products found matching your filters. Please adjust your search criteria.")

else:
    st.error("❌ Failed to load the dataset. Please ensure 'nutrients_csvfile.csv' is present in the application directory.")
    st.info("The dataset file should be semicolon-separated (;) and contain nutrition grade information.")

# Footer
st.divider()
st.markdown("""
<div style="text-align: center; color: #666; padding: 20px;">
    <p><strong>NutriScan Project</strong> - COE305 Machine Learning Course</p>
    <p>Predicting Health Risk from Food Product Labels | Dataset: 5,000 US Food Products</p>
    <p style="font-size: 12px;">Note: This is an educational project and should not replace professional nutritional advice.</p>
</div>
""", unsafe_allow_html=True)
