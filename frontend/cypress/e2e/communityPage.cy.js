describe('Community Page', () => {
    beforeEach(() => {
            cy.login()
        cy.visit('http://localhost:3000/community')
    })

    it('should display friends list when the "Friends" tab is clicked', () => {
        // Check that the friends list is displayed
        cy.contains('button', 'Friends').click()
        cy.get('.ListComponent').should('be.visible')
        cy.get('.UserListItemComponent').should('be.visible')
    })

    it('should remove a friend from the list when the remove button is clicked', () => {
        cy.contains('h4', 'My friends').should('be.visible')

        cy.get('.UserListItemComponent')
            .first()
            .find('button.remove-button')
            .click()
    })

    it('should look for email', () => {
        cy.get('#friend-email').type('test@example.com')
        cy.get('button').contains('Add').should('be.visible').and('be.enabled')
    })

    it('should display groups list when "Groups" button is clicked', () => {
        cy.contains('button', 'Groups').click()
        cy.get('.ListComponent').should('be.visible')
        cy.get('.GroupListItemComponent').should('be.visible')
    })

    it('should show the create group component when "+" button is clicked in groups view', () => {
        cy.contains('button', 'Groups').click()
        cy.contains('button', '+').click()
        cy.get('.CreateGroupComponent').should('be.visible')
    })

    it('should display the group details with expected buttons after creation', () => {
        cy.url().should('include', '/group')
        cy.get('button').contains('Leave').should('exist')
        cy.get('button').contains('Add routes').should('exist')
        cy.get('button').contains('Invite').should('exist')
    })
})
