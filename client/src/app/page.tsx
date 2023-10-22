import { useState } from 'react';
import logo from '../../.next/image/logo.png'; // Import the image
import "./homepage.css"

export default function Homepage() {
	const [option, setOption] = useState("job")
	function handleSelectOption() {
		
	}
  return (
    <div className="grid-container">
        <header>
            <h1>Job Hub</h1>
            <div className='header-buttons'>
                <button className='outline'>Filter</button>
                <button className='fill'>Sign in</button>
            </div>
        </header>
        <div className="main-content">
            <div className="content">
                <table>
                    <thead>
                        <tr>
                            <th><img className='logo' src={logo.src} alt="Logo" /></th>
                            <th>Company</th>
                            <th>Position</th>
                            <th>Location</th>
                            <th>Info</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><button>Job</button></td>
                            <td>Ragged Edge</td>
                            <td>Account Manager</td>
                            <td>London</td>
                            <td>+</td>
                        </tr>
                        <tr>
                            <td><button>Refresh</button></td>
                        </tr>
                        <tr>
                            <td><button>About</button></td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
  );
}
