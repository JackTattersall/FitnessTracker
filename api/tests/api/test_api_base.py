from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
import simplejson


class ApiTestBase(APITestCase):

    def _require_login(self):
        self.client.login(username='test_user', email='test@test.com', password='testing')

    def setUp(self):
        # User to authenticate against
        User.objects.create_user('test_user', 'test@test.com', 'testing')

    def detail_authentication(self, url, pk, msg):
        # act
        # not authenticated
        response = self.client.get(reverse(url, kwargs={'pk': pk}))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN, msg=msg + ' detail not authenticated')

        # authenticated
        self._require_login()
        response = self.client.get(reverse(url, kwargs={'pk': pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=msg + ' detail authenticated')

    def list_authentication(self, url, msg):
        # act
        # not authenticated
        response = self.client.get(reverse(url))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN, msg=msg + ' list not authenticated')

        # authenticated
        self._require_login()
        response = self.client.get(reverse(url))
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=msg + ' list authenticated')

    def post_authentication(self, url, data, msg):
        # act
        # not authenticated
        response = self.client.post(reverse(url), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN, msg=msg + ' post not authenticated')

        # authenticated
        self._require_login()
        response = self.client.post(reverse(url), data)
        print(simplejson.loads(response.content))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, msg=msg + ' post authenticated')