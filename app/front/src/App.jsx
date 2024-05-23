import React from "react";

import CSVUpload from './components/CSVUpload';
import Block from './components/Block';
import Loading from './components/Block';
import Header from './layouts/Header';


function App() {
  return (
    <div>
      <Header />
      <CSVUpload />
      <Block />
    </div>
  );
}

export default App;