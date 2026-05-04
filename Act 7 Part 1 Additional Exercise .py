import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# [span_5](start_span)Student Personalization[span_5](end_span)
student_name = "Roneilfred O. Saad"
student_id = "TUPM-25-0679"
color_bar = "#91f543" 

# [span_6](start_span)Load and sort data[span_6](end_span)
df = pd.read_csv('spotify_top_1000_tracks.csv')
longest_tracks = df.nlargest(10, 'duration_min')[['track_name', 'artist', 'duration_min']]

# [span_7](start_span)Display Table[span_7](end_span)
print(f"--- Top 10 Longest Tracks for {student_name} ---")
print(longest_tracks.to_string(index=False))

# [span_8](start_span)Visualization[span_8](end_span)
plt.figure(figsize=(10, 6))
sns.barplot(x='duration_min', y='track_name', data=longest_tracks, color=color_bar)
plt.title(f"{student_name} ({student_id})\nTop 10 Longest Spotify Tracks", fontsize=14)
plt.xlabel("Duration (Minutes)")
plt.ylabel("Track Name")
plt.tight_layout()
plt.show()
