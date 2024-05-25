import React from "react";

import Block from "../../components/Block/Block";
import CSVUpload from "../../components/CSVUpload/CSVUpload";
import './Body.css';

const Body = () => {
  /**
   * Body has many blocks and showing 2 columns grid
   */
  const blocks = [1, 2, 3, 4, 5];

  return (
    <main>
      {
        // Just for testing
        1 === 1
        ? <CSVUpload />
        : blocks.map(() => {
          <div className="container-item">
            <Block />
          </div>
        })
      }
    </main>
  );
}

export default Body;