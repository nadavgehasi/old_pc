interface SystemInterface {
  id: string;
  name: string;
  servers: Array<string>;
  team: string;
  universe: string;
  info: string;
}

export class System implements SystemInterface {
  id: string;
  name: string;
  servers: Array<string>;
  team: string;
  universe: string;
  info: string;

  constructor(system: SystemInterface) {
    this.id = system.id;
    this.name = system.name;
    this.servers = system.servers;
    this.team = system.team;
    this.universe = system.universe;
    this.info = system.info;
  }
}
