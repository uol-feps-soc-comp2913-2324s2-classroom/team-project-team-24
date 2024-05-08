[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/Nrqv5LcV)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=13773586&assignment_repo_type=AssignmentRepo)

# Running the App
## With docker
1. Install docker
2. Clone the repository
3. `cd` into the root directory of the project (`/team-project-teamp-24/`)
4. Run `docker compose up`

## Without docker
1. Install Node.js (version 18.0 or higher) and Python3.9 or higher
2. Open 2 terminal windows
3. Inside one run:
```shell
cd frontend
npm install
npm run serve
```
**Unix**  
4. Inside the other run:
```shell
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
flask --app app run -p 5001
```
**Windows**  
4. Inside the other run:
```shell
cd backend
python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
flask --app app run -p 5001
```
5. To then get membership payment working you need to use `stripe-cli`. To get that working follow the instructions in `/backend/stripe_api/README.md`.

# Testing 
## The frontend with cypress (End-To-End Testing)

navigate to `frontend\gpx_app_front`
need to have the app running while doing this, and it needs to be on port 3000. If not using docker run the command:

```BASH
npm run serve -- --port 3000
```

to then run cypress:

```BASH
# Run cypress
npx cypress open
```

2. To stop it, simply ctrl + c.

3. To observe the tests in action, navigate to E2E testing > specs > 'frontend\gpx_app_front\cypress\e2e', and select your desired cypress test file

4. If you'd like to add to the specs for further tests, or utilise existing files, navigate to the same area in your IDE, and

- Commands are to be placed in `cypress/support/commands.js`, essential commands such as login() are found here.
- Whenever you do cypress testing, to use `cy.login()`, just include it in the `beforeEach` portion of your tests, see `uploadTrail.cy.js` for reference
- Test GPX and dummy files are included in `cypress/fixtures`
- refer to https://docs.cypress.io/api/table-of-contents for helpful commands in cypress

## The backend with pytest (Unit Testing)
1. Activate the virtual environment setup earlier in the installation instructions
2. Run `cd backend`
3. Run `pytest` and all the tests should show
4. A green `.` means the test passed, a red `F` means the test failed.

