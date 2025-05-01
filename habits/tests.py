from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="testuser@example.com", password="testpassword")
        login_success = self.client.login(email="testuser@example.com", password="testpassword")
        print(f"Login success: {login_success}")
        self.habit_url = reverse("habits:habit-list")

    def test_create_habit(self):
        data = {"action": "Прогулка", "time": "12:00", "place": "Парк", "periodicity": 1, "user": self.user.id}
        response = self.client.post(self.habit_url, data, format="json")
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.count(), 1)
        self.assertEqual(Habit.objects.get().action, "Прогулка")
