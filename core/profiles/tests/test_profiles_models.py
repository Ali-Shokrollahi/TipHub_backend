from django.test import TestCase

from accounts.models import Staff, Student, Teacher
from profiles.models import StaffProfile, StudentProfile, TeacherProfile


class StudentProfileTest(TestCase):
    def setUp(self):
        self.user = Student.objects.create(email="teststudent@email.com", password="testpass123")

    def test_create_profile(self):
        student = StudentProfile.objects.create(user=self.user)
        self.assertEqual(student.user, self.user)


class TeacherProfileTest(TestCase):
    def setUp(self):
        self.user = Teacher.objects.create(email="testteacher@email.com", password="testpass123")

    def test_create_profile(self):
        teacher = TeacherProfile.objects.create(user=self.user, username="test_teacher", bio="I am teacher.",
                                                instagram="https://www.test.com/testingtestteacher/",
                                                github="https://www.test.com/testingtestteacher/",
                                                linkedin="https://www.test.com/testingtestteacher/",
                                                telegram="https://www.test.com/testingtestteacher/",
                                                website="https://www.test.com/",
                                                )
        self.assertEqual(teacher.user, self.user)
        self.assertEqual(teacher.bio, "I am teacher.")
        self.assertEqual(teacher.username, "test_teacher")
        self.assertEqual(teacher.instagram, "https://www.test.com/testingtestteacher/")
        self.assertEqual(teacher.github, "https://www.test.com/testingtestteacher/")
        self.assertEqual(teacher.linkedin, "https://www.test.com/testingtestteacher/")
        self.assertEqual(teacher.telegram, "https://www.test.com/testingtestteacher/")
        self.assertEqual(teacher.website, "https://www.test.com/")
        self.assertEqual(teacher.user, self.user)


class StaffProfileTest(TestCase):
    def setUp(self):
        self.user = Staff.objects.create(email="teststaff@email.com", password="testpass123")

    def test_create_profile(self):
        staff = StaffProfile.objects.create(user=self.user)
        self.assertEqual(staff.user, self.user)
