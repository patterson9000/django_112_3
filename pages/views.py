from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'pages/index.html'


class AboutPagesView(TemplateView):
    template_name = 'pages/about.html'
