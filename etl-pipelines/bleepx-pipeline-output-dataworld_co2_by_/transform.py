import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

# Use the SQL result if it exists, otherwise the original raw CSV
input_csv = sql_result if 'sql_result' in globals() and sql_result else raw_csv
df = pd.read_csv(StringIO(input_csv))

# Columns available: country_name, min_kt, max_kt, growth_kt

# Derived column example
df['scaled_min_kt'] = df['min_kt'] * 2
df['min_kt_per_max_kt'] = df['min_kt'] / df['max_kt'].replace(0, float('nan'))

# Filter to above-average rows
df = df[df['min_kt'] >= df['min_kt'].mean()]

# Aggregate and plot (the figure is captured automatically)
summary = df.groupby('country_name')['min_kt'].mean()
summary.plot(kind='bar')

# Print the final CSV so it can continue to S3
print(df.to_csv(index=False))