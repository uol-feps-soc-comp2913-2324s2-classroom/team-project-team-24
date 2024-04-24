describe('Login Page', () => {
    beforeEach(() => {
        it('successfully loads', () => {
            cy.visit('http://localhost:3000/login')
        })
    })

    describe('Login Page', () => {
        it('successfully logs in', () => {
            cy.visit('http://localhost:3000/login')

            cy.get('input[name=username]').type('testuser')
            cy.get('input[name=password]').type('password123{enter}')
        })
    })
})

// describe('My Test Suite', () => {
//     beforeEach(() => {
//         // 调用登录命令，假设用户名和密码已提供
//         cy.login('testuser', 'password123')
//     })

//     it('Test Case 1: Check user profile', () => {
//         // 测试用例内容，假设这需要用户已登录
//         cy.visit('/profile')
//         cy.get('.profile-info').should('contain', 'testuser')
//     })

//     it('Test Case 2: Perform an action only for logged-in users', () => {
//         // 另一个测试用例，同样假设用户已登录
//         cy.visit('/dashboard')
//         cy.get('.dashboard').should('be.visible')
//     })
// })
