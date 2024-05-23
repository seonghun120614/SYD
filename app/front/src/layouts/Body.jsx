import React from "react";

import Block from "../components/Block";

function Body() {
  /**
   * Body has many blocks and showing 2 columns grid
   */
  const blocks = [1, 2, 3, 4, 5];

  return (
    <body>
      {blocks.map(() => (
        <Block />
      ))}
    </body>
  );
}

export default Body;