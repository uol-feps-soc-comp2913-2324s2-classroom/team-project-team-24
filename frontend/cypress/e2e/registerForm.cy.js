describe('RegisterFormComponent', () => {
    beforeEach(() => {
        cy.visit('http://localhost:3000/register')
    })

    it('shoule register a new user', () => {
        cy.get('#username').type('newuser')
        cy.get('#email').type('newuser@example.com')
        cy.get('#password').type('password123')
        cy.get('#confirmPassword').type('password123')

        // continue button
        cy.contains('button', 'Continue').click()

        //step 2
        cy.get('#gender').type('male')
        cy.get('#age').type('18')
        cy.contains('button', 'Register').click()
    })

    it('cypress register function works', () => {
        cy.visit('http://localhost:3000/activitycenter')
    })
})
