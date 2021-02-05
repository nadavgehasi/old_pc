import React from "react";

interface PropertyListProps {
  content: Object;
}

const PropertyList: React.FC<PropertyListProps> = ({ content }) => {
  return (
    <div>
      {Object.entries(content).map((objectEntry) => (
        <h3>
          {objectEntry[0]}: {objectEntry[1]}
        </h3>
      ))}
    </div>
  );
};

export default PropertyList;
