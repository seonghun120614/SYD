import React from 'react';
import DownloadButton from './DownloadButton';
import Plot from './Plot'


const Block = () => {
  /**
   * The Block component represents a block that displays a plot and a download button 
   * to the user.
   */
  return (
    <div class="block">
      <Plot />
      <DownloadButton />
    </div>
  );
}

export default Block;