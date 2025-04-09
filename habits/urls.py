from django.urls import path

from habits.apps import HabitsConfig
from habits.views import (HabitCreateApiView, HabitDestroyApiView, HabitListApiView, HabitRetrieveApiView,
                          HabitUpdateApiView, PublicHabitListApiView)

app_name = HabitsConfig.name

urlpatterns = [
    path("habit/create/", HabitCreateApiView.as_view(), name="habit-create"),
    path("habits/", HabitListApiView.as_view(), name="habit-list"),
    path("habit/<int:pk>/", HabitRetrieveApiView.as_view(), name="habit-detail"),
    path("habit/update/<int:pk>/", HabitUpdateApiView.as_view(), name="habit-update"),
    path("habit/delete/<int:pk>/", HabitDestroyApiView.as_view(), name="habit-delete"),
    path('habits/public/', PublicHabitListApiView.as_view(), name='public-habit-list'),
]
