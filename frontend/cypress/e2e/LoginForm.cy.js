describe('LoginFormComponent', () => {
    beforeEach(() => {
        cy.visit('http://localhost:3000/login')
    })

    it('should display the username input field', () => {
        cy.contains('label', 'Username').siblings('input').should('be.visible').type(Cypress.env('username'));
      });
    
      it('should display the password input field', () => {
        cy.contains('label', 'Password').siblings('input[type="password"]').should('be.visible').type(Cypress.env('password'));
      });
    
      it('should display the "Login" button', () => {
        cy.contains('button', 'Login').should('be.visible');
      });
    
      it('should display the "Create an account" link', () => {
        cy.contains('a', 'Create an account').should('be.visible');
      });
    
      it('should display the separator text', () => {
        cy.contains('.separator-text', 'Or').should('be.visible');
      });

      it('login functionality should work', () => {
        cy.login();        
      })
})
