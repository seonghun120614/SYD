import React from "react";

function CSVUpload() {
  return (
    <form>
      <input type="file" id="csv" name="csv" accept=".csv"/>
    </form>
  );
}

export default CSVUpload;