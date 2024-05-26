import React from 'react';

import './Plot.css'

const Plot = ({ src }) => {
  /**
   * Using api and draw image about received byteString based 64 bits
   */

  return (
    <div className="plot">
      <img src={src} alt="Plot image"/>
    </div>
  );
}

export default Plot;
