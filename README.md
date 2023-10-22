

# Project README
# JobHub
The transition from academic studies to professional internships is a significant "turning over a new leaf" moment for SFU students. "JobHub" aims to make this transformative journey smoother, ensuring that students can confidently step into the professional world.
## Installation and Run Instructions

### Server Setup

1. Open a terminal and navigate to the server directory:
   ```bash
   cd server
   pip install -r requirements.txt
   cd server/src
   export FLASK_APP=main.py
   flask run --host=0.0.0.0 --port=5173
  
2. Open another terminal:
  
  ```bash
  cd client
  npm install
  npm run dev
  ```
Make sure it is running on port 5173 (same port as flask server)
