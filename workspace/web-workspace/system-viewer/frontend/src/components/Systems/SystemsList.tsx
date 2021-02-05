import React from "react";
import {
  addSystemApi,
  deleteSystemApi,
  getTeamSystems,
  updateSystemApi,
} from "../../api/SystemApi";
import { RouteComponentProps } from "react-router-dom";
import { System } from "../../types/system";
import EditableList from "../General/List/EditableList";

interface SystemsListProps extends RouteComponentProps<{ teamId: string }> {}

const SystemsList: React.FC<SystemsListProps> = ({ match }) => {
  const getAddSystemContent = (): any => {
    return {
      "שם מערכת": "",
      צלע: ["Ip", "Badid"],
      "שם צוות": `${match.params.teamId}`,
      "מידע חופשי": "",
    };
  };

  const getUpdateSystemContent = (system: System): any => {
    return {
      id: system.id,
      "שם מערכת": system.name,
      צלע: system.universe,
      "שם צוות": system.team,
      "מידע חופשי": system.info,
    };
  };

  const getSystemFromUpdateModalContent = (system: any) => {
    return {
      id: system.id,
      name: system["שם מערכת"],
      universe: system["צלע"],
      team: system["שם צוות"],
      info: system["מידע חופשי"],
    };
  };

  const updateSystem = (system: any) => {
    return updateSystemApi(getSystemFromUpdateModalContent(system));
  };

  const addSystem = (newSystem: any) => {
    return addSystemApi(
      newSystem["שם מערכת"],
      newSystem["צלע"],
      newSystem["שם צוות"],
      newSystem["מידע חופשי"]
    );
  };

  const itemToPropertyList = (system: any) => {
    return {
      "שם השרת": system.servers,
      "שם הצוות": system.team,
      "צלע": system.universe,
      "מידע חופשי": system.info,
    };
  };

  return (
    <EditableList
      getListContent={() => getTeamSystems(match.params.teamId)}
      addItemApi={addSystem}
      deleteItemApi={deleteSystemApi}
      updateItemApi={updateSystem}
      modalTitle="הוספת מערכת"
      itemToPropertyList={itemToPropertyList}
      itemToLink={(item: any) => {
        return item.id;
      }}
      itemToUpdateModal={getUpdateSystemContent}
      itemToAddModal={getAddSystemContent}
    />
  );
};

export default SystemsList;
