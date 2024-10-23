from playwright.sync_api import Page, expect

def test_contact_with_valid_info(page: Page):
    page.goto("https://bootcamp-qa.github.io/portfolioqa/")
    page.get_by_test_id("email").click()
    page.get_by_test_id("email").fill("reyes@test.com")
    page.get_by_test_id("subject").select_option("informacion")
    page.get_by_test_id("message").click()
    page.get_by_test_id("message").fill("test information")
    page.get_by_label("Acepto la Política de").check()
    page.get_by_test_id("buttonsubmitform").click()
    expect(page.locator("body")).to_contain_text("Se ha registrado tu respuesta.")

def test_contact_invalid_email(page: Page):
    page.goto("https://bootcamp-qa.github.io/portfolioqa/")
    page.get_by_test_id("email").click()
    page.get_by_test_id("email").fill("reyes")
    page.get_by_test_id("email").press("Tab")
    page.get_by_test_id("subject").select_option("informacion")
    page.get_by_test_id("message").click()
    page.get_by_test_id("message").fill("test")
    page.get_by_label("Acepto la Política de").check()
    page.get_by_test_id("buttonsubmitform").click()
    expect(page.get_by_test_id("email")).to_be_visible()
