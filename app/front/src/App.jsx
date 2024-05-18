import React, { useState } from "react";
import axios from "axios";

function App() {
  const [text, setText] = useState("없음");
  

  const clicked = () => {
    const data = {"name":"tempdata"};

    axios
      .post("http://127.0.0.1:8000/add/", data)
      .then((response) => {
        console.log(JSON.stringify(response.data));
        setText(JSON.stringify(response.data));
      })
      .catch((error) => {
        console.error("Error", error);
      });
  };


  return (
    <div>
      <h1>{text}</h1>
      <button onClick={clicked}>클릭</button>
    </div>
  );
}

export default App;