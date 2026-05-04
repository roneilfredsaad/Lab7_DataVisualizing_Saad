import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# [span_16](start_span)Student Personalization[span_16](end_span)
student_name = "Roneilfred O. Saad"
student_id = "TUPM-25-0679"
cmap_color = "viridis"

# [span_17](start_span)Data Prep[span_17](end_span)
df = pd.read_csv('spotify_top_1000_tracks.csv')
df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
df['year'] = df['release_date'].dt.year
df = df.dropna(subset=['year', 'duration_min', 'popularity'])
years = sorted(df['year'].unique())

# [span_18](start_span)Animation Init[span_18](end_span)
fig, ax = plt.subplots(figsize=(10, 7))

def update(frame_year):
    ax.clear()
    data_subset = df[df['year'] <= frame_year]
    
    # [span_19](start_span)[span_20](start_span)Hexbin Density Map[span_19](end_span)[span_20](end_span)
    hb = ax.hexbin(data_subset['duration_min'], data_subset['popularity'], 
                   gridsize=25, cmap=cmap_color, mincnt=1)
    
    ax.set_title(f"{student_name} ({student_id})\nDensity of Concentration up to {int(frame_year)}")
    ax.set_xlabel("Duration (min)")
    ax.set_ylabel("Popularity Score")
    ax.set_xlim(df['duration_min'].min(), df['duration_min'].max())
    ax.set_ylim(0, 105)
    return hb,

# [span_21](start_span)Save as GIF[span_21](end_span)
ani = FuncAnimation(fig, update, frames=years, repeat=False)
ani.save("exercise_3_density.gif", writer=PillowWriter(fps=5))
print("Exercise 3 animation saved as exercise_3_density.gif")
plt.close()
