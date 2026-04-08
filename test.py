from modules.processor import load_data
df = load_data()
# Print the first 20 rows to verify the column names are updated to lowercase
print(df.head(20))

# Ensure the columns are accessed in lowercase
df['steps'] = df['steps'].fillna(df['steps'].median())
df['sleep_hours'] = df['sleep_hours'].fillna(7.0)  # Example of using updated column name
df['heart_rate_bpm'] = df['heart_rate_bpm'].fillna(68)
df['calories_burned'] = df['calories_burned'].fillna(df['calories_burned'].median())  # Assuming this column exists
df['active_minutes'] = df['active_minutes'].fillna(df['active_minutes'].median())  # Assuming this column exists

# Example of a calculation using the updated column names
df['activity_index'] = df['steps'] / df['active_minutes']  # This line is illustrative
