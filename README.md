# IntroMLOps

Slides [Here](https://docs.google.com/presentation/d/1CAaNZtyCv5nmif1a03c6tZSTQdc47DF1Ssd_v8NI9yA/edit?usp=sharing) (Only for CIMAT) 


Step 1. (If Docker installed) Test Docker Image in your computer

* run/open docker
* on terminal 
  * cd to/file/containing/dockerfile
  * docker build -t loan_prediction .  
  *  docker run -p 8000:8000 loan_prediction
  *  if correctly will prompt: 
  > Application startup complete.\
  INFO: Uvicorn running on http://0.0.0.0:8000
  * send post example 
  > curl -X POST http://0.0.0.0:8000/predict_status \
     -H "Content-Type: application/json" \
     --data '{
         "Gender": "Male",
         "Married": "Yes",
         "Dependents": "0",
         "Education": "Graduate",
         "Self_Employed": "No",
         "ApplicantIncome": 5720,
         "CoapplicantIncome": 0,
         "LoanAmount": 110,
         "Loan_Amount_Term": 360,
         "Credit_History": 1,
         "Property_Area": "Urban"
     }'

Step 2. (If no docker install, try on your computer)
* create a virtual enviroment (make sure pyenv or virtualenv are installed or do it w/IDE)
    >virtualenv -p python3.9.6 venv 
* activate activate venv
    >  source venv/bin/activate
* install libraries
   > make install-model-requirements
* move into ./model folder, and run
  * >  uvicorn app:app --reload 
* once app is running, will show something like: 
    > INFO:     Will watch for changes in these directories: ['...path_to.../model']\
    INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)\
    INFO:     Started reloader process [..] using WatchFiles\
    INFO:     Started server process [...]\
    INFO:     Waiting for application startup.\
    INFO:     Application startup complete.\
* visit http://127.0.0.1:8000/docs and use the swagger with input_example json file. 





References: 


Books:

* McMahon, A. P. (2023). Machine Learning Engineering with Python: Manage the production life cycle of machine learning models using MLOps with practical examples. Packt Publishing
* Tashman, N., & Bourdev, B. (2022). Practical MLOps: Operationalizing Machine Learning Models. O’Reilly Media.
* Pote, S. (2023). Machine Learning in Production: Master the art of delivering robust Machine Learning solutions with MLOps. BPB Publications.
* Chung, C. (2022). Designing Machine Learning Systems: An Iterative Process for Production-Ready Applications. O’Reilly Media.


Websites/Tutorials:

* https://github.com/suhas-ds?tab=repositories
* https://mlflow.org/docs/latest/getting-started/running-notebooks/
* https://anderfernandez.com/en/blog/complete-mlflow-tutorial/
* https://dagshub.com/blog/model-deployment-types-strategies-and-best-practices/#challenges-in-ml-models-deployment
* Tutorial COMIA Patrones de Diseño y MLOps:Fundamentos y Aplicaciones ([Repo](https://github.com/Ivanrs297/mlops-mlflow-tracking))
* https://github.com/marketplace/actions/deploy-to-heroku
* https://www.ml4devs.com/en/articles/serverless-architecture-for-microservices-on-aws-vs-google-cloud-vs-azure-as-iaas-caas-paas-faas/
* https://www.anyscale.com/blog/challenges-of-deploying-ml-models-in-production













