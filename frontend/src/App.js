import React, { useState } from 'react';
import axios from 'axios';

function App() {

  const [file, setFile] = useState(null);
  const [message, setMessage] = useState('');

  const handleUpload = async () => {

    if (!file) {
      alert('Please select a file');
      return;
    }

    const formData = new FormData();
    formData.append('file', file);

    try {

      const response = await axios.post(
        'http://127.0.0.1:8000/api/upload/',
        formData
      );

      setMessage(
        `${response.data.message} - ${response.data.records_created} records created`
      );

    } catch (error) {

      console.error(error);
      setMessage('Upload failed');

    }
  };

  return (
    <div style={{
      padding: '40px',
      fontFamily: 'Arial'
    }}>

      <h1>Breathe ESG Assignment</h1>

      <p>Upload ESG CSV File</p>

      <input
        type="file"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <br /><br />

      <button onClick={handleUpload}>
        Upload CSV
      </button>

      <br /><br />

      <h3>{message}</h3>

    </div>
  );
}

export default App;