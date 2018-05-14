from django.test import TestCase

# Create your tests here.

from TimeTable.forms import Mechanic
from django.urls import reverse
from django.contrib.auth.models import User


class MechanicTest(TestCase):

    def setUp(self):
        # Create test users
        test_user1 = User.objects.create_user(username='testuser1', password='12345')
        test_user1.save()
        test_user2 = User.objects.create_user(username='testuser2', password='12345')
        test_user2.save()

    def test_redirect_if_not_logged_in(self):
        resp = self.client.get(reverse('mechanics'))
        self.assertRedirects(resp, '/accounts/login/?next=/mechanics/')

    def test_logged_in_uses_correct_template(self):
        login = self.client.login(username='testuser1', password='12345')
        resp = self.client.get(reverse('mechanics'))

        # Check our user is logged in
        self.assertEqual(str(resp.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(resp.status_code, 200)

        # Check we used correct template
        self.assertTemplateUsed(resp, 'mechanics.html')