
import pandas as pd

# Load the dataset
data = pd.read_csv("raw_data.csv")  # Replace with your actual raw dataset path

# Standardize text formats
data['Gender'] = data['Gender'].str.capitalize()

# Handle missing values
data['Age'] = data['Age'].fillna(data['Age'].median())

# Convert date formats
data['Join Date'] = pd.to_datetime(data['Join Date'], format='%d/%m/%Y', errors='coerce')

# Remove duplicates
data = data.drop_duplicates()

# Clean column names
data.columns = data.columns.str.lower().str.replace(' ', '_')

# Save cleaned data
data.to_csv("cleaned_data.csv", index=False)
print("Data cleaning completed and saved to 'cleaned_data.csv'")
