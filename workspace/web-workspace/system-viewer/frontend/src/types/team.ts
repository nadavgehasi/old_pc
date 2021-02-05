interface TeamInterface {
  id: string;
  name: string;
  servers: Array<string>;
  systems: Array<string>;
  info: string;
}

export class Team implements TeamInterface {
  id: string;
  name: string;
  servers: Array<string>;
  systems: Array<string>;
  info: string;

  constructor(team: TeamInterface) {
    this.id = team.id;
    this.name = team.name;
    this.servers = team.servers;
    this.systems = team.systems;
    this.info = team.info;
  }
}
