describe('I can visit the website', () => {
  it('passes', () => {
    cy.visit('http://localhost:3000/')
  })
})

describe('a passing test', () => {
  it('Does not do much!', () => {
    expect(true).to.equal(true)
  })
})