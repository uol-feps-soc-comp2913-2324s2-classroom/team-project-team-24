// cypress/integration/uploadTrail.spec.js

describe('UploadTrail Page', () => {
  beforeEach(() => {
    cy.visit('http://localhost:3000/login')
    cy.login(); // Log in before each test  
    // cy.interceptAxiosAuth();
  });

  it('should load the page successfully', () => {
    cy.visit('http://localhost:3000/uploadtrail')
    cy.contains('h1', 'Upload your new trail').should('be.visible');
  });

  it('should upload a file successfully', () => {
    const fileName = 'example.gpx';
    cy.fixture(fileName).then(fileContent => {
      cy.get('input[type="file"]').attachFile({
        fileContent,
        fileName,
        mimeType: 'application/gpx+xml'
      });
      cy.get('[data-cy=upload-button]').click(); // Assuming you add a data-cy attribute to your upload button
      // Add assertions here to verify successful upload
    });
  });

  it('should validate form fields', () => {
    cy.get('input[type="file"]').attachFile('example.txt'); // Upload unsupported file type
    cy.get('[data-cy=upload-button]').should('be.disabled');

    cy.get('[data-cy=route-name]').type('Trailblazer');
    cy.get('[data-cy=upload-button]').should('be.disabled');

    cy.get('[data-cy=route-name]').clear().type('New Trail');
    cy.get('[data-cy=upload-button]').should('not.be.disabled');
  });

  it('should handle duplicate route name', () => {
    cy.get('[data-cy=route-name]').type('Trailblazer');
    cy.get('[data-cy=upload-button]').should('be.disabled');
    cy.contains('.text-danger', 'Duplicate name detected.').should('be.visible');
  });

  it('should handle API request', () => {
    // Mock API request
    cy.intercept('POST', '/upload', (req) => {
      expect(req.body.get('file')).to.exist;
      expect(req.body.get('routeName')).to.exist;
      expect(req.body.get('exerciseType')).to.exist;
      req.reply({ status: 200, body: { message: 'Upload successful' } });
    }).as('upload');

    cy.get('input[type="file"]').attachFile('example.gpx');
    cy.get('[data-cy=route-name]').type('New Trail');
    cy.get('[data-cy=upload-button]').click();
    cy.wait('@upload').its('response.statusCode').should('eq', 200);
  });
});
