describe('Activity Center Page', () => {
  beforeEach(() => {
    cy.visit('http://localhost:3000/login')
    cy.login(); // Log in before each test  
    cy.visit('http://localhost:3000/activitycenter')
  });

  it('should load successfully', () => {
    // Check if the page title is visible
    cy.contains('h1', 'Activity Center Page').should('be.visible');
  });

  it('should display all components', () => {
    // Check if all expected components are present
    cy.get('GoalComponent').should('exist');
    cy.get('MapViewerComponent').should('exist');
    cy.get('OverallTrailStatsComponent').should('exist');
    cy.get('TrailListComponent').should('exist');
  });

})