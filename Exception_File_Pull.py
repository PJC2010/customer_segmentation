import openpyxl
import pandas as pd





df = pd.read_excel(r"C:/Users/PeteCastillo/OneDrive - VillageMD\Documents - VMD- Quality Leadership- PHI/General/2024 Planning/Pharmacy/2024 Exception Process/Med Adherence Exception File 11.20.2024.xlsx", sheet_name='Master')

market_codes = ['Atlanta', 'Austin', 'Dallas', 'Detroit', 'ElPaso', 'Houston', 'Phoenix', 'SanAntonio']

df = df[df['MarketCode '].isin(market_codes)]

#Adding in UID for tracking purposes
df['UID'] = df['PayerCode'].astype(str) + df['PayerMemberId'].astype(str) + df['MedAdherenceMeasureCode'].astype(str)

def determine_contract_status(row):
   if row['MarketCode '] == 'Phoenix' and row['PayerCode'] in ['BCBSAZ', 'AetnaMA', 'United', 'WellCare', 'Devoted']:
       return 'HP Contract'
   elif row['MarketCode '] == 'Denver' and row['PayerCode'] == 'United':
       return 'HP Contract'
   elif row['MarketCode '] == 'Atlanta' and row['PayerCode'] in ['United', 'AetnaMA', 'WellCare']:
       return 'HP Contract'
   elif row['MarketCode '] == 'Kentucky' and row['PayerCode'] in ['Anthem', 'WellCare']:
       return 'HP Contract'
   elif row['MarketCode '] == 'Detroit' and row['PayerCode'] == 'BCBSMI':
       return 'HP Contract'
   elif row['MarketCode '] == 'Houston' and row['PayerCode'] in ['Devoted', 'TexanPlus', 'WellMed', 'WellCare', 'United']:
       return 'HP Contract'
   elif row['MarketCode '] in ['Austin', 'Dallas', 'ElPaso'] and row['PayerCode'] == 'WellMed':
       return 'HP Contract'
   elif row['MarketCode '] == 'SanAntonio' and row['PayerCode'] in ['WellMed', 'WellCare', 'BCBSTX']:
       return 'HP Contract'
   else:
       return ' ' 
    
# Apply the function to create the Contract Status column
df['Contract Status'] = df.apply(determine_contract_status, axis=1)

# Function to convert the date formats
def convert_to_yyyy_mm_dd(date_str):
    if pd.isnull(date_str):
        return date_str
    try:
        return pd.to_datetime(date_str).strftime('%Y-%m-%d')
       # First, attempt to parse the string assuming it's already in 'YYYY-mm-dd' format
        
    except ValueError:
       # If that fails, try parsing it in the 'm/dd/yyyy' format
        return date_str
df['LastImpactableDate'] = df['LastImpactableDate'].apply(convert_to_yyyy_mm_dd)

value = df.iloc[97263,14]
print(value)

