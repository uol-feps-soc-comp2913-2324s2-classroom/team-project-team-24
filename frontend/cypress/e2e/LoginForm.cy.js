describe('LoginFormComponent', () => {
  beforeEach(() => {
    cy.visit('http://localhost:3000/login');
  });

  it('should log in with correct credentials', () => {
    cy.get('#username').type('u1');
    cy.get('#password').type('pwd');
    cy.get('form').submit();
  });
  
  it('cypress login function works', () => {
    cy.login() // logs in the user
  })
});