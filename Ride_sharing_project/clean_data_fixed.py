import pandas as pd

# Load the file
df = pd.read_csv('ncr_ride_bookings.csv')

# Remove rows where Avg VTAT is missing
df = df.dropna(subset=['Avg VTAT'])

# Create Total Fare column
df['Total Fare'] = df['Avg CTAT'] + df['Avg VTAT']

# Fix date format - using dayfirst=True fixes the mixed date issue!
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

# Save the cleaned file
df.to_csv('cleaned_rides.csv', index=False)

print("✅ SUCCESS! cleaned_rides.csv has been created!")