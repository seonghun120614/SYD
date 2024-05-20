import React from "react";

import CSVUpload from './components/CSVUpload';
import DownloadButton from './components/DownloadButton';


function App() {
  return (
    <div>
      <CSVUpload />
      <DownloadButton />
    </div>
  );
}

export default App;