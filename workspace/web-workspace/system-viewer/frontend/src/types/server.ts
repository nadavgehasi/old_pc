export const ID_FIELD: keyof Server = "id";
export const SERVER_NAME_FIELD: keyof Server = "name";
export const SERVER_BASE_FIELD: keyof Server = "base";
export const TEAM_NAME_FIELD: keyof Server = "team";
export const SYSTEM_NAME_FIELD: keyof Server = "systems";
export const STATUS_FIELD: keyof Server = "status";
export const TAGS_FIELD: keyof Server = "tag";
export const RAM_FIELD: keyof Server = "ram";
export const CORES_FIELD: keyof Server = "cores";

interface ServerInterface {
  id: string;
  name: string;
  base: string;
  team: string;
  systems: Array<string>;
  status: string;
  tag: string;
  ram: string;
  cores: string;
}

export class Server implements ServerInterface {
  id: string;
  name: string;
  base: string;
  team: string;
  systems: Array<string>;
  status: string;
  tag: string;
  ram: string;
  cores: string;

  constructor(server: ServerInterface) {
    this.id = server.id;
    this.name = server.name;
    this.base = server.base;
    this.team = server.team;
    this.systems = server.systems;
    this.status = server.status;
    this.tag = server.tag;
    this.ram = server.ram;
    this.cores = server.cores;
  }
}
