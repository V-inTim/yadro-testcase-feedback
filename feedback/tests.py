from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import FeedbackType, Feedback


class FeedbackAPITests(APITestCase):
    """Тесты на api обратной связи."""

    def setUp(self):
        self.type_problem = FeedbackType.objects.create(name="Проблема")
        self.url_feedback = reverse('feedback')
        self.url_types = reverse('feedback_types')

    def test_get_feedback_types(self):
        """Тест на получение типов."""
        response = self.client.get(self.url_types)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], "Проблема")

    def test_create_feedback_without_file(self):
        """Тест на создание без файла."""
        data = {
            "feedback_type": self.type_problem.id,
            "text": "Что-то не работает",
        }
        response = self.client.post(self.url_feedback, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Feedback.objects.count(), 1)

    def test_feedback_type_is_required(self):
        """Тест на отсутствие типа обращения."""
        data = {
            "text": "Отсутствует тип обращения"
        }
        response = self.client.post(self.url_feedback, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("feedback_type", response.data)
        self.assertEqual(Feedback.objects.count(), 0)
