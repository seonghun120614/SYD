import React from 'react';
import Button from 'react-bootstrap/Button';


const DownloadButton = ({ src }) => {
  /**
   * Download button for linked plot in Block tag.
   */
  
  const handleDownload = () => {

    const anchor = document.createElement('a');
    anchor.href = src;
    anchor.download = 'plot.png';

    anchor.click();
  };

  return (
    <Button variant="dark" onClick={handleDownload}>
      Download
    </Button>
  );
}

export default DownloadButton;