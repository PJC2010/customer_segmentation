import pandas as  pd
import plotly as plt

df= pd.read_csv('customer_segmentation_city.csv')

def create_bubble_chart(df):
    fig = px.scatter(df,
                    x='total_customers',
                    y='avg_customer_spend',
                    size='high_value_customers',
                    color='max_customer_spend',
                    hover_name='city',
                    title='City Customer Segmentation Analysis')
    fig.update_layout(
        xaxis_title="Total Customers",
        yaxis_title="Average Customer Spend ($)",
        showlegend=True
    )
    fig.show()