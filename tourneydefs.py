import uuid
from pydantic import BaseModel, Field
from typing import Text, List, Dict, Optional
from uuid import uuid4
import os
import json
import logging
import errno

class Team(BaseModel):
    id: str = ""
    name: str = ""
    tricode: str = ""
    points: int = 0
    logo_big: str = ""
    logo_small: str = ""

    def to_dict(self, state=False):
        if state:
            return self.__dict__
        else:
            dict_to_return = self.__dict__
            dict_to_return.pop("points")
            return dict_to_return

    def get_name(self):
        if self.name:
            return self.name
        else:
            return self.tricode
        
    def get_tricode(self):
        if self.tricode:
            return self.tricode
        else:
            return self.name

    def get_display_name(self):
        if self.tricode and not self.name:
            return self.tricode
        elif self.name and not self.tricode:
            return self.name
        else:
            return f"{self.tricode}: {self.name}"


class Match(BaseModel):
    id: str = str(uuid4())
    teams: List[str] = []
    scores: List[int] = [0, 0]
    best_of: int = 1
    finished: bool = False
    in_progress: bool = False
    winner: int = 2

    def to_dict(self, state=False):
        if state:
            return self.__dict__
        else:
            dict_to_return = self.__dict__
            dict_to_return.pop("scores")
            dict_to_return.pop("finished")
            dict_to_return.pop("in_progress")
            dict_to_return.pop("winner")
            return dict_to_return

class Game(BaseModel):
    match: str = ""
    winner: int = 3
    scores: List[int] = [0, 0]

    def to_dict(self):
        return self.__dict__

class Tournament(BaseModel):
    def load_from(self, filename="tournament-config.json"):
        try:
            with open(filename) as f:
                data = json.load(f)

                self.mapping = {}
                self.clear_everything()

                for team in data["teams"]:
                    team = Team(**team)
                    if team.id != "666":
                        id = self.add_team(team)
                        self.mapping[team.tricode] = id

                for current_match in data["matches"]:
                    match = Match(**current_match)
                    self.add_match(match, schedule=False)

                self.schedule = data.get("schedule", [])

                game_history = data.get("game_history")
                if game_history is not None:
                    for game in game_history:
                        game = Game(**game)
                        self.game_history.append(game)
                current_match = data.get("current_match")
                if current_match is not None:
                    self.current_match = current_match
        except:
            return False
        return True
    
    def update_match_history_from_challonge(self, tournamentinfo):
        self.game_history = []
        for round_index, round_match_list in tournamentinfo["matches_by_round"].items():
            for match in round_match_list:
                if match["state"] == "complete":
                    match_id = str(match["id"])
                    scheduleid = self.get_scheduleid_from_match_id(match_id)
                    self.matches[match_id].scores = [0, 0]
                    if match["winner_id"] == match["player1"]["id"]:
                        # reset best_of and scores
                        self.matches[match_id].best_of = (match["scores"][0] * 2) - 1
                        # process index 1 first
                        match_count = match["scores"][1]
                        while match_count > 0:
                            self.game_complete(scheduleid, 1)
                            match_count -= 1
                        match_count = match["scores"][0]
                        while match_count > 0:
                            self.game_complete(scheduleid, 0)
                            match_count -= 1
                    else:
                        self.matches[match_id].best_of = (match["scores"][1] * 2) - 1
                        match_count = match["scores"][0]
                        while match_count > 0:
                            self.game_complete(scheduleid, 0)
                            match_count -= 1
                        match_count = match["scores"][1]
                        while match_count > 0:
                            self.game_complete(scheduleid, 1)
                            match_count -= 1
                        # process index 0 first

        for round_index, round_match_list in tournamentinfo["matches_by_round"].items():
            for match in round_match_list:
                if match["state"] == "pending":
                    for match_id, our_match in enumerate(self.matches):
                        if our_match.id == match["id"]:
                            if match.get("player1"):
                                self.matches[match_id][0] == match["player1"]["id"]
                            if match.get("player2"):
                                self.matches[match_id][1] == match["player1"]["id"]


    def load_from_challonge(self, tournamentinfo):
        self.mapping = {}
        self.clear_everything()
        logging.debug("loading teams")
        round_bestof_mapping = {}
        try:
            for round_index, round in enumerate(tournamentinfo["rounds"]):
                round_bestof_mapping[round["number"]] = round["best_of"]

            for round_index, round_match_list in tournamentinfo["matches_by_round"].items():
                for match in round_match_list:
                    teams = []
                    if match.get("player1") and match.get("player2"):
                        teams.append(match["player1"])
                        teams.append(match["player2"])
                    for team in teams:
                        if team["id"] not in self.teams.keys():
                            logging.debug(f"found new team with id {team['id']}")
                            new_team = Team()
                            new_team.name = team["display_name"]
                            new_team.id = team["id"]
                            new_team.tricode = team["display_name"][0:3].upper()
                            self.mapping[new_team.tricode] = new_team.id
                            self.add_team(new_team)

            # load in completed matches
            for round_index, round_match_list in tournamentinfo["matches_by_round"].items():
                for match in round_match_list:
                    if match["state"] == "complete":
                        new_match = Match()
                        new_match.id = str(match["id"])
                        new_match.teams.append(self.teams[match["player1"]["id"]].id)
                        new_match.teams.append(self.teams[match["player2"]["id"]].id)
                        new_match.best_of = round_bestof_mapping[match["round"]]
                        self.matches[new_match.id] = new_match
                        self.schedule.append(new_match.id)

            # create match history for them
            # TODO: update this for match/schedule split
            self.update_match_history_from_challonge(tournamentinfo)

            # add the upcoming matches where teams are locked in
            for round_index, round_match_list in tournamentinfo["matches_by_round"].items():
                for match in round_match_list:
                    if match["state"] == "open":
                        new_match = Match()
                        new_match.id = str(match["id"])
                        new_match.teams.append(self.teams[match["player1"]["id"]].id)
                        new_match.teams.append(self.teams[match["player2"]["id"]].id)
                        new_match.best_of = round_bestof_mapping[match["round"]]
                        self.matches[new_match.id] = new_match
                        self.schedule.append(new_match.id)

            # add the upcoming matches where teams are not locked in
            for round_index, round_match_list in tournamentinfo["matches_by_round"].items():
                for match in round_match_list:
                    if match["state"] == "pending":
                        new_match = Match()
                        new_match.id = str(match["id"])
                        if match.get("player1"):
                            new_match.teams.append(self.teams[match["player1"]["id"]].id)
                        else:
                            new_match.teams.append(self.teams[self.get_team_id_by_tricode("TBD")])
                        if match.get("player2"):
                            new_match.teams.append(self.teams[match["player2"]["id"]].id)
                        else:
                            new_match.teams.append(self.teams[self.get_team_id_by_tricode("TBD")])
                        self.matches[new_match.id] = new_match
                        self.schedule.append(new_match.id)
        except:
            return False

        return True
    

    def save_to(self, filename, savestate=False):
        # do write here
        output_dict = {}
        output_dict["teams"] = []

        for id, team in self.teams.items():
            if team.id != "666":
                output_dict["teams"].append(team.to_dict(savestate))

        output_dict["matches"] = []
        for id, match in self.matches.items():
            output_dict["matches"].append(match.to_dict(savestate))

        output_dict["schedule"] = self.schedule

        if savestate:
            output_dict["current_match"] = self.current_match
            output_dict["game_history"] = []
            for game in self.game_history:
                output_dict["game_history"].append(game.to_dict())
        
        
        with open(filename, "w") as f:
            json.dump(output_dict, f)
        return

    def write_to_stream(self, swap=False):
        # do text write here
        filename = "streamlabels/start.txt"
        if not os.path.exists(os.path.dirname(filename)):
            try:
                os.makedirs(os.path.dirname(filename))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise

        if len(self.schedule):
            for index, schedule_item in enumerate(self.schedule):
                match = self.matches[schedule_item]
                with open(f"streamlabels\match-{index}-teams.txt", "w") as f_teams:
                    team1 = self.teams.get(match.teams[0])
                    team2 = self.teams.get(match.teams[1])
                    f_teams.write(f"{team1.get_name()}\n")
                    f_teams.write(f"{team2.get_name()}\n")

                with open(f"streamlabels\match-{index}-tricodes.txt", "w") as f_teams:
                    team1 = self.teams.get(match.teams[0])
                    team2 = self.teams.get(match.teams[1])
                    f_teams.write(f"{team1.get_tricode()}\n")
                    f_teams.write(f"{team2.get_tricode()}\n")

                with open(f"streamlabels\match-{index}-scores.txt", "w") as f_scores:
                    f_scores.write(f"{match.scores[0]}\n")
                    f_scores.write(f"{match.scores[1]}\n")
            
            current_match = self.current_match if self.current_match < len(self.schedule) else self.current_match - 1
            current_teams = self.get_teams_from_scheduleid(current_match)
            match = self.get_match_from_scheduleid(current_match)
            if current_teams is not None:
                t0 = 0
                t1 = 1
                if swap:
                    t0 = 1
                    t1 = 0
                with open(f"streamlabels\current-match-teams.txt", "w") as f_current:
                    f_current.write(f"{current_teams[0].get_name()} vs {current_teams[1].get_name()}\n")
                    f_current.close()
                
                with open(f"streamlabels\current-match-tricodes.txt", "w") as f_current:
                    f_current.write(f"{current_teams[0].get_tricode()} vs {current_teams[1].get_tricode()}\n")
                    f_current.close()

                with open(f"streamlabels\current-match-team1-tricode.txt", "w") as f_current:
                    f_current.write(f"{current_teams[t0].get_tricode()}\n")

                with open(f"streamlabels\current-match-team2-tricode.txt", "w") as f_current:
                    f_current.write(f"{current_teams[t1].get_tricode()}\n")
                
                with open(f"streamlabels\current-match-team1-name.txt", "w") as f_current:
                    f_current.write(f"{current_teams[t0].get_name()}\n")

                with open(f"streamlabels\current-match-team2-name.txt", "w") as f_current:
                    f_current.write(f"{current_teams[t1].get_name()}\n")

                with open(f"streamlabels\current-match-team1-score.txt", "w") as f_current:
                    f_current.write(f"{match.scores[t0]}\n")

                with open(f"streamlabels\current-match-team2-score.txt", "w") as f_current:
                    f_current.write(f"{match.scores[t1]}\n")
            
            standings = self.get_standings()
            if standings:
                with open(f"streamlabels\standings-complete.txt", "w") as f_current:
                    for result in standings:
                        team = self.teams[result[0]]
                        f_current.write(f"{team.get_name()}: {result[1]}\n")
                    f_current.close()

                with open(f"streamlabels\standings-teams-names.txt", "w") as f_current:
                    for result in standings:
                        team = self.teams[result[0]]
                        f_current.write(f"{team.get_name()}\n")
                    f_current.close()

                with open(f"streamlabels\standings-teams-tricodes.txt", "w") as f_current:
                    for result in standings:
                        team = self.teams[result[0]]
                        f_current.write(f"{team.get_tricode()}\n")
                    f_current.close()

                with open(f"streamlabels\standings-teams-points.txt", "w") as f_current:
                    for result in standings:
                        team = self.teams[result[0]]
                        f_current.write(f"{result[1]}\n")
                    f_current.close()

                with open(f"streamlabels\standings-teams-leader.txt", "w") as f_current:
                    result = standings[0]
                    team = self.teams[result[0]]
                    f_current.write(f"{team.get_name()}")
                    f_current.close()

        return
    
    def update_match_scores(self):
        self.current_match = 0
        for match_id in self.matches.keys():
            self.matches[match_id].scores = [0, 0]
            self.matches[match_id].winner = 2
            self.matches[match_id].finished = False
            self.matches[match_id].in_progress = False
        for game in self.game_history:
            scheduleid = self.get_scheduleid_from_match_id(game.match)
            self.process_game(scheduleid, game.winner)


    def process_game(self, scheduleid, winner_index):
        match_id = self.get_match_id_from_scheduleid(scheduleid)
        cutoff = self.matches[match_id].best_of / 2
        self.matches[match_id].scores[winner_index] += 1
        self.matches[match_id].in_progress = True
        if self.matches[match_id].scores[0] > cutoff or self.matches[match_id].scores[1] > cutoff:
            self.matches[match_id].in_progress = False
            self.matches[match_id].finished = True
            self.matches[match_id].winner = winner_index
            self.teams[self.matches[match_id].teams[winner_index]].points += 1
            self.current_match += 1

    def game_complete(self, scheduleid, winner_index):
        self.process_game(scheduleid, winner_index)
        match_id = self.get_match_id_from_scheduleid(scheduleid)
        finished_game = Game(match = match_id, winner=winner_index)
        self.game_history.append(finished_game)


    def get_standings(self):
        standings = []
        for id, team in self.teams.items():
            if team.id != "666":
                standings.append((team.id, team.points))
        actual_standings = sorted(standings, key=lambda y:y[1], reverse=True)
        return actual_standings

    ## TEAM READ/WRITE/EDIT
    def add_team(self, team_to_add, callback = None):
        if not team_to_add.id:
            new_team_id = str(uuid4())
            team_to_add.id = new_team_id
        self.teams[team_to_add.id] = team_to_add
        return team_to_add.id


    def edit_team(self, update):
        self.teams[update.id] = update


    def delete_team(self, id):
        # delete any matches they have

        for i, schedule_item in reversed(list(enumerate(self.schedule))):
            match = self.get_match_from_scheduleid(schedule_item)
            if id in match.teams or self.teams[id].tricode in match.teams:
                self.matches.pop(match.id)
                del(self.schedule[i])
        self.teams.pop(id)


    ## MATCH READ/WRITE/EDIT
    def add_match(self, match, schedule=True):
        if not match.id:
            match.id = str(uuid.uui4())
        self.matches[match.id] = match
        if schedule:
            self.schedule.append(str(match.id))

    def delete_match(self, match_id):
        self.matches.pop(match_id)
        scheduleid = self.get_scheduleid_from_match_id(match_id)
        del(self.schedule[scheduleid])
        for i, game in reversed(list(enumerate(self.game_history))):
            if game.match == match_id:
                del(self.game_history[i])

    def edit_match(self, match_id, match):
        self.matches[match_id].teams = match.teams
        self.matches[match_id].best_of = match.best_of

    def get_team_id_by_tricode(self, tricode):
        for key, team in self.teams.items():
            if team.tricode == tricode:
                return key
        return None

    ## HELPER FUNCTIONS
    def get_teams_from_scheduleid(self, id):
        try:    
            match_id = self.schedule[id]
            team1 = self.teams[self.matches[match_id].teams[0]]
            team2 = self.teams[self.matches[match_id].teams[1]]
            return [team1, team2]
        except IndexError:
            return None

    def get_scheduleid_from_match_id(self, match_id):
        return self.schedule.index(match_id)

    def swap_matches(self, scheduleid1, scheduleid2):
        temp_value = self.schedule[scheduleid1]
        self.schedule[scheduleid1] = self.schedule[scheduleid2]
        self.schedule[scheduleid2] = temp_value
    
    def get_current_match(self):
        return self.get_match_from_scheduleid(self.current_match)

    def get_match_id_from_scheduleid(self, scheduleid):
        match_id = self.schedule[scheduleid]
        return self.matches[match_id].id

    def get_match_from_scheduleid(self, scheduleid):
        match_id = self.schedule[scheduleid]
        return self.matches[match_id]

    def clear_everything(self):
        self.teams = {}
        self.add_team(self.placeholder_team)
        self.matches = {}
        self.schedule = []
        self.game_history = []
        self.current_match = 0
        self.mapping = {}

    placeholder_team = Team(tricode="TBD", name = "TBD", id="666")
    teams: Dict = {}
    matches: List[Match] = []
    schedule: List[str] = []
    current_match: int = 0
    game_history: List[Game] = []
    mapping: Dict = {}