from django.contrib import admin

from polls.polls.models import Poll, Question, Variant


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    """Polls."""

    def get_readonly_fields(self, request, obj):  # noqa: WPS110
        """Add start_date to readonly fields if object exists."""
        if obj:
            return self.readonly_fields + ('start_date',)
        return self.readonly_fields


class VariantInline(admin.TabularInline):
    """Varinat."""

    model = Variant


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """Question."""

    inlines = [
        VariantInline,
    ]
