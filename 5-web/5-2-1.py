from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://ist256.com/fall2023/syllabus/")
    
    startelement = page.query_selector("h4#criteria-for-project-grade")
    nextelement = startelement.query_selector("~ *")
    
    bullet_elements = nextelement.query_selector_all("li")

    criteria = []
    for bullet_element in bullet_elements:
        criteria.append(bullet_element.inner_html())

    print(criteria)
    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
    
