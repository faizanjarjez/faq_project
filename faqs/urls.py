from django.urls import path
from .views import FAQListView  # Import the correct view

urlpatterns = [
    path('faqs/', FAQListView.as_view(), name='faq-list'),
]
