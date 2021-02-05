import { Team } from "../types/team";
import axios from "axios";

const convertResultToTeams = (res: any): Array<Team> => {
  return res.data.map((team: Team) => new Team(team));
};

export const getTeams = (): Promise<Array<Team>> => {
  return axios.get("/api/teams/").then(convertResultToTeams);
};

export const addTeamApi = (name: string, info: string): Promise<any> => {
  return axios.post("/api/teams/", {
    name: name,
    info: info,
  });
};

export const updateTeamApi = (team: Team): Promise<any> => {
  return axios.put(`/api/teams/${team.id}/`, {
    name: team.name,
    info: team.info,
  });
};

export const deleteTeamApi = (teamId: string): Promise<any> => {
  return axios.delete(`/api/teams/${teamId}`);
};
