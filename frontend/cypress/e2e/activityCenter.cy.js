describe('Activity Center Page', () => {
  beforeEach(() => {
    cy.visit('http://localhost:3000/login')
    cy.login(); // Log in before each test  
    cy.visit('http://localhost:3000/activitycenter')
  });

  it('should display all components', () => {
    // Assert that the main containers exist
    cy.get('.activityCenterPageContainer').should('exist');
    cy.get('.main-container').should('exist');
    cy.get('.map-view-column').should('exist');
    cy.get('.track-stats-column').should('exist');
    cy.get('.trails-container').should('exist');
  });

  describe('Trail List Item Component', () => {
    it('should download the trail when download button is clicked', () => {

      // Intercept console.log statements
    cy.window().then((win) => {
      cy.stub(win.console, 'log').as('consoleLog');
    });

      // Find the download button and click it
      cy.contains('.outer', 'Download').click();

      // Log some information after clicking the button
      cy.log('After clicking the download button');

      // Assert that the downloadTrail method is called
      // TODO: INSERT DESIRED BEHAVIOUR
    });
  
    it('should delete the trail when delete button is clicked', () => {
      // Find the delete button and click it
      cy.contains('.outer', 'Delete').click();
  
      // Assert that the deleteTrail method is called
      // TODO: INSERT DESIRED BEHAVIOUR
    });
  });

})