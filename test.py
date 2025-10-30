from django.test import TestCase

class SimpleTest(TestCase):
    def test_addition(self):
        """Проверка, что тесты работают"""
        self.assertEqual(1 + 1, 2)
