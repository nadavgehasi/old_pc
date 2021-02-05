import React from "react";
import { Tag } from "antd";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faEdit } from "@fortawesome/free-regular-svg-icons/faEdit";
import { faTrashAlt } from "@fortawesome/free-regular-svg-icons/faTrashAlt";
import { faRedoAlt } from "@fortawesome/free-solid-svg-icons/faRedoAlt";
import {
  Server,
  CORES_FIELD,
  RAM_FIELD,
  SERVER_NAME_FIELD,
  STATUS_FIELD,
  SYSTEM_NAME_FIELD,
  TAGS_FIELD,
  TEAM_NAME_FIELD,
  SERVER_BASE_FIELD,
} from "../../types/server";
import { getColumnByField } from "../../utils/tableColumnsUtils";

const getServersTableColumns = (deleteServer: (serverId: string) => void) => {
  return [
    {
      ...getColumnByField("שרת", SERVER_NAME_FIELD),
      render: (text: string) => (
        <span>
          <FontAwesomeIcon icon={faEdit} />
          <a> {text}</a>
        </span>
      ),
    },
    { ...getColumnByField("בסיס", SERVER_BASE_FIELD) },
    { ...getColumnByField("צוות", TEAM_NAME_FIELD) },
    { ...getColumnByField("מערכת", SYSTEM_NAME_FIELD) },
    {
      ...getColumnByField("מבצעי / טסטים", TAGS_FIELD),
      render: (tag: string) => (
        <span>
          {() => {
            let color = tag.length > 5 ? "geekblue" : "green";
            if (tag === "Tests") {
              color = "volcano";
            }
            return (
              <Tag color={color} key={tag}>
                {tag.toUpperCase()}
              </Tag>
            );
          }}
        </span>
      ),
    },
    {
      ...getColumnByField("סטטוס", STATUS_FIELD),
      render: (text: string) => (
        <span>
          <FontAwesomeIcon icon={faRedoAlt} />
          <a> {text}</a>
        </span>
      ),
    },
    { ...getColumnByField("ראם", RAM_FIELD) },
    { ...getColumnByField("מספר ליבות", CORES_FIELD) },
    {
      title: "Delete",
      key: "delete",
      render: (text: string, record: Server) => (
        <span>
          <FontAwesomeIcon
            icon={faTrashAlt}
            onClick={(event) => deleteServer(record.id)}
          />
        </span>
      ),
    },
  ];
};

export default getServersTableColumns;
