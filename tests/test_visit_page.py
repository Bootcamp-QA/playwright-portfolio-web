from playwright.sync_api import Page, expect

def test_visit(page: Page):
    page.goto("https://bootcamp-qa.github.io/portfolioqa/")

