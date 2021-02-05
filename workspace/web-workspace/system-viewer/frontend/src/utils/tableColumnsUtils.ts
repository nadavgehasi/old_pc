import { Server } from "../types/server";

/**
 * Compares between two server objects by a specific field.
 * @param firstServer
 * @param secondServer
 * @param field The field serverName by which the objects should be compared
 */
const sortByField = (
  firstServer: Server,
  secondServer: Server,
  field: keyof Server
): number => {
  if (firstServer[field] > secondServer[field]) {
    return 1;
  } else if (firstServer[field] < secondServer[field]) {
    return -1;
  } else {
    return 0;
  }
};

export const getColumnByField = (
  titleName: string,
  serverFieldName: keyof Server
) => {
  return {
    title: titleName,
    dataIndex: serverFieldName,
    key: serverFieldName,
    sorter: (firstServer: Server, secondServer: Server) =>
      sortByField(firstServer, secondServer, serverFieldName),
  };
};
