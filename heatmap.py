import pandas as  pd
import plotly as plt

df= pd.read_csv('customer_segmentation_city.csv')
def create_heatmap(df):
    # Normalize the data
    metrics = ['total_customers', 'high_value_customers',
                'avg_customer_spend', 'max_customer_spend']
    normalized_data = df[metrics].apply(lambda x: (x - x.min()) / (x.max() - x.min()))
    normalized_data['city'] = df['city']
    plt.figure(figsize=(10, 8))
    sns.heatmap(normalized_data.set_index('city')[metrics],
                cmap='YlOrRd',
                annot=True,
                fmt='.2f')
    plt.title('Normalized Customer Metrics by City')
    plt.tight_layout()
    plt.show()