import React, {
  useState
} from "react";

import "./CSVUpload.css";
import { Upload } from 'react-bootstrap-icons';



const CSVUpload = () => {
  /*
  To get the csv file from client
  */
  const handleDragOver = (event) => event.preventDefault();
  const [numOfFiles, setNumOfFiles] = useState(0);
  const handleDrop = async (event) => {
    event.preventDefault();

    const files = event.dataTransfer.files;
    if (!(files.length === 1 & files[0].name.endsWith(".csv")))
      return;
    setNumOfFiles(files.length);

    // Make form
    const formData = new FormData();
    const title = files[0].name.split('.')[0];
    const csv = files[0];
    formData.append('title', title);
    formData.append('csv', csv);

    // Request
    const response = await fetch('/api/upload', {
      method: 'POST',
      body: formData
    });

    if (response.ok)
      console.log(response.json());
    else
      console.log('Failed Loading');
  }

  return (
    <form>
      <label
        onDrop={handleDrop}
        onDragOver={handleDragOver}
        htmlFor="csv"
        className="btn btn-outline-black"
        id="upload_button"
      >
        <Upload style={{ fontSize: '4em' }} />
        <br/>
        <br/>
        <p>Load your csv file</p>
        <p>{
          numOfFiles === 1 ? "Success" : "Please upload one file"
        }</p>
      </label>
    </form>
  );
}

export default CSVUpload;