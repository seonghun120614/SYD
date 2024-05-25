import React from "react";

import Block from "../../components/Block/Block"
import './Body.css';

const Body = () => {
  /**
   * Body has many blocks and showing 2 columns grid
   */
  const blocks = [1, 2, 3, 4, 5];

  return (
    <main>
      {blocks.map(() => (
        <div className="container-item">
          <Block />
        </div>
      ))}
    </main>
  );
}

export default Body;