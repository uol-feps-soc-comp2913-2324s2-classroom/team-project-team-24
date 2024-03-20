// cypress/integration/uploadTrail.spec.js
describe('Login Page', () => {
  it('should have JavaScript enabled', () => {
    // Cache the login session
    cy.session('login', () => {
      cy.visit('http://localhost:3000/login'); // Replace '/login' with the URL of your login page

      // Type into the username input field
      cy.get('#username') // Assuming '#username' is the selector for the username input field
        .type('u1')
        .should('have.value', 'u1'); // Verify that the input value is set correctly

      // Type into the password input field
      cy.get('#password') // Assuming '#password' is the selector for the password input field
        .type('pwd')
        .should('have.value', 'pwd'); // Verify that the input value is set correctly

      // Submit the form
      cy.get('form').submit();

      // Verify that the page navigates to the expected URL after form submission
      cy.url().should('include', '/activitycenter'); // Replace '/dashboard' with the expected URL after successful login
    });
  });
});

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
