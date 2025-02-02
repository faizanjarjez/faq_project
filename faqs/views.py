from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FAQ

class FAQListView(APIView):
    def get(self, request):
        lang = request.GET.get('lang', 'en')  # Default to English
        cache_key = f'faqs_{lang}'  # Cache key per language

        cached_faqs = cache.get(cache_key)
        if cached_faqs:
            return Response(cached_faqs)

        faqs = FAQ.objects.all()
        data = [{
            'question': getattr(faq, f'question_{lang}', faq.question),
            'answer': getattr(faq, f'answer_{lang}', faq.answer),
        } for faq in faqs]

        cache.set(cache_key, data, timeout=60 * 15)  # Cache for 15 min
        return Response(data)
