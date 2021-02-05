import React from "react";
import { Card } from "antd";
import "antd/lib/card/style/index.css";
import "./CardStyle.css";
import CardTitle from "./CardTitle";
import PropertyList from "../List/PropertyList";
import { Link } from "react-router-dom";

interface ItemCardProps {
  item: any;
  deleteItem: (itemId: string) => void;
  updateItem: (system: any) => void;
  itemToLink: (item: any) => string;
  itemToPropertyList: (item: any) => any;
}

const ItemCard: React.FC<ItemCardProps> = ({
  item,
  deleteItem,
  updateItem,
  itemToPropertyList,
  itemToLink,
}) => {
  return (
    <Card
      title={
        <CardTitle
          title={<Link to={itemToLink(item)}>{item.name}</Link>}
          deleteCard={() => deleteItem(item.id)}
          updateCard={() => updateItem(item)}
        />
      }
    >
      <PropertyList content={itemToPropertyList(item)} />
    </Card>
  );
};

export default ItemCard;
