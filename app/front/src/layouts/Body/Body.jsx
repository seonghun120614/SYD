import React, {
  useState,
  useEffect
} from "react";

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
    console.log(csv);

    formData.append('title', title);
    formData.append('csv', csv);

    try {
      // Request
      const res = await fetch('/api/upload', {
        method: 'POST',
        body: formData
      });

      if (res.ok) {
        const json = await res.json();
        setResponse(json);
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
        <>
          {response.map((item) => (
            <div className="container-item">
              <Block src={`data:image/png;base64,${item}`} />
            </div>
          ))}
        </>
      )}
    </main>
  );
}

export default Body;
