from django.views.generic.base import TemplateView

# Create your views here.

class LandingView(TemplateView): 
	template_name = "base/index.html"

