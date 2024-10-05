import React, { useState, useEffect } from 'react';
import axios from 'axios';

function DataList({ refresh }) {
  const [dataList, setDataList] = useState([]);

  useEffect(() => {
    fetchData();
  }, [refresh]);

  const fetchData = () => {
    axios.get(`/api/students/`)
      .then(response => {
        setDataList(response.data);
      })
      .catch(error => {
        console.error('Error fetching data:', error);
        alert('Failed to fetch data.');
      });
  };

  const allKeys = Array.from(new Set(
    dataList.flatMap(item => Object.keys(item))
  ));

  const displayKeys = allKeys.filter(key => key !== 'id');

  return (
    <div>
      <h2>Data List</h2>
      {dataList.length > 0 ? (
        <table border="1" cellPadding="5">
          <thead>
            <tr>
              {displayKeys.map((key, index) => (
                <th key={index}>{key}</th>
              ))}
            </tr>
          </thead>
          <tbody>
            {dataList.map((item, index) => (
              <tr key={index}>
                {displayKeys.map((key, idx) => (
                  <td key={idx}>{item[key]}</td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      ) : (
        <p>No data available.</p>
      )}
    </div>
  );
}

export default DataList;

