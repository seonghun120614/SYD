import React, {
  useState
} from "react";

import Block from "../../components/Block/Block";
import CSVUpload from "../../components/CSVUpload/CSVUpload";
import Modal from "../../components/Modal/Modal";
import './Body.css';

const Body = () => {
  const [response, setResponse] = useState(null);
  const [isLoading, setIsLoading] = useState(false);

  const handleFileUpload = async (file) => {
    // Make form
    const formData = new FormData();
    const title = file.name.split('.')[0];
    const csv = file;
    console.log(csv);

    formData.append('title', title);
    formData.append('csv', csv);

    setIsLoading(true);

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
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <main>
      <Modal isOpen={isLoading} />
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
