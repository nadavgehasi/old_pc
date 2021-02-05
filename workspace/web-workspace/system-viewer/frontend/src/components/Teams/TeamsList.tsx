import React from "react";
import {
  addTeamApi,
  deleteTeamApi,
  getTeams,
  updateTeamApi,
} from "../../api/TeamApi";
import { Team } from "../../types/team";
import EditableList from "../General/List/EditableList";

const TeamsList = () => {
  const getAddTeamContent = (): any => {
    return {
      "שם": "",
      "מידע": "",
    };
  };

  const getUpdateTeamContent = (team: Team): any => {
    return {
      id: team.id,
      name: team.name,
      info: team.info,
    };
  };

  const getTeamFromContent = (team: any): any => {
    return {
      id: team["id"],
      name: team["שם"],
      info: team["מידע"],
    };
  };

  const itemToPropertyList = (team: any) => {
    return {
      "מספר מערכות": team.systems.length,
      "מספר שרתים": team.servers.length,
      "מידע חופשי": team.info,
    };
  };

  const addTeam = (newTeam: any) => {
    return addTeamApi(newTeam["שם"], newTeam["מידע"]);
  };

  const updateTeam = (item: any) => {
    return updateTeamApi(getTeamFromContent(item));
  };

  const itemToLink = (item: any): string => {
    return `/teams/${item.id}`;
  };

  return (
    <EditableList
      getListContent={getTeams}
      addItemApi={addTeam}
      deleteItemApi={deleteTeamApi}
      updateItemApi={updateTeam}
      itemToAddModal={getAddTeamContent}
      itemToUpdateModal={getUpdateTeamContent}
      modalTitle="הוספת צוות"
      itemToPropertyList={itemToPropertyList}
      itemToLink={itemToLink}
    />
  );
};

export default TeamsList;
