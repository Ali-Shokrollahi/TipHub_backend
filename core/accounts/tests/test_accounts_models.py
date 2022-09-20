from django.test import TestCase

from accounts.models import Staff, Student, Teacher, User, rename_profile


class CustomUserTest(TestCase):

    def setUp(self):
        User.objects.create_user(
            email="teststudent@email.com", password="testpass123", first_name="test",
            last_name="tester", phone_number="09011111111", image="default.png"
        )
        User.objects.create_user(
            email="testteacher@email.com", password="testpass123", first_name="test",
            last_name="tester", phone_number="09011111112", image="default.png", role="TEA"
        )
        User.objects.create_user(
            email="teststaff@email.com", password="testpass123", first_name="test",
            last_name="tester", phone_number="09011111113", image="default.png", role="STA"
        )

    def test_student_user(self):
        user = Student.objects.get(email="teststudent@email.com")

        self.assertEqual(user.email, "teststudent@email.com")
        self.assertEqual(user.get_full_name, "test tester")
        self.assertEqual(user.phone_number, "09011111111")
        self.assertEqual(user.image, "default.png")
        self.assertEqual(user.role, "STU")
        self.assertFalse(user.is_active)
        self.assertFalse(user.email_verified)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertEqual(user.extra.user.email, "teststudent@email.com")
        self.assertEqual(user.extra.user.id, user.id)

    def test_teacher_user(self):
        user = Teacher.objects.get(email="testteacher@email.com")

        self.assertEqual(user.email, "testteacher@email.com")
        self.assertEqual(user.get_full_name, "test tester")
        self.assertEqual(user.phone_number, "09011111112")
        self.assertEqual(user.image, "default.png")
        self.assertEqual(user.role, "TEA")
        self.assertFalse(user.is_active)
        self.assertFalse(user.email_verified)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertEqual(user.extra.user.email, "testteacher@email.com")
        self.assertEqual(user.extra.user.id, user.id)

    def test_staff_user(self):
        user = Staff.objects.get(email="teststaff@email.com")

        self.assertEqual(user.email, "teststaff@email.com")
        self.assertEqual(user.get_full_name, "test tester")
        self.assertEqual(user.phone_number, "09011111113")
        self.assertEqual(user.image, "default.png")
        self.assertEqual(user.role, "STA")
        self.assertFalse(user.is_active)
        self.assertFalse(user.email_verified)
        self.assertTrue(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertEqual(user.extra.user.email, "teststaff@email.com")
        self.assertEqual(user.extra.user.id, user.id)

    def test_rename_profile(self):
        filename = "ali.sh.jpg"
        instance = Student.objects.get(email="teststudent@email.com")
        result = rename_profile(filename=filename, instance=instance)
        self.assertEqual(result, "profiles/teststudent@email.com.jpg")

    def test_create_superuser(self):
        user = User.objects.create_superuser(
            email="testadmin@email.com", password="testpass123", first_name="testadmin",
            last_name="testeradmin", phone_number="09011111114", image="default.png"
        )

        self.assertEqual(user.email, "testadmin@email.com")
        self.assertEqual(user.get_full_name, "testadmin testeradmin")
        self.assertEqual(user.phone_number, "09011111114")
        self.assertEqual(user.role, "STA")
        self.assertTrue(user.is_active)
        self.assertTrue(user.email_verified)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email="testadmin1@email.com", password="testpass123", is_superuser=False
            )
