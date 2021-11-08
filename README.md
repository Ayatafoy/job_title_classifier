# Job title classifier
The repository contains the implementation of the job title classifier training and deployment pipeline

Classifier was trained to classify the following IT Jobs specializations:
1. Cloud Architect
2. Technology Integration
3. Statistics
4. Data and Analytics Manager
5. Artificial Intelligence
6. Technical Operations
7. Data Warehousing
8. Network Architect
9. Data Quality Manager
10. Data Visualization Expert
11. Machine Learning
12. Database Administrator
13. IT Consultant
14. Cloud Services Developer
15. Deep Learning
16. Data Architect
17. Information Security Analyst
18. Business Intelligence Analyst
19. Data Analyst
20. Data Engineer
21. IT Systems Administrator
22. Big Data Engineer
23. Business Analyst
24. Full Stack Developer
25. Data Scientist

The service uses simple keywords match to detect job position grade, for the following grades:
1. Intern
2. Junior
3. Middle
4. Senior
5. Lead
6. Executive

### Testing deployed docker container
1. `cd` to the root of this repository.
2. `docker compose up --build` run the containers
5. Run `main.py` script

### Setup local environment
1. Set your Python executable to 3.7
2. `cd` to the root of this repository.
3. `virtualenv job_title_classifier` to create a virtual environment.
4. `pip install virtualenv` to install virtualenv 
5. Activate the virtual environment
   - bash: `source job_title_classifier/bin/activate`
6. `pip install ipykernel` to install ipykernel
7. `python -m ipykernel install --user --name job_title_classifier --display-name "job_title_classifier"` to register new kernel
8. `pip install -r requirements.txt` to install project dependencies
9. run `classifier_app.py`   
9. run `main.py`