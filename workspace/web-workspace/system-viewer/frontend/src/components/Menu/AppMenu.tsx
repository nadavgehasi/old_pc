import { Link } from "react-router-dom";
import React from "react";
import { Menu } from "antd";
import "antd/lib/menu/style/index.css";

import "./AppMenu.css";

const AppMenu = () => {
  return (
    <Menu defaultSelectedKeys={["/teams"]}>
      <Menu.Item key="/table">
        <Link to="table">שרתים</Link>
      </Menu.Item>
      <Menu.Item key="/teams">
        <Link to="/teams">צוותים</Link>
      </Menu.Item>
    </Menu>
  );
};

export default AppMenu;
