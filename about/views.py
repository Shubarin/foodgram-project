from django.views.generic.base import TemplateView


class AboutAuthorView(TemplateView):
    template_name = 'about/about_author.html'


class AboutTechView(TemplateView):
    template_name = 'about/about_spec.html'
