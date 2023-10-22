import './App.css'
  import React, {useState, useEffect} from "react";
  import "./App.css";
  import axios from 'axios'
  
  function App() {
    // Sample data for the table

    const [jobs, setJobs] = useState([]);

    const fetchData = async () => {
      try {
        const response = await axios.get('http://207.23.170.240:5173/', {
          withCredentials: true,
        });
        setJobs(response.data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };


    useEffect(() => {
      fetchData();
    }, []);
    return (
      <div className="App">
        <header className="App-header">
          <h1>Design Jobs Board</h1>
          <table className="Job-table">
            <thead>
              <tr>
                <th>Company</th>
                <th>Job Title</th>
                <th>Application Link</th>
              </tr>
            </thead>
            <tbody>
              {jobs.map((job, index) => (
                <tr key={index}>
                  <td>{job.company}</td>
                  <td>{job.position_name}</td>
                  <td>
                    <a href={job.link} target="_blank" rel="noopener noreferrer">
                      Apply Now
                    </a>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </header>
      </div>
    );
  }
  
  export default App;
