import React from "react";

import "./CSVUpload.css";
import { Upload } from 'react-bootstrap-icons';


const CSVUpload = () => {
  /*
   To get the csv file from client
  */
  return (
    <form>
      <label htmlFor="csv" class="btn btn-outline-black" id="upload_button">
        <Upload style={{ fontSize: '4em' }} />
        <br/>
        <br/>
        <p>Load your csv file</p>
        <input type="file" id="csv" name="csv" style={{ display:"none" }} />
      </label>
    </form>
  );
}

export default CSVUpload;