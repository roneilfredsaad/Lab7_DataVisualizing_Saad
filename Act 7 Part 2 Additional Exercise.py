import pandas as pd
import matplotlib.pyplot as plt

# Student Information
student_name = "Roneilfred O. Saad"
student_id = "TUPM-25-0679"
# Colors derived from ID 679
color_bar = "#91f543"
color_line = "#4edf9c"

# 1. Load and prepare the dataset
try:
    df = pd.read_csv('spotify_top_1000_tracks.csv')
    df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
    df['year'] = df['release_date'].dt.year
    df = df.dropna(subset=['year'])

    # 2. [span_1](start_span)Group by year and calculate cumulative growth[span_1](end_span)
    yearly_counts = df['year'].value_counts().sort_index().reset_index()
    yearly_counts.columns = ['Year', 'Count']
    yearly_counts['Cumulative'] = yearly_counts['Count'].cumsum()

    # 3. [span_2](start_span)Create the combined bar and line chart[span_2](end_span)
    fig, ax1 = plt.subplots(figsize=(12, 6))

    # Plot Yearly Counts as Bars
    ax1.bar(yearly_counts['Year'], yearly_counts['Count'], color=color_bar, alpha=0.7, label='Yearly Count')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Songs Released (Bars)', color='black')

    # Plot Cumulative Total as a Line on a secondary Y-axis
    ax2 = ax1.twinx()
    ax2.plot(yearly_counts['Year'], yearly_counts['Cumulative'], color=color_line, marker='o', linewidth=2, label='Cumulative Total')
    ax2.set_ylabel('Cumulative Count (Line)', color='black')

    # 4. Final Formatting
    plt.title(f"{student_name} ({student_id})\nSong Release Trend and Cumulative Growth", fontsize=14)
    fig.legend(loc="upper left", bbox_to_anchor=(0.15, 0.85))
    plt.tight_layout()
    plt.show()

except Exception as e:
    print(f"Error: {e}. Ensure 'spotify_top_1000_tracks.csv' is in this folder.")
