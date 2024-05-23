import React from 'react';


function DownloadButton() {
  /**
   * Download button for linked plot in Block tag.
   */
  const handleDownload = () => {
    console.log("Download Button is clicked.");
  };

  return (
    <button onClick={handleDownload}>
      Download
    </button>
  );
}

export default DownloadButton;