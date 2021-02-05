import React, { useEffect, useState } from "react";
import { List } from "antd";
import "./ListStyle.css";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faPlus } from "@fortawesome/free-solid-svg-icons";
import AddModal from "../Modal/AddModal";
import ItemCard from "../Card/ItemCard";

interface EditableListProps {
  modalTitle: string;
  getListContent: () => Promise<Array<any>>;
  deleteItemApi: (id: string) => Promise<any>;
  updateItemApi: (item: any) => Promise<any>;
  addItemApi: (item: any) => Promise<any>;
  itemToPropertyList: (item: any) => any;
  itemToAddModal: () => any;
  itemToUpdateModal: (item: any) => any;
  itemToLink: (item: any) => string;
}

const EditableList: React.FC<EditableListProps> = ({
  modalTitle,
  getListContent,
  deleteItemApi,
  addItemApi,
  updateItemApi,
  itemToPropertyList,
  itemToAddModal,
  itemToUpdateModal,
  itemToLink,
}) => {
  const [listContent, setListContent] = useState(Array<any>());
  const [modalVisible, setModalVisible] = useState(false);
  const [modalContent, setModalContent] = useState(itemToAddModal());
  const [isAdd, setIsAdd] = useState(false);

  useEffect(() => {
    getListContent().then((listContent) => setListContent(listContent));
  }, []);

  const deleteItem = (itemId: string) => {
    deleteItemApi(itemId).then((res) => {
      // TODO Add message here
      getListContent().then((listContent) => setListContent(listContent));
    });
  };

  const updateItem = (e: React.MouseEvent<HTMLElement>, item: any) => {
    setModalVisible(false);
    updateItemApi(item).then((res) => {
      // TODO add message here
      getListContent().then((listContent) => setListContent(listContent));
    });
  };

  const addItem = (e: React.MouseEvent<HTMLElement>, newItemInfo: any) => {
    setModalVisible(false);
    addItemApi(newItemInfo).then((res) => {
      // TODO Add message here
      getListContent().then((listContent) => setListContent(listContent));
    });
  };

  return (
    <div>
      <FontAwesomeIcon
        icon={faPlus}
        style={{ float: "right" }}
        onClick={() => {
          setIsAdd(true);
          setModalContent(itemToAddModal());
          setModalVisible(true);
        }}
      />
      <AddModal
        title={modalTitle}
        visible={modalVisible}
        isAdd={isAdd}
        onAdd={addItem}
        onUpdate={updateItem}
        onCancel={(e: React.MouseEvent<HTMLElement>, newTeamInfo: any) => {
          setModalVisible(false);
        }}
        newObj={modalContent}
        setNewObj={setModalContent}
      />
      <List
        dataSource={listContent}
        renderItem={(item) => (
          <ItemCard
            item={item}
            itemToLink={itemToLink}
            deleteItem={deleteItem}
            itemToPropertyList={itemToPropertyList}
            updateItem={() => {
              setIsAdd(false);
              setModalContent(itemToUpdateModal(item));
              setModalVisible(true);
            }}
          />
        )}
      />
    </div>
  );
};

export default EditableList;
