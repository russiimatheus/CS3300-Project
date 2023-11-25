from django.test import TestCase
from django.contrib.auth.models import User
from .models import Activity, Registration
from django.utils import timezone
import datetime

class ActivityModelTest(TestCase):
    def setUp(self):
        self.activity = Activity.objects.create(
            name="Yoga Class",
            date=timezone.now().date(),
            time=timezone.now().time(),
            description="A relaxing yoga session",
            instructor=Activity.MATHEUS
        )

    def test_activity_creation(self):
        self.assertTrue(isinstance(self.activity, Activity))
        self.assertEqual(self.activity.__str__(), self.activity.name)

    def test_activity_fields(self):
        self.assertEqual(self.activity.name, "Yoga Class")
        self.assertEqual(self.activity.description, "A relaxing yoga session")
        self.assertEqual(self.activity.instructor, Activity.MATHEUS)

class RegistrationModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('testuser', 'test@example.com', 'testpassword')
        self.activity = Activity.objects.create(
            name="Dance Class",
            date=timezone.now().date(),
            time=timezone.now().time(),
            description="Energetic dance session",
            instructor=Activity.MATIAS
        )
        self.registration = Registration.objects.create(
            user=self.user,
            activity=self.activity
        )

    def test_registration_creation(self):
        self.assertTrue(isinstance(self.registration, Registration))
        self.assertEqual(self.registration.__str__(), f"{self.user.username} - {self.activity.name}")

    def test_registration_link_to_user_and_activity(self):
        self.assertEqual(self.registration.user, self.user)
        self.assertEqual(self.registration.activity, self.activity)

