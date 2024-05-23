import React from "react";

import CSVUpload from './components/CSVUpload';
import Body from './layouts/Body';
import Header from './layouts/Header';
import Footer from './layouts/Footer';


const App = () => {
  return (
    <div>
      <Header />
      <Body />
      <CSVUpload />
      <Footer />
    </div>
  );
}

export default App;