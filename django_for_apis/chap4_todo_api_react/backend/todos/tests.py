from django.test import TestCase

from .models import Todo

# Create your tests here.
class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Todo.objects.create(title="first todo", body="a body here")  # that's where the data is created

    def test_title_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_name = "{}".format(todo.title)
        print("todo-object: \n", todo)
        print("title: " + expected_object_name)
        self.assertEqual(expected_object_name, "first todo")

    def test_body_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_name = "{}".format(todo.body)
        print("body: " + expected_object_name)
        self.assertEqual(expected_object_name, "a body here")
