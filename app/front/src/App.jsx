import React, { useState } from "react";
import axios from "axios";

function App() {
  const [text, setText] = useState("없음");

  // 비동기 통신 로직을 별도의 함수로 분리
  const fetchData = async () => {
    try {
      const data = { "name": "tempdata" };

      const response = await axios.post(`/api/add/`, data);
      console.log(JSON.stringify(response.data));
      setText(JSON.stringify(response.data));
    } catch (error) {
      console.error("Error", error);
      setText("데이터 로딩 중 에러 발생!");
    }
  };

  return (
    <div>
      <h1>{text}</h1>
      <button onClick={fetchData}>클릭</button>
    </div>
  );
}

export default App;