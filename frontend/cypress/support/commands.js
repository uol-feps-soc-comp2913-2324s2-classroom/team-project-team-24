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
Cypress.Commands.add('login', () => {
    // Caching session when logging in via page visit
    cy.session('user-login', () => {
        cy.visit('http://localhost:3000/login');
        cy.get('#username').type('u1'); // Assuming '#username' is the selector for the username input field
        cy.get('#password').type('pwd'); // Assuming '#password' is the selector for the password input field
        cy.get('form').submit();
        // cy.url().should('include', '/activitycenter');
    });
    // Caching session when logging in via API
    cy.session('api-login', () => {
        cy.request({
        method: 'POST',
        url: 'http://localhost:3000/login',
        body: { username: 'u1', password: 'pwd' }, // Use the actual username and password values
        }).then(({ body }) => {
        window.localStorage.setItem('token', body.token)
        
      }).then(response => {
        // expect(response.body).to.have.property('token');
      });
        // }).then(response => {
        // expect(response.status).to.eq(200);
        // expect(response.body).to.have.property('token');
        // window.localStorage.setItem('token', response.body.token);
        // });
    });
  });
  
