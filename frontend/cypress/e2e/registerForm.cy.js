describe('RegisterFormComponent', () => {
    beforeEach(() => {
        cy.visit('http://localhost:3000/register')
        cy.register(); // Log in before each test  
    })

    it('should register a new user', () => {
        cy.contains('label', 'Username').siblings('input').type('chick');
        cy.contains('label', 'Email').siblings('input').type('chick@example.com');
        cy.contains('label', 'Password').siblings('input').type('Password123');
        cy.contains('label', 'Confirm Password').siblings('input').type('Password123');

        // continue button
        cy.contains('button', 'Continue').click()

        // step 2 of register
        cy.contains('label', 'Gender').siblings('input').type('male');
        cy.contains('label', 'Age').siblings('input').type('18');
        cy.contains('button', 'Register').click()
    })

    it('cypress register function works', () => {
        cy.visit('http://localhost:3000/activitycenter')
    })
})
