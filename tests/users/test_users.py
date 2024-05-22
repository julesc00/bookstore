import pytest

from django.contrib.auth import get_user_model
from django.test import TestCase


class TestCustomUser(TestCase):
    def test_create_user(self):
        tmp_user = get_user_model()
        user = tmp_user.objects.create_user(
            username='will',
            email="test_user@email.com",
            password="testpass123")

        assert user.username == 'will'
        assert user.email == "test_user@email.com"
        assert user.is_active
        assert not user.is_staff
        assert not user.is_superuser

    def test_create_superuser(self):
        tmp_user = get_user_model()
        admin_user = tmp_user.objects.create_superuser(
            username='superadmin',
            email="superadmin@email.com",
            password="testpass123")

        assert admin_user.username == 'superadmin'
        assert admin_user.email == "superadmin@email.com"
        assert admin_user.is_active
        assert admin_user.is_staff
        assert admin_user.is_superuser
