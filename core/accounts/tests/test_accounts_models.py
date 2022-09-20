from django.test import TestCase
from accounts.models import User


class CustomUserTest(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(
            email="test@email.com", password="testpass123", username="test123", first_name="test",
            last_name="tester", phone_number="09011111111", image="default.png"
        )

        self.assertEqual(user.email, "test@email.com")
        self.assertEqual(user.username, "test123")
        self.assertEqual(user.get_full_name, "test tester")
        self.assertEqual(user.phone_number, "09011111111")
        self.assertEqual(user.role, "STU")
        self.assertFalse(user.is_active)
        self.assertFalse(user.email_verified)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        user = User.objects.create_superuser(
            email="testadmin@email.com", password="testpass123", username="testadmin123", first_name="testadmin",
            last_name="testeradmin", phone_number="09011111111", image="default.png"
        )

        self.assertEqual(user.email, "testadmin@email.com")
        self.assertEqual(user.username, "testadmin123")
        self.assertEqual(user.get_full_name, "testadmin testeradmin")
        self.assertEqual(user.phone_number, "09011111111")
        self.assertEqual(user.role, "STA")
        self.assertTrue(user.is_active)
        self.assertTrue(user.email_verified)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
