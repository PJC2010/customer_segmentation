import pandas as  pd
import plotly as plt

df= pd.read_csv('customer_segmentation_city.csv')

def create_stacked_bar(df):
    plt.figure(figsize=(12, 6))
    df_stack = df[['city', 'high_value_customers', 'total_customers']]
    df_stack['regular_customers'] = df_stack['total_customers'] - df_stack['high_value_customers']
    plt.bar(df['city'], df_stack['regular_customers'], label='Regular Customers')
    plt.bar(df['city'], df_stack['high_value_customers'],
        bottom=df_stack['regular_customers'], label='High Value Customers')
    plt.xticks(rotation=45, ha='right')
    plt.title('Customer Distribution by City')
    plt.xlabel('City')
    plt.ylabel('Number of Customers')
    plt.legend()
    plt.tight_layout()
    plt.show()
