describe('LoginFormComponent', () => {
  beforeEach(() => {
    cy.visit('http://localhost:3000/login');
  });

  it('should log in with correct credentials', () => {
    cy.get('#username').type('u1');
    cy.get('#password').type('pwd');
    cy.get('form').submit();
    
    // Add assertions to verify successful login behavior
  //   cy.url().should('include', '/activitycenter');
  // });

  // it('should display error message with incorrect credentials', () => {
  //   cy.get('#username').type('invalid_username');
  //   cy.get('#password').type('invalid_password');
  //   cy.get('form').submit();

  //   // Add assertions to verify error message is displayed
  //   cy.contains('.error-message', 'Invalid credentials').should('be.visible');
  });

  it('can navigate to another page', () => {
    cy.visit('http://localhost:3000/uploadtrail');

  });
});