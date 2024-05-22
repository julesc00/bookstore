from django.views.generic import TemplateView


class HomePageView(TemplateView):
    """Left at page 92 of the book"""
    template_name = "pages/home.html"
