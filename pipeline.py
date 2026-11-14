import nflreadpy as nfl

SEASONS = list(range(2021, 2026))
COLUMNS = [
    "game_id", "play_id", "season", "week", "season_type",
    "posteam", "defteam", "home_team", "away_team", "home_coach", "away_coach",
    "down", "ydstogo", "yardline_100", "qtr", "game_seconds_remaining", "score_differential",
    "play_type", "fourth_down_converted", "desc"]

pbp = nfl.load_pbp(SEASONS).to_pandas()
pbp = pbp[COLUMNS]
print(pbp.shape)