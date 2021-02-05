import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faEdit } from "@fortawesome/free-regular-svg-icons/faEdit";
import { faTrashAlt } from "@fortawesome/free-regular-svg-icons/faTrashAlt";
import React, { ReactElement } from "react";

interface CardTitleProps {
  title: ReactElement;
  deleteCard: () => void;
  updateCard: () => void;
}

const CardTitle: React.FC<CardTitleProps> = ({
  title,
  deleteCard,
  updateCard,
}) => {
  return (
    <div>
      <FontAwesomeIcon
        icon={faEdit}
        style={{ float: "right" }}
        onClick={() => updateCard()}
      />
      {title}
      <FontAwesomeIcon
        icon={faTrashAlt}
        onClick={deleteCard}
        style={{ float: "left" }}
      />
    </div>
  );
};

export default CardTitle;
