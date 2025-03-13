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







