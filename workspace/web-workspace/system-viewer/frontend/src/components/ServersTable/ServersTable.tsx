import React, { useEffect, useState } from "react";
import { Table } from "antd";
import "antd/lib/table/style/index.css";
import "antd/lib/tag/style/index.css";
import "antd/lib/pagination/style/index.css";
import getServersTableColumns from "./ServerTableColumns";
import "./ServersTable.css";
import { deleteServerApi, getServers } from "../../api/ServerApi";
import { getTeamSystems } from "../../api/SystemApi";
import { System } from "../../types/system";
import { Server } from "../../types/server";

// interface ServersTableProps {
//     servers: Array<Server>;
//     deleteServer: (serverId: string) => void;
// }

const ServersTable: React.FC = () => {
  const [servers, setServers] = useState(Array<Server>());

  useEffect(() => {
    getServers().then((servers: Array<Server>) => {
      setServers(servers);
    });
  }, []);

  const deleteServer = (serverId: string) => {
    deleteServerApi(serverId);
    // setServers(deleteServerFromServers(serverId, servers));
  };

  const data = servers.map((server) => ({
    ...server,
    key: server.id,
  }));

  return (
    <Table
      dataSource={data}
      columns={getServersTableColumns(deleteServer)}
      bordered={false}
      style={{ direction: "rtl" }}
    />
  );
};

export default ServersTable;
