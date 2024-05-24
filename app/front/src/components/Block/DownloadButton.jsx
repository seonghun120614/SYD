import React from 'react';
import Button from 'react-bootstrap/Button';


const DownloadButton = () => {
  /**
   * Download button for linked plot in Block tag.
   */
  const handleDownload = () => {
    console.log("Download Button is clicked.");
  };

  return (
    <Button variant="dark" onClick={handleDownload}>
      Download
    </Button>
  );
}

export default DownloadButton;