# Job title classifier
The repository contains the implementation of the job title classifier training and deployment pipeline

### Classifier was trained to classify the following IT Jobs specializations:
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

### The service uses simple keywords match to detect job position grade, for the following grades:
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

## Improvements steps
1. Extend training dataset with more classes and samples
2. Train FastText embeddings an full dataset, presented in EDA notebook and use FastText embeddings instead of Embedding layer
3. Add k-fold cross validation
4. Add bayessian hyperparameters optimization
5. Add training tricks like LR scheduler and early stopping
6. Add more models for benchmarking, for example SVM, Logreg, LSTM, Distilbert and so on. Depending on dataset size.
7. Iteratively clean the dataset using cleanlab
8. Add classes weights
9. Test different loss functions
10. Test different optimizers

## Useful resources:
### Papers with code dataset
https://paperswithcode.com/paper/a-large-scale-industrial-and-professional
https://paperswithcode.com/dataset/skill2vec
https://paperswithcode.com/dataset/jobstack

### Kaggle datasets
https://www.kaggle.com/nsharan/h-1b-visa
https://www.kaggle.com/abrambeyer/h1b-visa-petitions-20152019
https://www.kaggle.com/mullervilmos/it-jobs
https://www.kaggle.com/jonatancr/data-science-jobs-around-the-world
https://www.kaggle.com/devario/uk-data-science-jobs-dataset
https://www.kaggle.com/PromptCloudHQ/us-jobs-on-monstercom
https://www.kaggle.com/estasney/job-title-synonyms

### O*NET Job titles description
https://www.onetcenter.org/database.html#all-files

### Job titles IT
https://github.com/ggeop/Job-Recommendation-Engine

### Industry text classifier
https://github.com/Elzawawy/industry-text-classifier

### Classification of job positions by area and level
https://github.com/rootstrap/ai-job-title-area-classification/
https://github.com/rootstrap/ai-job-title-level-classification

### A tool to assign standard occupational classification codes to job vacancy descriptions
https://github.com/aeturrell/occupationcoder

### Job tag classifier
https://github.com/mrciolino/Job-Tag-Classifier

### Implementing a CNN for Text Classification in TensorFlow
http://www.wildml.com/2015/12/implementing-a-cnn-for-text-classification-in-tensorflow/

### Example of text classification on job description dataset
https://github.com/Solvve/ml_job_classifier/blob/master/job_classification_example.ipynb

### Linkedin Job parser
https://github.com/sethpoly/linkedin_linker
https://github.com/connorgiles/job-hoarder
https://github.com/rylee12/Job-Finder
https://github.com/JKeun/something-fun/blob/master/data/job-titles-linkedin-parsing-name.csv
https://levelup.gitconnected.com/linkedin-scrapper-a3e6790099b5

### ODS salaries analysis
https://github.com/egorborisov/jobs_article

Google drive with additional datasets:
https://drive.google.com/file/d/1BdF_oM6OoESRM8vvuQgfdWHz65dbDZqn/view?usp=sharing

Unzip the archive in the project root.

