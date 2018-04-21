from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Recipe
import unittest
import mock

class RecipeModelTest(TestCase):

	def create_recipe(self):
		password = 'mypassword'
		my_admin = User.objects.create_superuser('myuser', 'myemail@test.com', password)
		self.client.login(username=my_admin.username, password=password)

		title="Test"
		ingredients="Nothing1" 
		instructions="Nothing2"
		return Recipe.objects.create(author=my_admin,
									 title=title, 
									 ingredients=ingredients, 
									 instructions=instructions)

	def test_string_representation(self):
		testMock = mock.Mock()
		testMock.title = "Test"
		self.assertEqual(Recipe.__str__(testMock), "Test")

	def test_publish(self):
		testObject = self.create_recipe()
		self.assertTrue(isinstance(testObject, Recipe))
		testObject.publish()
		title = Recipe.objects.get(title='Test')
		self.assertEqual(title.title, 'Test')

