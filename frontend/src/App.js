import React, { useState } from 'react';
import UploadForm from './UploadForm';
import DataList from './DataList';

function App() {
  const [refreshData, setRefreshData] = useState(false);

  const handleUploadSuccess = () => {
    setRefreshData(!refreshData);
  };

  return (
    <div className="App">
      <UploadForm onUploadSuccess={handleUploadSuccess} />
      <DataList refresh={refreshData} />
    </div>
  );
}

export default App;

