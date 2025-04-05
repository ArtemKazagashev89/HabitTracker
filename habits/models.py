from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from users.models import User

from .tasks import send_reminder


class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.CharField(verbose_name="Место", max_length=100, null=True, blank=True)
    time = models.TimeField(verbose_name="Время", null=True, blank=True)
    action = models.CharField(verbose_name="Действие", max_length=1000)
    sign_pleasant_habit = models.BooleanField(default=False)
    associated_habit = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL)
    periodicity = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(7)])
    reward = models.CharField(verbose_name="Вознаграждение", max_length=255, null=True, blank=True)
    complete_time = models.IntegerField(verbose_name="Время выполнения (в секундах)", null=True, blank=True)
    publicity_sign = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"

    def clean(self):
        if self.reward and self.associated_habit:
            raise ValidationError("Нельзя одновременно указывать вознаграждение и связанную привычку.")
        if self.complete_time and self.complete_time > 120:
            raise ValidationError("Время выполнения не должно превышать 120 секунд.")
        if self.associated_habit and not self.associated_habit.sign_pleasant_habit:
            raise ValidationError("Связанная привычка должна быть приятной.")
        if self.sign_pleasant_habit and (self.associated_habit or self.reward):
            raise ValidationError("Приятная привычка не может иметь связанную привычку или вознаграждение.")
        if self.periodicity < 1 or self.periodicity > 7:
            raise ValidationError("Периодичность должна быть от 1 до 7 дней.")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        send_reminder.apply_async((self.user.td_chat_id, self.action), eta=self.time)
