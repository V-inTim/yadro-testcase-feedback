from django.db import models


class FeedbackType(models.Model):
    """Модель типа обратной связи."""

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Feedback(models.Model):
    """Модель обратной связи."""

    feedback_type = models.ForeignKey(
        FeedbackType,
        on_delete=models.CASCADE,
        verbose_name="feeadback_type",
    )
    text = models.TextField(max_length=500)
    file = models.FileField(upload_to='documents/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"feedback №{self.id}"
