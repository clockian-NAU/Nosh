from django.test import TestCase
from django.contrib.auth.models import User
from ..views import *
from ..models import Recipe


class ViewsTest(TestCase):

	def test_recipe_list(self):
		response = self.client.get('http://127.0.0.1:8000/')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'recipe/recipe_list.html')

	def test_search(self):
		response = self.client.get('http://127.0.0.1:8000/recipe/search/')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'recipe/search_results.html')
