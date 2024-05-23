import React from "react";


const CSVUpload = () => {
  /*
   To get the csv file from client
  */
  return (
    <form>
      <input type="file" id="csv" name="csv" accept=".csv"/>
    </form>
  );
}

export default CSVUpload;