"""
Tests for the Django admin modifiactions.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client


class AdminSiteTests(TestCase):
    """Tests for Django admin."""

    def setUp(self):
        """Create user and client."""

        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email="admin@example.com",
            password="adminpassword123"
        )
        self.client.force_login(self.admin_user)

        users_details = [
            ("user1@example.com", "userpass1", "Test User 1"),
            ("user2@example.com", "userpass2", "Test User 2"),
            ("user3@example.com", "userpass3", "Test User 3"),
        ]

        email, password, username = users_details[0]
        self.user = get_user_model().objects.create_user(
            email=email,
            password=password,
            name=username,
        )

    def test_users_list(self):
        """Test that users are listed on the page."""

        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)
