from django.contrib import admin

from .models import Feedback, FeedbackType

admin.site.register(Feedback)
admin.site.register(FeedbackType)
