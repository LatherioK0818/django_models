from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Snack

class SnackTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        test_user = get_user_model().objects.create_user(username='tester', password='pass')
        test_user.save()
        Snack.objects.create(name='Chocolate', purchaser=test_user, description='Sweet, dark, and rich.')

    def test_snack_content(self):
        snack = Snack.objects.get(id=1)
        expected_object_name = f'{snack.name}'
        expected_object_description = f'{snack.description}'
        self.assertEqual(expected_object_name, 'Chocolate')
        self.assertEqual(expected_object_description, 'Sweet, dark, and rich.')

    def test_snack_list_view(self):
        response = self.client.get(reverse('snack_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Chocolate')
        self.assertTemplateUsed(response, 'snack_list.html')

    def test_snack_detail_view(self):
        response = self.client.get(reverse('snack_detail', args='1'))
        no_response = self.client.get('/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Chocolate')
        self.assertTemplateUsed(response, 'snack_detail.html')

