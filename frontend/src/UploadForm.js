import React, { useState } from 'react';
import axios from 'axios';

function UploadForm({ onUploadSuccess }) {
  const [csvFile, setCsvFile] = useState(null);

  const handleFileChange = (e) => {
    setCsvFile(e.target.files[0]);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!csvFile) {
      alert('Please select a CSV file to upload.');
      return;
    }
    const formData = new FormData();
    formData.append('file', csvFile);

    axios.post(`/api/upload/`, formData)
      .then(response => {
        alert('Upload successful!');
        if (onUploadSuccess) {
          onUploadSuccess(); 
        }
      })
      .catch(error => {
        console.error(error);
        alert('An error occurred during upload.');
      });
  };

  return (
    <div>
      <h2>Upload CSV</h2>
      <form onSubmit={handleSubmit}>
        <input type="file" accept=".csv" onChange={handleFileChange} required />
        <button type="submit">Upload</button>
      </form>
    </div>
  );
}

export default UploadForm;

