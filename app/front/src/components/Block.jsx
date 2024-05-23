import React from 'react';
import Button from './DownloadButton';
import Plot from './Plot'


function Block() {
  /**
   * The Block component represents a block that displays a plot and a download button 
   * to the user.
   */
  return (
    <div class="block">
      <Plot />
      <Button />
    </div>
  );
}

export default Block;