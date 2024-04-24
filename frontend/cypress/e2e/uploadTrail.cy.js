describe('UploadTrail Page', () => {
  beforeEach(() => {
    cy.visit('http://localhost:3000/login')
    cy.login(); // Log in before each test  
    cy.visit('http://localhost:3000/uploadtrail')

  });

  it('should load uploadtrail page successfully', () => {
    cy.contains('h1', 'Upload your new trail').should('be.visible');
  });

  it('should upload a GPX file successfully', () => {
    // Define the file path
    const filePath = './cypress/fixtures/waypoint1.gpx';

    // Attach the file to the file input field
    cy.get('input[type="file"]').selectFile(filePath);

    // Enter the route name
    cy.get('input[placeholder="Enter the name of your route"]').type('Example Route');

    // Select the exercise type
    cy.get('select').select('Running'); // Adjust the exercise type as needed

    // Click the upload button
    cy.contains('Upload').click(); // Assuming the button text is 'Upload'

    // Wait for the upload to complete and verify success
    cy.contains('Uploading data...').should('not.exist'); // Wait for upload process to complete
  });

  it('should validate form fields', () => {
    cy.get('input[type="file"]').selectFile('./cypress/fixtures/example.json'); // Upload unsupported file type
    // TODO: bring to error page
  });

  it('should handle duplicate route name', () => {
    cy.get('.upload-gpx-container input[type="text"]').type('Trailblazer');
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
    const filePath = './cypress/fixtures/waypoint1.gpx';
    cy.get('input[type="file"]').selectFile(filePath);
    cy.get('.upload-gpx-container input[type="text"]').type('New Trail');
    cy.contains('Upload').click();
    // TODO: ADD UPLOAD RESPONSE
    // cy.wait('@upload').its('response.statusCode').should('eq', 200);
  });
});
