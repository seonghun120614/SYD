import React from 'react';


function DownloadButton() {
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