describe('Membership Page', () => {
  beforeEach(() => {
    cy.login(); // Log in before each test
  });

  it('should display the page heading', () => {
    cy.contains('h1', 'Membership').should('be.visible');
    cy.get('.membership-options-container').should('be.visible');
  });

  it('should display the subscription options container', () => {
    cy.get('.membership-options-container').should('be.visible');
  });

  it('should display membership options', () => {
    // Assuming membership options are loaded dynamically
    cy.get('.membership-option').should('have.length.greaterThan', 0);
  });
});