from django.test import TestCase, Client
from .models import Activity
from django.urls import reverse

class ActivityViewTestCase(TestCase):
    def setUp(self):
        # Create an instance of the Activity model
        Activity.objects.create(
            name="Test Activity",
            date="2022-01-01",
            time="12:00",
            description="A test activity",
            instructor=Activity.MATHEUS
        )
        # Set up the client to make requests
        self.client = Client()

    def test_activity_list_view(self):
        # Get the url for the activity list (change 'activity_list' to your actual url name)
        url = reverse('activity_list') 
        # Make a GET request to the list view
        response = self.client.get(url)
        # Check if the response is 200 OK
        self.assertEqual(response.status_code, 200)
        # Optionally, check if the response context contains your activities
        self.assertIn('Test Activity', response.context['activities'])
