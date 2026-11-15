import nflreadpy as nfl

SEASONS = list(range(2021, 2026))
COLUMNS = [
    "game_id", "play_id", "season", "week", "season_type",
    "posteam", "defteam", "home_team", "away_team", "home_coach", "away_coach",
    "down", "ydstogo", "yardline_100", "qtr", "game_seconds_remaining", "score_differential",
    "play_type", "fourth_down_converted", "desc"]
DECISIONS = {
    "run": "go_for_it",
    "pass": "go_for_it",
    "punt": "punt",
    "field_goal": "field_goal"}

pbp = nfl.load_pbp(SEASONS).to_pandas()
pbp = pbp[COLUMNS]
fourth = pbp[pbp['down'] == 4.0]
fourth = fourth[fourth["play_type"].isin(["run", "pass", "punt", "field_goal"])]
fourth["decision"] = fourth["play_type"].map(DECISIONS)
print(fourth["decision"].value_counts())