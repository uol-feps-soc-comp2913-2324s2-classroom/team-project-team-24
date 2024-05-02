describe('LoginFormComponent', () => {
    beforeEach(() => {
        cy.visit('http://localhost:3000/login')
    })

    it('should log in with correct credentials', () => {
        cy.get('#username').type('u1')
        cy.get('#password').type('pwd')
        cy.contains('button', 'Login').click()
    })

    it('should trigger forgotPassword page', () => {
        cy.get('.form-actions a').contains('Forgot password').click()
        cy.visit('http://localhost:3000/resetPassword')
    })

    it('should trigger register page', () => {
        cy.get('.form-footer a').contains('Create an account').click()
        cy.visit('http://localhost:3000/register')
    })

    it('cypress login function works', () => {
        cy.visit('http://localhost:3000/activitycenter')
    })
})
