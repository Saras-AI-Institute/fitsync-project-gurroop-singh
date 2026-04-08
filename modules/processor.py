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
    
    # Standardize the DataFrame column names to lower case
    data.columns = [column.lower() for column in data.columns]

    # Fill missing values intelligently
    # Fill missing 'steps' with the median value of the column
    if 'steps' in data.columns:
        median_steps = data['steps'].median()
        data['steps'].fillna(median_steps, inplace=True)

    # Fill missing 'sleep_hours' with 7.0
    if 'sleep_hours' in data.columns:
        data['sleep_hours'].fillna(7.0, inplace=True)

    # Fill missing 'heart_rate_bpm' with 68
    if 'heart_rate_bpm' in data.columns:
        data['heart_rate_bpm'].fillna(68, inplace=True)
    # Fill missing values in all other columns with their respective median
    for column in data.columns:
        if column not in ['steps', 'sleep_hours', 'heart_rate_bpm', 'date']:
            median_value = data[column].median()
            data[column].fillna(median_value, inplace=True)

    # Convert 'date' column to datetime objects
    if 'date' in data.columns:
        data['date'] = pd.to_datetime(data['date'], errors='coerce')

    return data


def calculate_recovery_score(df):
    """
    Calculate and add a new column 'recovery_score' to the DataFrame, reflecting body recovery status (0 to 100).
    """
    scores = []
    for index, row in df.iterrows():
        # Start with a neutral score
        score = 50

        # Adjust based on Sleep_Hours
        if row['sleep_hours'] >= 7:
            score += 20  # Good sleep
        elif row['sleep_hours'] < 6:
            score -= 20  # Poor sleep

        # Adjust based on Heart_Rate_Bpm (lower is better)
        if 50 <= row['heart_rate_bpm'] <= 95:
            if row['heart_rate_bpm'] < 60:
                score += 10
            elif row['heart_rate_bpm'] > 80:
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

    # Add 'recovery_score' column to the DataFrame
    df['recovery_score'] = scores
    return df


def process_data():
    """
    Main function to process health data for the Streamlit dashboard.
    It loads, calculates recovery scores, and returns the processed DataFrame.
    """
    # Load the cleaned data
    df = load_data()

    # Calculate the recovery score
    df = calculate_recovery_score(df)  # Corrected function name

    # Return the final processed DataFrame
    return df

