import allure


def attach_screenshot(page, name="Screenshot"):
    screenshot = page.screenshot()

    allure.attach(
        screenshot,
        name=name,
        attachment_type=allure.attachment_type.PNG
    )