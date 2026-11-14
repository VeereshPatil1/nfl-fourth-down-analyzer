import nflreadpy as nfl

# Download every play from the 2025 season (returns a Polars DataFrame),
# then convert it to pandas, which we already know how to use
pbp = nfl.load_pbp([2025]).to_pandas()

# (rows, columns): how big is this thing?
print(pbp.shape)
# Count how many rows have each value in the "down" column.
# dropna=False also counts missing values (NaN), which pandas hides by default
print(pbp["down"].value_counts(dropna=False))
fourth = pbp[pbp['down'] == 4.0] 
print(len(fourth))
print(fourth["play_type"].value_counts(dropna=False))
print(fourth[['ydstogo', 'yardline_100', 'score_differential', 'game_seconds_remaining', 'play_type', 'fourth_down_converted']].head())
went_for_it = fourth[fourth['play_type'].isin(['run', 'pass'])]
print(went_for_it['fourth_down_converted'].mean())
