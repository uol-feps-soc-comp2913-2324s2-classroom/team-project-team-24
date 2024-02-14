[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/Nrqv5LcV)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=13773586&assignment_repo_type=AssignmentRepo)

# To Get Started With Development

## Prerequisites
Make sure you have these installed:
1. Docker
2. Node.js (Version 18.0 or higher)
3. Python3

## Starting the whole project
The whole project can now be started with one command using docker compose:
```bash
docker compose up
```
**Use `docker compose up --build` if you have made any changes. If you don't your changes will not be shown when you run the app!!**  
To then close it, press `Ctrl+C`.  
You could also use the `-d` flag to make it detached, and the in order to stop it, run:
```bash
docker compose down
```

## Starting the frontend development server
Make sure you have Node.js installed.
```BASH
# Navigate to the frontend folder
cd ./team-project-team-24/frontend/gpx_app_front

# Install dependencies
npm install

# Start development server
npm run dev

# ctrl + c to stop the server as usual
```

## Starting the backend development server
Make sure you have Docker installed.

### With Docker
```BASH
# Navigate to the backend folder
cd ./team-project-team-24/backend

# Build the docker image
docker build -t gpx_app .

# Run the docker container
# You can also do this in the Docker Desktop app which is easier just make sure to set the "host port" 
# to 5000 in the "optional settings"
docker run --name gpx_app_server -p 5000:5000 -d gpx_app

# Command breakdown:
# docker run --name <set this to whatever you want> -p <host_port>:<container_port> -d <image_name>
# Probably a good idea to keep the host port and the container port as 5000
```

### Without Docker
```BASH
# Navigate to the backend folder
cd ./team-project-team-24/backend

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start the server
python run.py
```

## Stopping the backend development server
```BASH
# Stop the docker container
docker stop gpx_app_server
```

## More Useful Docker Commands
```BASH
# List all running containers
docker ps

# List all containers
docker ps -a

# List all images
docker images

# Remove a container
docker rm <container_id>

# Remove an image
docker rmi <image_id>
```
Or forget about all of this and use the Docker Desktop app to manage containers and images.
