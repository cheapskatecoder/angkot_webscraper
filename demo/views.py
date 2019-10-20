import time
from .models import Routes
from django.shortcuts import render
from django.views import View
from .forms import DemoForm


# Create your views here.


class Demo(View):
    template_name = 'demo/demo.html'

    def get(self, request):
        form = DemoForm()
        return render(request, template_name=self.template_name, context={'form': form})

    def post(self, request):
        default_form = DemoForm()
        if request.method == "POST":
            form = DemoForm(request.POST)
            if form.is_valid():
                origin = form.cleaned_data.get('origin')
                destination = form.cleaned_data.get('destination')
                routes = Routes.objects.filter(origin=origin, destination=destination)
                if routes:
                    print(routes)
                    return render(request, template_name=self.template_name,
                                  context={"routes": routes, "form": default_form})
        print("bad one")
        return render(request, template_name=self.template_name, context={"form": default_form})
