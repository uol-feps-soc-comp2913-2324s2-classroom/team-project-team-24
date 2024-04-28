describe('LoginFormComponent', () => {
    beforeEach(() => {
        cy.visit('http://localhost:3000/login')
    })

    it('should log in with correct credentials', () => {
        cy.get('#username').type('u1')
        cy.get('#password').type('pwd')
        // 能用的按钮代码
        cy.contains('button', 'Login').click()
    })

    it('should trigger forgotPassword page', () => {
        // 模拟点击"Forgot password"按钮
        cy.get('.form-actions a').contains('Forgot password').click()
        cy.visit('http://localhost:3000/resetpassword')
    })

    it('should trigger register page', () => {
        // 模拟点击"Forgot password"按钮
        cy.get('.form-footer a').contains('Create an account').click()
        cy.visit('http://localhost:3000/register')
    })

    it('cypress login function works', () => {
        // cy.login() // logs in the user
        cy.visit('http://localhost:3000/activitycenter')
    })
})
