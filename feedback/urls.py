from django.urls import path

from .views import FeedbackTypeView, FeedbackView

urlpatterns = [
    path('types/', FeedbackTypeView.as_view(), name='feedback_types'),
    path('', FeedbackView.as_view(), name='feedback'),
]
