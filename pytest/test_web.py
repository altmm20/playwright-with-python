from playwright.sync_api import Page
import pytest

def test_title(page:Page):
    page.goto("https://demo.playwright.dev/todomvc/#/")
    assert page.title() == "React • TodoMVC"

def test_author_name(page:Page):
    page.goto("https://demo.playwright.dev/todomvc/#/")
    assert (page.inner_text(selector="p:nth-of-type(2)>a")) is not 'Mahin'