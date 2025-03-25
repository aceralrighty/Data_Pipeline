import pandas as pd

# From CSV
df_csv = pd.read_csv('data.csv')

# From JSON
df_json = pd.read_json('data.json')

# From SQL database
from sqlalchemy import create_engine
engine = create_engine('postgresql://user:password@host:3306/database')
df_sql = pd.read_sql_query('SELECT * FROM raw_data', engine)
# Data Cleaning
pd['column_name'].fillna(0, inplace=True) # Handle missing values
pd.drop_duplicates(inplace=True) # Remove duplicates

# Data Transformation
pd['new_column'] = pd['column1'] + pd['column2'] # Create new columns
pd['date_column'] = pd.to_datetime(pd['date_column']) # Convert data types

pd.to_csv('cleaned_data.csv', index=False)
pd.to_sql('cleaned_data', engine)