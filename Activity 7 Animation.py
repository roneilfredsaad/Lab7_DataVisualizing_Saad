import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import os

# 1. Load and Prepare Data (Defines 'df')
try:
    df = pd.read_csv('spotify_top_1000_tracks.csv')
    df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
    df['year'] = df['release_date'].dt.year
    df = df.dropna(subset=['year'])

    # Prepare Yearly Average Popularity
    yearly_pop = df.groupby('year')['popularity'].mean().reset_index()
    yearly_pop = yearly_pop.sort_values('year')
except Exception as e:
    print(f"Error loading data: {e}")

# 2. Initialize the Figure
fig, ax = plt.subplots(figsize=(10,6))
ax.set_xlim(yearly_pop['year'].min(), yearly_pop['year'].max())
ax.set_ylim(0, yearly_pop['popularity'].max() * 1.1)
line, = ax.plot([], [], color='royalblue', linewidth=2.5, label='Avg Popularity')

ax.set_title("Roneilfred O. Saad (TUPM-25-0679)\nEvolution of Track Popularity Over Time", fontsize=14)
ax.set_xlabel("Year of Release")
ax.set_ylabel("Average Popularity")
ax.legend(loc="upper left")

# 3. Animation Function
def animate(i):
    x = yearly_pop['year'][:i]
    y = yearly_pop['popularity'][:i]
    line.set_data(x, y)
    return line,

# 4. Create and Save Animation
ani = FuncAnimation(fig, animate, frames=len(yearly_pop), interval=100, repeat=False)
gif_path = "yearly_popularity_trend.gif"
ani.save(gif_path, writer=PillowWriter(fps=10))

print(f"Animation saved successfully as: {gif_path}")
plt.close(fig)
