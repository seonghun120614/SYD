import React, {
  useState
} from "react";

import "./CSVUpload.css";
import { Upload } from 'react-bootstrap-icons';



const CSVUpload = () => {
  /*
  To get the csv file from client
  */
  const [csvFile, setCsvFile] = useState(null);
  const handleDragOver = (event) => event.preventDefault();

  const handleDrop = (event) => {
    event.preventDefault();
    const files = event.dataTransfer.files;

    if (!(files.length === 1 & files[0].name.endsWith(".csv")))
      return;
    setCsvFile(files[0]);

    const formData = new FormData();
    formData.append(files[0]);
    const response = fetch('/api', {
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
          csvFile
          ? csvFile.name
          : "Please upload one file"
        }</p>
      </label>
    </form>
  );
}

export default CSVUpload;