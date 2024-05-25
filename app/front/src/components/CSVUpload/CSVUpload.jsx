import React, {
  useState
} from "react";

import "./CSVUpload.css";
import { Upload } from 'react-bootstrap-icons';

const CSVUpload = ({ onFileUpload }) => {
  const handleDragOver = (event) => event.preventDefault();
  const [numOfFiles, setNumOfFiles] = useState(0);

  const handleDrop = async (event) => {
    event.preventDefault();

    const files = event.dataTransfer.files;
    if (!(files.length === 1 && files[0].name.endsWith(".csv"))) {
      setNumOfFiles(files.length);
      return;
    }
    
    onFileUpload(files[0]);
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
          numOfFiles === 1 ? "Success" : "Please upload one csv file"
        }</p>
      </label>
    </form>
  );
}

export default CSVUpload;
