# AI_Finance_Project
# 🚀 Check out the 2nd place winner at Hackathon Startup Week 2024!

## Project Description

This project is a web application for expense analysis and prediction, developed as part of my participation in the Hackathon Startup Week 2024. I am pleased to announce that this project was awarded **second place** at the event, standing out among the innovative solutions presented where 5 teams competed over 24 hours to develop solutions for the proposed challenge in the banking sector.

The application uses advanced time series analysis techniques and machine learning models to predict a company's future expenses. Leveraging historical expense data, the system provides accurate predictions by expense category, allowing businesses to better manage their budgets and make informed decisions.

# 📊 Business Expense Analysis and Prediction

This project aims to:

1. **Predict future expenses** of a company based on historical data from multiple companies.
2. **Classify expenses** into different categories and predict the percentage allocated to each category.
3. **Visualize data** and predictions through interactive graphs.

## 📚 Repository Contents

- **Input Data**: `data.csv` with information on categorized expenses.
- **Analysis Notebook**: Code for data preprocessing, model training, and graph generation.
- **Trained Models**: Saved prediction models for future use.

## 🛠 Technologies Used

- **Python** 🐍
- **Pandas** 🧩
- **TensorFlow** 🤖
- **Plotly** 📈
- **Scikit-learn** 📊

## 📁 Repository Structure

- `data/`:
  - `data.csv`: Dataset with transaction data.
  - `model_<cc_num>.keras`: Trained models.
  - `model_<cc_num>.h5`: Trained models in HDF5 format.
  - `model_<cc_num>.pkl`: Trained models in pickle format.
  - `summary_<cc_num>.txt`: Model summary.
  - `df_metrics_<cc_num>.csv`: Model metrics.

- `scripts/`:
  - `expense_prediction.py`: Script to predict future expenses.
  - `visualization.py`: Script to generate interactive graphs.

## 🚀 Getting Started

### 1. Clone the Repository

Clone the repository to your local machine:
```bash
git clone https://github.com/yourusername/expense-analysis-prediction.git
```
## 2. Install Dependencies

Install the necessary dependencies:

```bash
pip install -r requirements.txt
```
## 3. Prepare the Data

Place your `data.csv` file in the `data/` folder.

## 4. Run the Analysis

Run the scripts to analyze and predict expenses:

### Model Training and Prediction:

```bash
python scripts/expense_prediction.py
```

### Data Visualization:

Run the script to generate interactive graphs:

```bash
python scripts/visualization.py
```

## 📊 Visualizations

The project includes several types of graphs to explore the data:

- Line Graph of Expense Trends by Category
- Stacked Bar Graph of Expense by Category
- Scatter Plot of Expense by Date and Time
- Pie Chart of Expense Distribution by Category
- Heatmap of Expense by Category and Date
- Box Plot of Expense Distribution
- Bar Graph of Average Expense by Hour of the Day

These graphs will help you better understand expense behavior and identify patterns.

## 📝 Additional Documentation

For a detailed explanation of time series analysis, model building, and interactive graph usage, review the notebook and scripts provided in the repository.

## 📞 Contact

Have questions or suggestions? Feel free to reach out to me at ena.ateibuz@gmail.com 💬

- GitHub: [GitHub Profile](https://github.com/yourusername)
- LinkedIn: [Ana on LinkedIn](https://www.linkedin.com/in/ana-zubieta/)

Thank you for visiting my repository! I hope you find this project useful and interesting. 🙌

⭐ If you liked this project, please give it a star and follow me on LinkedIn for more similar content. ⭐
