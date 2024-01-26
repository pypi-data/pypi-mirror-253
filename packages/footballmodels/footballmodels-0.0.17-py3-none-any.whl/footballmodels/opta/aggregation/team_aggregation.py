import pandas as pd
from footballmodels.opta import actions as A


def get_team_match_data(data):
    data["attack"] = A.open_play_xg(data)
    data["set_piece_xg"] = A.set_piece_xg(data)
    data["ppda_qualifying_passes"] = A.ppda_qualifying_passes(data)
    data["ppda_qualifying_defensive_actions"] = A.ppda_qualifying_defensive_actions(data)
    data["box_efficiency"] = A.non_penalty_goal(data) - A.non_penalty_xg(data)
    data["physical_duels"] = A.ground_duels_won(data) + A.aerial_duels_won(data)
    data["touch"] = A.touch(data)
    data["shots"] = A.open_play_shot(data)
    data["counterattack_shots"] = A.counterattack_shot(data)
    data["attacking_touches"] = A.touch(data) & (data["x"] >= 66.6)
    for_data = (
        data.groupby(["season", "competition", "matchId", "team", "teamId"])
        .agg(
            {
                "attack": "sum",
                "ppda_qualifying_defensive_actions": "sum",
                "set_piece_xg": "sum",
                "box_efficiency": "sum",
                "physical_duels": "sum",
                "touch": "sum",
                "shots": "sum",
                "counterattack_shots": "sum",
                "attacking_touches": "sum",
            }
        )
        .reset_index()
    )

    against_data = (
        data.groupby(
            [
                "season",
                "competition",
                "matchId",
                "opponent",
            ]
        )
        .agg(
            {
                "attack": "sum",
                "ppda_qualifying_passes": "sum",
                "set_piece_xg": "sum",
                "box_efficiency": "sum",
                "touch": "sum",
                "attacking_touches": "sum",
            }
        )
        .reset_index()
    )

    against_data["defense"] = against_data["attack"]
    against_data = against_data.drop(columns=["attack"])
    merged_data = pd.merge(
        for_data[
            [
                "season",
                "competition",
                "matchId",
                "team",
                "teamId",
                "attack",
                "ppda_qualifying_defensive_actions",
                "set_piece_xg",
                "box_efficiency",
                "physical_duels",
                "touch",
                "shots",
                "counterattack_shots",
                "attacking_touches",
            ]
        ],
        against_data[
            [
                "season",
                "competition",
                "matchId",
                "opponent",
                "defense",
                "ppda_qualifying_passes",
                "set_piece_xg",
                "box_efficiency",
                "touch",
                "attacking_touches",
            ]
        ],
        left_on=["season", "competition", "matchId", "team"],
        right_on=["season", "competition", "matchId", "opponent"],
        how="left",
        suffixes=("_for", "_against"),
    )
    merged_data = merged_data.drop(columns=["opponent"])
    merged_data["set_piece"] = merged_data["set_piece_xg_for"] - merged_data["set_piece_xg_against"]
    merged_data["box_efficiency"] = merged_data["box_efficiency_for"] - merged_data["box_efficiency_against"]
    return merged_data
