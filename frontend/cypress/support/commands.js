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

Cypress.Commands.add('login', () => {
  // Make a login call to the endpoint and set token in Cypress environment
  cy.visit('http://localhost:3000/login'); // Assuming '/login' is your login page URL
  cy.get('#username').type(Cypress.env('username')); // Assuming '#username' is the username input field
  cy.get('#password').type(Cypress.env('password')); // Assuming '#password' is the password input field
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
Cypress.env('username', 'u1');
Cypress.env('password', 'pwd');
