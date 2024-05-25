import React, { useState } from "react";

import Block from "../../components/Block/Block";
import CSVUpload from "../../components/CSVUpload/CSVUpload";
import './Body.css';

const Body = () => {
  const [response, setResponse] = useState(null);

  const handleFileUpload = async (file) => {
    // Make form
    const formData = new FormData();
    const title = file.name.split('.')[0];
    const csv = file;

    formData.append('title', title);
    formData.append('csv', csv);

    try {
      // Request
      const res = await fetch('/api/upload', {
        method: 'POST',
        body: formData
      });

      if (res.ok) {
        const data = await res.json();
        setResponse(data); // 응답 데이터를 상태로 업데이트
      } else {
        setResponse(null);
        console.log('Failed Loading');
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <main>
      {response === null ? (
        <CSVUpload onFileUpload={handleFileUpload} />
      ) : (
        <div className="container-item">
          {response.map((object) => (
            <div key={object.id}>
              {object.name}
            </div>
          ))}
          {/* <Block src={src}/> */}
        </div>
      )}
    </main>
  );
}

export default Body;
