from django.contrib.auth.models import User
from django.db import models


class Poll(models.Model):
    """Model Poll."""

    name = models.CharField(max_length=200)  # noqa: WPS432
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        """Represent model."""
        return f'{self.name} ({self.pk})'


class Question(models.Model):
    """Model Question."""

    types = [
        ('text', 'text'),
        ('single select', 'single select'),
        ('multiple select', 'multiple select'),
    ]
    poll = models.ManyToManyField(Poll, related_name='questions')
    text = models.TextField()
    type = models.CharField(
        choices=types, max_length=30,  # noqa: WPS432
    )

    def __str__(self) -> str:
        """Represent model."""
        return f'{self.text} ({self.type})'


class Variant(models.Model):
    """Model Variant."""

    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='variants',
    )
    text = models.CharField(max_length=200)  # noqa: WPS432

    def __str__(self) -> str:
        """Represent model."""
        return f'{self.text}'


class Answer(models.Model):
    """Model Answer."""

    user = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='users',
    )
    question = models.ForeignKey(
        Question, on_delete=models.PROTECT, related_name='questions',
    )
    variant = models.ForeignKey(
        Variant, on_delete=models.PROTECT, related_name='variants',
    )

    def __str__(self) -> str:
        """Represent model."""
        return f'{self.variant.text}'  # noqa: WPS237
