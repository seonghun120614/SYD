import React from "react";

import CSVUpload from './components/CSVUpload';
import Body from './layouts/Body';
import Header from './layouts/Header';


function App() {
  return (
    <div>
      <Header />
      <Body />
      <CSVUpload />
    </div>
  );
}

export default App;