import './App.css'
import React, { useState, useEffect } from "react";
import "./App.css";
import axios from 'axios';
        

function App() {
  const [jobs, setJobs] = useState([]);

  const fetchData = async () => {
    try {
      const response = await axios.get('http://localhost:5000/jobs', {
        withCredentials: true,
      });
      setJobs(response.data);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  useEffect(() => {
    const fetchDataAndAppliedStatus = async () => {
      await fetchData(); 
  
      const appliedJobsData = localStorage.getItem('appliedJobs');
      if (appliedJobsData) {
        const appliedJobs = JSON.parse(appliedJobsData);
        setJobs(appliedJobs);
      }
    };
  
    fetchDataAndAppliedStatus(); // Call the function
  
  }, []);

  
  const handleAppliedToggle = (jobId) => {
    const updatedJobs = jobs.map((job) => {
      if (job.id === jobId) {
        job.applied = !job.applied; 
      }
      return job;
    });

    // Update state and local storage
    setJobs(updatedJobs);
    localStorage.setItem('appliedJobs', JSON.stringify(updatedJobs));
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Job Board</h1>
        <table className="Job-table">
          <thead>
            <tr>
              <th>Company</th>
              <th>Job Title</th>
              <th>Application Link</th>
              <th>Applied</th> {/* New column */}
            </tr>
          </thead>
          <tbody>
            {jobs.map((job) => (
              <tr key={job.id}>
                <td>{job.company}</td>
                <td>{job.position_name}</td>
                <td>
                  <a href={job.link} target="_blank" rel="noopener noreferrer">
                    Apply Now
                  </a>
                </td>
                <td className='checkbox'>
                
                  <input 
                    
                    type="checkbox"
                    checked={job.applied || false}
                    onChange={() => handleAppliedToggle(job.id)}
                  >
                  </input>
              
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
