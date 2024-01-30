from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here


class OIDCIntegrationTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse("oidc-op-login")
        self.logout_url = reverse("oidc-op-logout")

    def test_oidc_authentication(self):
        # Simulate the authentication process
        response = self.client.get(self.login_url)
        self.assertEqual(
            response.status_code, 302
        )  # Redirect to the OIDC provider for authentication

        # Follow the redirect to the OIDC provider's authentication page
        response = self.client.get(response.url)
        self.assertEqual(
            response.status_code, 200
        )  # Successfully reached the authentication page

        # Submit the authentication form with valid credentials
        login_data = {
            "username": "testuser",
            "password": "testpassword",
        }
        response = self.client.post(response.url, data=login_data)
        self.assertEqual(
            response.status_code, 302
        )  # Redirected back to the application after successful authentication

        # Access a protected view to verify authentication
        protected_url = reverse("protected-view")
        response = self.client.get(protected_url)
        self.assertEqual(
            response.status_code, 200
        )  # Successfully accessed the protected view

        # Perform logout
        response = self.client.get(self.logout_url)
        self.assertEqual(
            response.status_code, 302
        )  # Redirected to the OIDC provider for logout

        # Follow the redirect to the OIDC provider's logout page
        response = self.client.get(response.url)
        self.assertEqual(
            response.status_code, 200
        )  # Successfully reached the logout page

        # Verify that the user is logged out
        protected_url = reverse("protected-view")
        response = self.client.get(protected_url)
        self.assertEqual(
            response.status_code, 302
        )  # Redirected to the login page as user is logged out
