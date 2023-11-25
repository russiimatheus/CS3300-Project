from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Activity

class ViewTests(TestCase):
    def setUp(self):
        # Create a test user and activity
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.activity = Activity.objects.create(
            name="Sample Activity",
            date="2021-01-01",
            time="10:00",
            description="Sample description",
            instructor=Activity.MATHEUS
        )

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_view_activities(self):
        response = self.client.get(reverse('view_activities'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'view_activities.html')

    def test_create_activity_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('create_activity'))
        self.assertEqual(response.status_code, 200)

    def test_edit_activity_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('edit_activity', args=(self.activity.id,)))
        self.assertEqual(response.status_code, 200)

    def test_delete_activity_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('delete_activity', args=(self.activity.id,)))
        self.assertEqual(response.status_code, 200)

    def test_register(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    # ... (other tests as necessary) ...
