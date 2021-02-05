import React from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";

import AppMenu from "./components/Menu/AppMenu";
import ServersTable from "./components/ServersTable/ServersTable";
import TeamsList from "./components/Teams/TeamsList";
import SystemsList from "./components/Systems/SystemsList";
import "./App.css";

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <AppMenu />
        <Switch>
          <Route path="/" exact component={TeamsList} />
          <Route path="/table" exact component={ServersTable} />
          <Route path="/teams" exact component={TeamsList} />
          <Route path="/teams/:teamId" component={SystemsList} />
        </Switch>
      </BrowserRouter>
    </div>
  );
}

export default App;
