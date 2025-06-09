import streamlit as st
import pandas as pd
import altair as alt
from datetime import datetime, timedelta
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Set Streamlit page configuration
st.set_page_config(page_title="Financial Dashboard", layout="wide")

# Load data from CSV
@st.cache_data
def load_data():
    df = pd.read_csv('filtered_financial_data.csv')
    df['date'] = pd.to_datetime(df['date'])
    df['Transaction Amount'] = df['Transaction Amount'].astype(float)
    return df

df = load_data()

# Sidebar filters
st.sidebar.header("Filters")
categories = ['All'] + sorted(df['Category'].unique().tolist())
selected_category = st.sidebar.selectbox("Select Category", categories)

months = pd.to_datetime(df['date']).dt.to_period('M').unique()
month_options = ['All'] + [month.strftime('%B %Y') for month in sorted(months)]
selected_month = st.sidebar.selectbox("Select Month", month_options)

# Apply filters based on user selections
filtered_df = df
if selected_category != 'All':
    filtered_df = filtered_df[filtered_df['Category'] == selected_category]
if selected_month != 'All':
    selected_period = pd.Period(selected_month, 'M')
    filtered_df = filtered_df[pd.to_datetime(filtered_df['date']).dt.to_period('M') == selected_period]

# Display key metrics
col1, col2, col3, col4 = st.columns(4)
total_transactions = filtered_df['Transaction Amount'].sum()
average_transaction = filtered_df['Transaction Amount'].mean()
total_income = filtered_df[filtered_df['Transaction Amount'] > 0]['Transaction Amount'].sum()
total_expenses = abs(filtered_df[filtered_df['Transaction Amount'] < 0]['Transaction Amount'].sum())

col1.metric("Net Transaction Amount", f"${total_transactions:,.2f}")
col2.metric("Average Transaction Amount", f"${average_transaction:,.2f}")
col3.metric("Total Income", f"${total_income:,.2f}")
col4.metric("Total Expenses", f"${total_expenses:,.2f}")

# Chart for daily transaction amounts over time
daily_data = filtered_df.groupby('date')['Transaction Amount'].sum().reset_index()
chart_transactions = alt.Chart(daily_data).mark_line().encode(
    x='date:T',
    y='Transaction Amount:Q',
    tooltip=['date:T', 'Transaction Amount:Q']
).properties(title='Daily Transaction Amount Over Time')
st.altair_chart(chart_transactions, use_container_width=True)

# Pie chart for income distribution by category
income_data = filtered_df[filtered_df['Transaction Amount'] > 0].groupby('Category')['Transaction Amount'].sum().reset_index()
income_pie = alt.Chart(income_data).mark_arc().encode(
    theta=alt.Theta(field='Transaction Amount', type='quantitative'),
    color=alt.Color(field='Category', type='nominal'),
    tooltip=['Category', 'Transaction Amount']
).properties(title='Income Distribution by Category')

# Pie chart for expenditure distribution by category
expense_data = filtered_df[filtered_df['Transaction Amount'] < 0].groupby('Category')['Transaction Amount'].sum().reset_index()
expense_data['Transaction Amount'] = expense_data['Transaction Amount'].abs()
expense_pie = alt.Chart(expense_data).mark_arc().encode(
    theta=alt.Theta(field='Transaction Amount', type='quantitative'),
    color=alt.Color(field='Category', type='nominal'),
    tooltip=['Category', 'Transaction Amount']
).properties(title='Expenditure Distribution by Category')

st.altair_chart(income_pie, use_container_width=True)
st.altair_chart(expense_pie, use_container_width=True)

# Functions to prepare data, train model, and make predictions
def prepare_data(df):
    df['date'] = pd.to_datetime(df['date'])
    df['days_since_start'] = (df['date'] - df['date'].min()).dt.days
    return df

def train_model(df, target):
    X = df[['days_since_start']]
    y = df[target]
    model = LinearRegression()
    model.fit(X, y)
    return model

def make_predictions(model, df, days_to_predict=30):
    last_date = df['date'].max()
    future_dates = pd.date_range(start=last_date + timedelta(days=1), periods=days_to_predict)
    future_df = pd.DataFrame({'date': future_dates})
    future_df['days_since_start'] = (future_df['date'] - df['date'].min()).dt.days
    predictions = model.predict(future_df[['days_since_start']])
    future_df['prediction'] = predictions
    return future_df

# Function to predict future transactions
def predict_future_transactions(df):
    prepared_df = prepare_data(df)
    transaction_model = train_model(prepared_df, 'Transaction Amount')
    future_transactions = make_predictions(transaction_model, prepared_df, days_to_predict=30)
    future_income = future_transactions[future_transactions['prediction'] > 0]
    future_expenditure = future_transactions[future_transactions['prediction'] < 0]
    return future_income, future_expenditure

# Predict future income and expenditure
future_income, future_expenditure = predict_future_transactions(df)

# Display predictions
st.header("Predictions")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Predicted Income")
    chart_predicted_income = alt.Chart(future_income).mark_line().encode(
        x='date:T',
        y='prediction:Q',
        tooltip=['date:T', 'prediction:Q']
    ).properties(title='Predicted Daily Income for Next 30 Days')
    st.altair_chart(chart_predicted_income, use_container_width=True)

with col2:
    st.subheader("Predicted Expenditure")
    chart_predicted_expenditure = alt.Chart(future_expenditure).mark_line().encode(
        x='date:T',
        y='prediction:Q',
        tooltip=['date:T', 'prediction:Q']
    ).properties(title='Predicted Daily Expenditure for Next 30 Days')
    st.altair_chart(chart_predicted_expenditure, use_container_width=True)

# Monthly category-wise transaction breakdown (Bar Chart)
monthly_category_data = filtered_df.groupby([pd.Grouper(key='date', freq='M'), 'Category'])['Transaction Amount'].sum().reset_index()
chart_category_monthly = alt.Chart(monthly_category_data).mark_bar().encode(
    x=alt.X('yearmonth(date):T', title='Month'),
    y=alt.Y('Transaction Amount:Q', title='Transaction Amount'),
    color='Category:N',
    tooltip=['yearmonth(date):T', 'Category:N', 'Transaction Amount:Q']
).properties(title='Monthly Transaction Breakdown by Category')
st.altair_chart(chart_category_monthly, use_container_width=True)

# Predictions with uncertainty (confidence intervals)
def make_predictions_with_uncertainty(model, df, days_to_predict=30, confidence_interval=0.1):
    future_df = make_predictions(model, df, days_to_predict)
    future_df['upper_bound'] = future_df['prediction'] * (1 + confidence_interval)
    future_df['lower_bound'] = future_df['prediction'] * (1 - confidence_interval)
    return future_df

# Prepare for prediction with uncertainty
prepared_df = prepare_data(df)
transaction_model = train_model(prepared_df, 'Transaction Amount')

# Predict future transactions with uncertainty
future_with_uncertainty = make_predictions_with_uncertainty(transaction_model, df)

# Chart with prediction and uncertainty bands
chart_future_with_uncertainty = alt.Chart(future_with_uncertainty).mark_line().encode(
    x='date:T',
    y='prediction:Q'
).properties(title='Predicted Future Transactions with Confidence Interval').interactive()

# Add confidence interval bands
band = alt.Chart(future_with_uncertainty).mark_area(opacity=0.3).encode(
    x='date:T',
    y='lower_bound:Q',
    y2='upper_bound:Q'
)

st.altair_chart(chart_future_with_uncertainty + band, use_container_width=True)


# Box Plot of Transaction Amounts per Category
box_plot = alt.Chart(filtered_df).mark_boxplot().encode(
    x=alt.X('Category:N', title='Category'),
    y=alt.Y('Transaction Amount:Q', title='Transaction Amount'),
    color='Category:N',
    tooltip=['Category:N', 'Transaction Amount:Q']
).properties(
    title='Transaction Amount Distribution per Category'
)

st.altair_chart(box_plot, use_container_width=True)

# Treemap of Categories
treemap_data = filtered_df.groupby('Category')['Transaction Amount'].sum().reset_index()

treemap = alt.Chart(treemap_data).mark_rect().encode(
    x=alt.X('sum(Transaction Amount):Q', title='Transaction Amount'),
    y=alt.Y('Category:N', title='Category', sort='-x'),
    color=alt.Color('Category:N', legend=None),
    tooltip=['Category:N', 'sum(Transaction Amount):Q']
).properties(
    title='Transaction Amount by Category Treemap'
)

st.altair_chart(treemap, use_container_width=True)


# Waterfall Chart for Income and Expenses
waterfall_data = filtered_df.groupby('date')['Transaction Amount'].sum().reset_index()
waterfall_data['type'] = waterfall_data['Transaction Amount'].apply(lambda x: 'Income' if x > 0 else 'Expense')

waterfall_chart = alt.Chart(waterfall_data).mark_bar().encode(
    x='date:T',
    y='Transaction Amount:Q',
    color=alt.Color('type:N', scale=alt.Scale(domain=['Income', 'Expense'], range=['green', 'red'])),
    tooltip=['date:T', 'Transaction Amount:Q']
).properties(
    title='Income and Expenses Waterfall Chart'
)
st.altair_chart(waterfall_chart, use_container_width=True)


# Animated Line Chart for Transaction Trends
transaction_trend = daily_data.reset_index()
transaction_trend['month'] = transaction_trend['date'].dt.to_period('M')

animation_chart = alt.Chart(transaction_trend).mark_line(interpolate='basis').encode(
    x='date:T',
    y='Transaction Amount:Q',
    color='month:N',
    tooltip=['date:T', 'Transaction Amount:Q']
).properties(title='Transaction Trends Over Time').add_params(
    alt.selection_interval(bind='scales')
)

st.altair_chart(animation_chart, use_container_width=True)


# Bubble Chart for Transactions by Category
bubble_data = filtered_df.groupby('Category').agg(
    Total_Amount=('Transaction Amount', 'sum'),
    Transaction_Count=('Transaction Amount', 'count')
).reset_index()

bubble_chart = alt.Chart(bubble_data).mark_circle(size=60).encode(
    x='Transaction_Count:Q',
    y='Total_Amount:Q',
    color='Category:N',
    tooltip=['Category:N', 'Total_Amount:Q', 'Transaction_Count:Q']
).properties(title='Transactions by Category')

st.altair_chart(bubble_chart, use_container_width=True)


# Dual-axis Chart for Income and Expenses
dual_axis_data = daily_data.copy()
dual_axis_data['type'] = dual_axis_data['Transaction Amount'].apply(lambda x: 'Income' if x > 0 else 'Expense')

dual_axis_chart = alt.Chart(dual_axis_data).mark_line().encode(
    x='date:T',
    y=alt.Y('Transaction Amount:Q', axis=alt.Axis(title='Transaction Amount')),
    color='type:N',
    tooltip=['date:T', 'Transaction Amount:Q']
).properties(title='Income vs. Expenses Over Time')

st.altair_chart(dual_axis_chart, use_container_width=True)


heatmap_data = filtered_df.groupby([pd.Grouper(key='date', freq='D'), 'Category'])['Transaction Amount'].sum().reset_index()
heatmap = alt.Chart(heatmap_data).mark_rect().encode(
    x=alt.X('date:T', title='Date'),
    y=alt.Y('Category:N', title='Category'),
    color=alt.Color('Transaction Amount:Q', scale=alt.Scale(scheme='viridis')),
    tooltip=['date:T', 'Category:N', 'Transaction Amount:Q']
).properties(title='Heatmap of Transactions by Date and Category')

st.altair_chart(heatmap, use_container_width=True)


import numpy as np

def radar_chart(data):
    categories = list(data['Category'])
    values = list(data['Transaction Amount'])

    angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
    values += values[:1]  # Repeat the first value to close the circle
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.fill(angles, values, color='blue', alpha=0.25)
    ax.plot(angles, values, color='blue', linewidth=2)

    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)
    st.pyplot(fig)

# Prepare data for radar chart
radar_data = filtered_df.groupby('Category')['Transaction Amount'].sum().reset_index()
radar_chart(radar_data)
