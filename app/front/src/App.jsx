import React from "react";

import CSVUpload from './components/CSVUpload';
import Button from './components/Button';
import Plot from './components/Plot';


function App() {
  return (
    <div>
      <CSVUpload />
      <Button />
      <Plot />
    </div>
  );
}

export default App;