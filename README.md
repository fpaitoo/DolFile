# DolFile
This application makes the job of saving files in a central location easier by sending files via api for safe keeping and also by retrieving the files via api.
This is actively being developed and more features will be added in order to secure, improve and add more features.
##Pre-requisite
1. Python > 3.9
2. Pip > 22.0
## Setup
### 1. Method One - Cloning Project
1. Clone the project by using the clone functionalities provided by Github.
2. With your terminal application opened, navigate to the project Directory
3. RUN `pip3 install -r requirements.txt`
4. You can now serve the application by running the below command. You can change the port number to your preferred port
`gunicorn --workers 1 --timeout 120 -b 0.0.0.0:8000 wsgi:gunicorn_app`
5. Open your browser and navigate to your servers ip or 127.0.0.1:port_number if you are running it locally
    `http://127.0.0.1:8000` - assuming am running it locally 
6. By default, username = 'admin' and password = 'letMePass'

### 2. Method Two - Docker
1. Run `docker pull gpaitoo/dolfile` to get the image locally
2. to start serving the application run `docker run --name dolfile -p 8000:8000 -e USERNAME=gpaitoo -e PASSWORD=mypassword gpaitoo/dolfile`
3. You can set your username and password by using the environment variables. Once set, do not use it in your subsequent commands
4. Open your browser and navigate to your servers ip or 127.0.0.1:port_number if you are running it locally
    `http://127.0.0.1:8000` - assuming am running it locally 
5. By default, username = 'admin' and password = 'letMePass' unless set via environment variables 

##Usage
