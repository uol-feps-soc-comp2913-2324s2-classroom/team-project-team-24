// ***********************************************
// This example commands.js shows you how to
// create various custom commands and overwrite
// existing commands.
//
// For more comprehensive examples of custom
// commands please read more here:
// https://on.cypress.io/custom-commands
// ***********************************************
//
//
// -- This is a parent command --
// Cypress.Commands.add('login', (email, password) => { ... })
//
//
// -- This is a child command --
// Cypress.Commands.add('drag', { prevSubject: 'element'}, (subject, options) => { ... })
//
//
// -- This is a dual command --
// Cypress.Commands.add('dismiss', { prevSubject: 'optional'}, (subject, options) => { ... })
//
//
// -- This will overwrite an existing command --
// Cypress.Commands.overwrite('visit', (originalFn, url, options) => { ... })

// cypress/support/commands.js

Cypress.Commands.add('setUserToken', () => {
  // Extract token from the response and set it in Cypress environment
  cy.request({
    method: 'POST',
    url: 'http://localhost:3000/login', // Replace with your login endpoint
    body: {
      username: Cypress.env('username'),
      password: Cypress.env('password')
    }
  }).then((response) => {
    Cypress.env('token', response.body.token);
  });
});

Cypress.Commands.add('register', () => {
  cy.visit('http://localhost:3000/register'); // Assuming '/register' is your registration page URL
  cy.contains('label', 'Username').siblings('input').type(Cypress.env('username'));
  cy.contains('label', 'Email').siblings('input').type(Cypress.env('email'));
  cy.contains('label', 'Password').siblings('input').type(Cypress.env('password'));
  cy.contains('label', 'Confirm Password').siblings('input').type(Cypress.env('password'));

  // continue button
  cy.contains('button', 'Continue').click()

  // step 2 of register
  cy.contains('label', 'Gender').siblings('input').type(Cypress.env('gender'));
  cy.contains('label', 'Age').siblings('input').type(Cypress.env('age'));
  cy.wait(1000);
  // click register
  cy.contains('Register').click()
  cy.url().should('include', '/membership'); // Verify successful login redirect
});

Cypress.Commands.add('login', () => {
  // Make a login call to the endpoint and set token in Cypress environment
  cy.visit('http://localhost:3000/login'); // Assuming '/login' is your login page URL
  cy.contains('label', 'Username').siblings('input').type(Cypress.env('username'));
  cy.contains('label', 'Password').siblings('input').type(Cypress.env('password'));
  cy.contains('button', 'Login').click(); // Click the login button
  cy.url().should('include', '/activitycenter'); // Verify successful login redirect
  cy.setUserToken(); // Set user token after successful login
});   

Cypress.Commands.add('createProduct', (name) => {
  const payload = {
    name: name,
  };

  const token = Cypress.env('token');
  // Access the user JWT token stored in env

  cy.request({
    method: 'POST',
    url: 'http://localhost:5001/products/', // Replace with your products endpoint
    body: payload,
    headers: {
      authorization: 'Bearer ' + token, // Consume the token
    },
  }).as('createProduct');
});

// Set your login credentials as environment variables
Cypress.env('username', 'newuser');
Cypress.env('email', 'newuser@example.com');
Cypress.env('password', 'Password123');
Cypress.env('gender' , 'male');
Cypress.env('age' , '18');