from http import HTTPStatus

import pytest
from django.test import TestCase
from django.urls import reverse, resolve

from pages.views import HomePageView


class TestHomePageView(TestCase):
    def setUp(self):
        self.response = self.client.get(reverse("pages:home"))

    def test_home_page_status_code(self):
        assert self.response.status_code == HTTPStatus.OK

    def test_homepage_url_name(self):
        assert self.response.status_code == HTTPStatus.OK
        assert "home.html" in self.response.template_name

    def test_homepage_template(self):
        assert "home.html" in self.response.template_name
        assert "_base.html" in self.response.template_name

    def test_homepage_contains_correct_html(self):
        assert "Welcome to the Bookstore" in str(self.response.content)

    def test_homepage_does_not_contain_incorrect_html(self):
        assert "Hi there! I should not be on the page" not in str(self.response.content)
