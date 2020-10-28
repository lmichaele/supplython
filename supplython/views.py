from django.views.generic import TemplateView

class BackorderPageView(TemplateView):
	template_name = 'backordermanagement.html'