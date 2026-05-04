import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# 0. [span_7](start_span)CONFIGURATION & STUDENT INFO[span_7](end_span)
# ==========================================
student_name = "Roneilfred O. Saad"
student_id = "TUPM-25-0679"

# [span_8](start_span)Generate colors from ID[span_8](end_span)
id_num = 679
color1 = f"#{(id_num*7)%256:02x}{(id_num*3)%256:02x}{(id_num*5)%256:02x}" # #91f543
color2 = f"#{(id_num*2)%256:02x}{(id_num*9)%256:02x}{(id_num*4)%256:02x}" # #4edf9c

# Load Dataset
try:
    df = pd.read_csv('spotify_top_1000_tracks.csv')
    # Preprocessing
    df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
    df['release_year'] = df['release_date'].dt.year
    df['decade'] = (df['release_year'] // 10) * 10
    df = df.dropna(subset=['release_year'])
    print("Dataset loaded and preprocessed successfully.")
except Exception as e:
    print(f"Error: {e}. Please ensure 'spotify_top_1000_tracks.csv' is in this folder.")

# ==========================================
# VISUALIZATION TASKS (1-20)
# ==========================================

# 1. [span_9](start_span)Histogram - Song Duration[span_9](end_span)
plt.figure(figsize=(8, 5))
df['duration_min'].plot(kind='hist', bins=30, color=color1, alpha=0.7)
plt.title(f"{student_name} ({student_id})\nHistogram of Song Duration")
plt.xlabel('Duration (min)')
plt.ylabel('Frequency')
plt.show()

# 2. [span_10](start_span)Boxplot - Popularity by Decade[span_10](end_span)
plt.figure(figsize=(10, 5))
sns.boxplot(x='decade', y='popularity', data=df, palette='coolwarm')
plt.title(f"{student_name} ({student_id})\nBoxplot of Popularity by Decade")
plt.show()

# 3. [span_11](start_span)Top 10 Artists by Song Count[span_11](end_span)
plt.figure(figsize=(10, 6))
sns.countplot(y='artist', data=df, order=df['artist'].value_counts().head(10).index, palette='viridis')
plt.title(f"{student_name} ({student_id})\nTop 10 Artists by Song Count")
plt.show()

# 4. [span_12](start_span)Ridge Style Plot (Violin Plot)[span_12](end_span)
plt.figure(figsize=(10, 6))
sns.violinplot(data=df, x='duration_min', y='decade', palette='coolwarm', orient='h')
plt.title(f"{student_name} ({student_id})\nRidge Style Plot by Decade")
plt.show()

# 5. [span_13](start_span)Average Popularity per Decade[span_13](end_span)
plt.figure(figsize=(8, 5))
avg_pop = df.groupby('decade')['popularity'].mean()
avg_pop.plot(kind='line', color=color1, marker='o')
plt.title(f"{student_name} ({student_id})\nAverage Popularity per Decade")
plt.xlabel('Decade')
plt.ylabel('Average Popularity')
plt.grid(True)
plt.show()

# 6. [span_14](start_span)Number of Songs Over Time (Area Plot)[span_14](end_span)
plt.figure(figsize=(8, 5))
count_by_year = df['release_year'].value_counts().sort_index()
count_by_year.plot(kind='area', color=color2, alpha=0.7)
plt.title(f"{student_name} ({student_id})\nNumber of Songs Over Time")
plt.xlabel('Year')
plt.ylabel('Count')
plt.show()

# 7. [span_15](start_span)Popularity vs Duration per Decade[span_15](end_span)
g = sns.FacetGrid(df, col='decade', col_wrap=4, height=3)
g.map_dataframe(sns.scatterplot, x='duration_min', y='popularity', color=color1)
g.fig.suptitle(f"{student_name} ({student_id})\nPopularity vs Duration per Decade", y=1.02)
plt.show()

# 8. [span_16](start_span)Top 10 Longest Songs (Stem Plot)[span_16](end_span)
plt.figure(figsize=(12, 6))
longest = df.nlargest(10, 'duration_min')
plt.stem(longest['track_name'], longest['duration_min'], linefmt='#888888', markerfmt='o', basefmt=" ")
plt.xticks(rotation=45, ha='right')
plt.title(f"{student_name} ({student_id})\nTop 10 Longest Songs")
plt.ylabel('Duration (min)')
plt.tight_layout()
plt.show()

# 9. [span_17](start_span)Average Duration: Top 5 Artists (Dot Chart)[span_17](end_span)
plt.figure(figsize=(8, 5))
avg_duration = df.groupby('artist')['duration_min'].mean().nlargest(5)
plt.plot(avg_duration.values, avg_duration.index, 'o', color=color2)
plt.title(f"{student_name} ({student_id})\nAverage Duration: Top 5 Artists")
plt.xlabel('Duration (min)')
plt.grid(True)
plt.show()

# 10. [span_18](start_span)Top 3 Artists by Decade (Stacked Bar)[span_18](end_span)
crosstab = pd.crosstab(df['decade'], df['artist'])
top3 = df['artist'].value_counts().head(3).index
crosstab[top3].plot(kind='bar', stacked=True, colormap='coolwarm', figsize=(10, 5))
plt.title(f"{student_name} ({student_id})\nTop 3 Artists by Decade")
plt.ylabel('Number of Songs')
plt.show()

# 11. [span_19](start_span)Top 10 Tracks by Popularity[span_19](end_span)
plt.figure(figsize=(10, 6))
top_tracks = df.nlargest(10, 'popularity') # Fixed typo from PDF
plt.barh(top_tracks['track_name'], top_tracks['popularity'], color=color1)
plt.xlabel('Popularity')
plt.title(f"{student_name} ({student_id})\nTop 10 Tracks by Popularity")
plt.gca().invert_yaxis()
plt.show()

# 12. [span_20](start_span)Duration Spread of Top Artists[span_20](end_span)
plt.figure(figsize=(10, 6))
top_artists = df['artist'].value_counts().head(3).index
sns.stripplot(data=df[df['artist'].isin(top_artists)], x='artist', y='duration_min', palette=['#8C1515', '#888888'])
plt.title(f"{student_name} ({student_id})\nDuration of Top Artists")
plt.show()

# 13. [span_21](start_span)Top 5 Albums Distribution[span_21](end_span)
plt.figure(figsize=(8, 8))
top_albums = df['album'].value_counts().head(5)
colors = ['#8C1515', color1, '#888888', color2, '#666666']
plt.pie(top_albums, labels=top_albums.index, autopct='%1.1f%%', colors=colors)
plt.title(f"{student_name} ({student_id})\nTop 5 Albums Distribution")
plt.show()

# 14. [span_22](start_span)Hierarchical Clustering of Features[span_22](end_span)
numerical_cols = ['popularity', 'duration_min']
df_numeric = df[numerical_cols].dropna()
sns.clustermap(df_numeric.corr(), annot=True, cmap='viridis', linewidths=.75, figsize=(6, 6))
plt.suptitle(f"{student_name} ({student_id})\nHierarchical Clustering of Features")
plt.show()

# 15. [span_23](start_span)Pair Plot of Key Attributes[span_23](end_span)
sns.pairplot(df[['duration_min', 'popularity', 'release_year']], diag_kind='kde')
plt.suptitle(f"{student_name} ({student_id})\nPair Plot of Key Attributes", y=1.02)
plt.show()

# 16. [span_24](start_span)Songs Released per Year[span_24](end_span)
plt.figure(figsize=(12, 5))
df['release_year'].value_counts().sort_index().plot(kind='bar', color=color2)
plt.title(f"{student_name} ({student_id})\nSongs Released per Year")
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.show()

# 17. [span_25](start_span)Swarm Plot of Artist Popularity[span_25](end_span)
plt.figure(figsize=(12, 6))
sns.swarmplot(data=df.head(50), x='artist', y='popularity', palette='coolwarm')
plt.title(f"{student_name} ({student_id})\nSwarm Plot of Artist Popularity (Sample 50)")
plt.xticks(rotation=45)
plt.show()

# 18. [span_26](start_span)Hexbin Plot of Duration vs Popularity[span_26](end_span)
plt.figure(figsize=(8, 6))
plt.hexbin(df['duration_min'], df['popularity'], gridsize=20, cmap='coolwarm', alpha=0.7)
plt.xlabel('Duration (min)')
plt.ylabel('Popularity')
plt.title(f"{student_name} ({student_id})\nHexbin Plot of Duration vs Popularity")
plt.colorbar(label='Count')
plt.show()

# 19. [span_27](start_span)ECDF of Song Duration[span_27](end_span)
plt.figure(figsize=(8, 5))
sns.ecdfplot(data=df, x='duration_min', color=color1)
plt.title(f"{student_name} ({student_id})\nECDF of Song Duration")
plt.xlabel('Duration (min)')
plt.ylabel('Cumulative Probability')
plt.show()

# 20. [span_28](start_span)Avg Popularity by Decade and Top Artists[span_28](end_span)
avg_artist_decade = df.groupby(['decade', 'artist'])['popularity'].mean().unstack().fillna(0)
top3 = df['artist'].value_counts().head(3).index
avg_artist_decade[top3].plot(kind='bar', figsize=(10, 5))
plt.title(f"{student_name} ({student_id})\nAverage Popularity by Decade and Top Artists")
plt.ylabel('Average Popularity')
plt.show()
