import pytest
from playwright.sync_api import Playwright


class Test_Actions_Ex1:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, playwright: Playwright):
        global browser, context, page
        browser = playwright.chromium.launch(headless=False, channel="chrome")
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://atidcollege.co.il/Xamples/ex_actions.html")

    def test01_drag_and_drop(self):
        print(f"\ntext before drop: {page.locator('#droppable').inner_text()}")
        page.drag_and_drop("#draggable", "#droppable", force=True)
        print(f"text after drop: {page.locator('#droppable').inner_text()}")
        assert page.locator('#droppable').inner_text() == "Dropped!"

    def test02_select_elements(self):
        page.locator(" li:nth-child(2)").click()
        page.keyboard.down("Control")
        page.locator(" li:nth-child(3)").click()
        page.keyboard.up("Control")

    def test03_double_click(self):
        page.locator("#dbl_click").dblclick()
        print(f"\n{page.locator('#demo').inner_text()}")
        assert page.locator('#demo').inner_text() == "Hello World"

    def test04_mouse_hover(self):
        element = page.locator("[id='mouse_hover']")
        print(element.get_attribute("style"))
        page.mouse.move(element.bounding_box()["x"], element.bounding_box()["y"])
        print(element.get_attribute("style"))
        assert element.get_attribute("style") == "background-color: rgb(255, 255, 0);"

    def test05_scroll_down(self):
        text_element = "This Element is Shown When Scrolled"
        page.locator("#scrolled_element").scroll_into_view_if_needed()
        print(f"\nThe text of element at the bottom is: {page.locator('#scrolled_element').inner_text()}")
        assert page.locator('#scrolled_element').inner_text() == text_element
