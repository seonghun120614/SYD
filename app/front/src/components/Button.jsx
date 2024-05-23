import React from 'react';


function DownloadButton() {
  /*
  Plot image download button
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