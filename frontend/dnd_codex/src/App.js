import './App.css';
import axios from 'axios';
import { useState, useEffect } from 'react';



function App() {
  const [allies, setAllies] = useState([]);

  useEffect(() =>{
    fetchAllies();
  }, []);

  const fetchAllies = async () => {
    try {
      const response = await axios.get('http://localhost:8000/api/allieslist/');
      setAllies(response.data);
    }catch(error){
      console.error('Error fetching allies:',error);
    }
  };

  return (
    <div>
      <h1>Allies List</h1>
      {allies.map((ally) => (
        <div key={ally.id}>
          <h2>{ally.name}</h2>
        </div>
      ))}
    </div>
  );
}

export default App;
