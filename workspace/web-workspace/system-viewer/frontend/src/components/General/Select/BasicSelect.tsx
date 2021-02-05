import { Select } from "antd";
import React from "react";
import "antd/lib/select/style/index.css";

const { Option } = Select;

interface BasicSelectProps {
  content: string[];
  onChange: (value: string) => void;
}

const BasicSelect: React.FC<BasicSelectProps> = ({ content, onChange }) => {
  return (
    <Select defaultValue="בחר" style={{ width: 120 }} onChange={onChange}>
      {content.map((value) => (
        <Option value={value}>{value}</Option>
      ))}
    </Select>
  );
};

export default BasicSelect;
