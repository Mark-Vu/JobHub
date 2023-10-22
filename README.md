# JobHub 
Star this repo if you are interested, we might reach out for help in this project! We will host it on _[JobHubSFU.com](JobHubSFU.com)_ once we work things out.  

## We will get you all the jobs you ever wanted to find~ 

### Inspiration
When you are in the co-op job search process. You'll search for 
- Software Engineer Intern 
- Software Engineer Co-op 
- Software Developer Intern 
- Software Developer Co-op 
- Data Engineer Intern 
- Data Engineer Co-op 

And MANY more ... You will put all these keywords into Indeed, LinkedIn, Glassdoor, etc... You are excited/anxious and motivated when you just started applying, but after a few days/weeks, you get no interviews and this keyword search process starts to burn you out. 

Now, imagine you go to "_JobHubSFU.com_", and you see a tailored list of jobs that you can apply for, scraped from all these websites using enumerated keywords. You click on a job URL and you apply. 

We hope this can make your student-professional transition easier. We also hope we can help you turn into a chapter of your career in life. 

### What's Next? 
Since we are first time using these technologies, we didn't have enough time to complete it. We will 
- first, discuss more possibilities and explore tool options, define scope and provide a more detailed proposal as a result 
- then, will finalize on tech stack and architecture design 
- discuss and break down the project into large/medium tasks 
- break down larger tasks into individual minimal tickets that one person is able to take 
- work as a team in the initial setup 
- colab to build a fresh working application 
- deploy to make it internet-facing 
- invite other developers to contribute and make it more than a cs-job-only thing 

We will write comprehensive documentation for everyone (0 experience required kinda doc yea) who's interested in joining the project and contributing. This will be a sick project to work on to learn all aspects of software development and popular technologies, especially Amazon Web services (AWS). 

### Just some examples of how this project can be extended: 
- Include user registration (major, experience level, etc) 
    - There is a lot to work on for each major/experience level. 
- Include more websites 
    - We need customized scrapers for each website since their page structures are different. 
- Email/Message notification 
    - Register users to AWS SNS to give daily updates 
- Resume review section 
    - Post resumes and get advices/roasted
Many more... 

A potential architecture image is attached. 

--------------------------------------------------------------------------------------------------
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
