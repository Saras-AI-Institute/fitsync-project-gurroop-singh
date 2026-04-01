import pandas as pd
from datetime import datetime


def load_data():
    """
    Load health data from a CSV file, handle missing values, and convert date column.
    Returns a cleaned pandas DataFrame.
    """
    # Read the CSV file
    file_path = 'data/health_data.csv'
    data = pd.read_csv(file_path)
    
    # Fill missing values intelligently
    # Fill missing 'steps' with the median value of the column
    if 'steps' in data.columns:
        median_steps = data['steps'].median()
        data['steps'].fillna(median_steps, inplace=True)

    # Fill missing 'Sleep_Hours' with 7.0
    if 'Sleep_Hours' in data.columns:
        data['Sleep_Hours'].fillna(7.0, inplace=True)

    # Fill missing 'Heart_Rate_Bpm' with 68
    if 'Heart_Rate_Bpm' in data.columns:
        data['Heart_Rate_Bpm'].fillna(68, inplace=True)

    # Fill missing values in all other columns with their respective median
    for column in data.columns:
        if column not in ['steps', 'Sleep_Hours', 'Heart_Rate_Bpm', 'date']:
            median_value = data[column].median()
            data[column].fillna(median_value, inplace=True)

    # Convert 'date' column to datetime objects
    if 'date' in data.columns:
        data['date'] = pd.to_datetime(data['date'], errors='coerce')

    return data


def calculate_recover_score(df):
    """
    Calculate and add a new column 'Recovery_Score' to the DataFrame, reflecting body recovery status (0 to 100).
    """
    scores = []
    for index, row in df.iterrows():
        # Start with a neutral score
        score = 50

        # Adjust based on Sleep_Hours
        if row['Sleep_Hours'] >= 7:
            score += 20  # Good sleep
        elif row['Sleep_Hours'] < 6:
            score -= 20  # Poor sleep

        # Adjust based on Heart_Rate_Bpm (lower is better)
        if 50 <= row['Heart_Rate_Bpm'] <= 95:
            if row['Heart_Rate_Bpm'] < 60:
                score += 10
            elif row['Heart_Rate_Bpm'] > 80:
                score -= 10

        # Adjust based on Steps (higher is generally good, but very high can be straining)
        if 4000 <= row['steps'] <= 16000:
            if row['steps'] < 10000:
                score += 10  # Moderate activity is positive
            else:
                score -= 5   # High activity might lead to slight reduction due to strain

        # Ensure the score is within the 0-100 range
        score = max(0, min(100, score))
        scores.append(score)

    # Add 'Recovery_Score' column to the DataFrame
    df['Recovery_Score'] = scores
    return df

