import { System } from "../types/system";
import axios from "axios";

export const getTeamSystems = (teamId: string): Promise<Array<System>> => {
  return axios
    .get(`/api/systems/?team=${teamId}`)
    .then((res) => res.data.map((system: System) => new System(system)));
};

export const addSystemApi = (
  name: string,
  universe: string,
  teamName: string,
  info: string
): Promise<any> => {
  return axios.post("/api/systems/", {
    name: name,
    universe: universe,
    team: teamName,
    info: info,
  });
};

export const updateSystemApi = (system: any): Promise<any> => {
  return axios.put(`/api/systems/${system.id}/`, {
    name: system.name,
    team: system.team,
    universe: system.universe,
    info: system.info,
  });
};

export const deleteSystemApi = (systemId: string): Promise<any> => {
  return axios.delete(`/api/systems/${systemId}`);
};
