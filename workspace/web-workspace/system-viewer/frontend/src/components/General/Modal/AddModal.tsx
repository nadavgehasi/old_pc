import React from "react";
import { Input } from "antd";
import "antd/lib/modal/style/index.css";
import "antd/lib/button/style/index.css";
import "./AddModal.css";
import BasicModal from "./BasicModal";
import BasicSelect from "../Select/BasicSelect";

interface AddModalProps {
  title: string;
  visible: boolean;
  isAdd: boolean;
  onUpdate: (e: React.MouseEvent<HTMLElement>, newObject: any) => void;
  onAdd: (e: React.MouseEvent<HTMLElement>, newObject: any) => void;
  onCancel: (e: React.MouseEvent<HTMLElement>, newObject: any) => void;
  newObj: any;
  setNewObj: (newObj: any) => void;
}

const AddModal: React.FC<AddModalProps> = ({
  title,
  visible,
  isAdd,
  onUpdate,
  onAdd,
  onCancel,
  newObj,
  setNewObj,
}) => {
  const updateEntry = (name: string, value: string) => {
    newObj[name] = value;
    setNewObj(newObj);
  };

  const getContent = (objectEntry: [string, unknown]) => {
    if (objectEntry[1] instanceof Array) {
      return (
        <BasicSelect
          content={objectEntry[1]}
          onChange={(value: string) => updateEntry(objectEntry[0], value)}
        />
      );
    } else if (objectEntry[1] === "" || !isAdd) {
      return (
        <Input
          defaultValue={String(objectEntry[1])}
          onChange={(e) => updateEntry(objectEntry[0], e.target.value)}
        />
      );
    }
    return <span>{String(objectEntry[1])}</span>;
  };

  return (
    <BasicModal
      title={title}
      visible={visible}
      onOk={(e) => {
        if (isAdd) {
          onAdd(e, newObj);
        } else {
          onUpdate(e, newObj);
        }
      }}
      onCancel={(e) => onCancel(e, newObj)}
    >
      {Object.entries(newObj).map((objectEntry) => (
        <h3 key="add-modal">
          <span>{objectEntry[0]}: </span>
          {getContent(objectEntry)}
        </h3>
      ))}
    </BasicModal>
  );
};

export default AddModal;
