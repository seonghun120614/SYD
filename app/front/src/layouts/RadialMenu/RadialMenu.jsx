import React from 'react';
import './RadialMenu.css';

const RadialMenu = ({ items }) => {
  const itemCount = items.length;
  const radius = 50;

  const getCoordinates = (index) => {
    const angle = (index / itemCount) * 2 * Math.PI;
    const x = radius * Math.cos(angle);
    const y = radius * Math.sin(angle);
    return { x, y };
  };

  return (
    <div className="radial-menu">
      {items.map((item, index) => {
        const { x, y } = getCoordinates(index);
        return (
          <p
            key={index}
            className="radial-item"
            style={{
              transform: `translate(${x}px, ${y}px)`
            }}
          >
            {item}
          </p>
        );
      })}
    </div>
  );
};

export default RadialMenu;
