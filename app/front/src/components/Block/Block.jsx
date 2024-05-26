import React from 'react';

import DownloadButton from './DownloadButton';
import Plot from './Plot'

import './Block.css'


const Block = ({ src }) => {
  /**
   * The Block component represents a block that displays a plot and a download button 
   * to the user.
   */
  return (
    <div className="block">
      <div className="plot_position">
        <Plot src={src}/>
      </div>
      <div className="button_position">
        <DownloadButton />
      </div>
    </div>
  );
}

export default Block;