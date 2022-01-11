from django.contrib import admin

from polls.polls.models import Poll, Question, Variant


class QuestionInline(admin.TabularInline):
    """Question inline."""

    model = Question.poll.through


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    """Polls."""

    inlines = [
        QuestionInline,
    ]

    def get_readonly_fields(self, request, obj):  # noqa: WPS110
        """Add start_date to readonly fields if object exists."""
        if obj:
            return self.readonly_fields + ('start_date',)
        return self.readonly_fields


class VariantInline(admin.TabularInline):
    """Varinat inline."""

    model = Variant


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """Question."""

    inlines = [
        VariantInline,
    ]
    exclude = [
        'poll',
    ]
