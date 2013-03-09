from django.contrib import admin

from models import Result, Feedback


class FeedbackInline(admin.TabularInline):
    model = Feedback
    extra = 1


class ResultAdmin(admin.ModelAdmin):
    inlines = [FeedbackInline]
    list_display = ("date", "short_input", "success")
    list_filter = ["date", "success"]
    search_fields = ["input_text", "output_text"]


admin.site.register(Result, ResultAdmin)