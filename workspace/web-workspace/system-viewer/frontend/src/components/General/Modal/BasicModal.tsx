import React, { ReactElement, useState } from "react";
import { Dropdown, Input, Menu, Modal } from "antd";
import "antd/lib/modal/style/index.css";
import "antd/lib/button/style/index.css";
import "antd/lib/menu/style/index.css";
import "antd/lib/dropdown/style/index.css";
import "./AddModal.css";

interface BasicModalProps {
  title: string;
  visible: boolean;
  onOk: (e: React.MouseEvent<HTMLElement>) => void;
  onCancel: (e: React.MouseEvent<HTMLElement>) => void;
}

const BasicModal: React.FC<BasicModalProps> = ({
  title,
  visible,
  onOk,
  onCancel,
  children,
}) => {
  const handleOk = (e: React.MouseEvent<HTMLElement>) => {
    onOk(e);
  };

  const handleCancel = (e: React.MouseEvent<HTMLElement>) => {
    onCancel(e);
  };

  return (
    <Modal
      title={title}
      visible={visible}
      onOk={handleOk}
      onCancel={handleCancel}
      okText={"הוסף"}
      cancelText={"בטל"}
    >
      {children}
    </Modal>
  );
};

export default BasicModal;
