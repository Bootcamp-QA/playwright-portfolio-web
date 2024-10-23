from playwright.sync_api import Page, expect


def test_check_header_info(page: Page):
    page.goto("https://bootcamp-qa.github.io/portfolioqa/")
    expect(page.get_by_test_id("headername")).to_contain_text("Reyes Diaz")
    expect(page.get_by_test_id("headertitle")).to_contain_text("Junior QA")
    expect(page.get_by_test_id("githublink")).to_be_visible()
    expect(page.get_by_test_id("linkedinlink")).to_be_visible()
    page.get_by_test_id("linkedinlink").click()