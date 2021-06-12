from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class CandidatePageView(TemplateView):
    template_name = 'candidate.html'
