from django.test import TestCase


# Create your tests here.
class ExampleTest(TestCase):
    def test_example(self):
        math = 1+1
        self.assertEqual(math, 2, "Test")
