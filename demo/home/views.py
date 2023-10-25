from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.conf import settings
from home.models import Lang, Rattata
from home.forms import RattataForm, LangForm

# Create your views here.

# This is a little complex because we need to detect when we are
# running in various configurations


class HomeView(View):
    template = 'home/main.html'
    success_url = reverse_lazy('home:all')
    def get(self, request):
        form = RattataForm()
        ctx = {'form': form}
        return render(request, self.template, ctx)

    def post(self, request):
        form = RattataForm(request.POST)
        ctx = {'form': form}
        if not form.is_valid():
            return render(request, self.template, ctx)

        make = form.save()
        return redirect(self.success_url)
    
class LangView(View):
    template = 'home/main.html'
    success_url = reverse_lazy('home:all')
    def get(self, request):
        form = LangForm()
        ctx = {'form': form}
        return render(request, self.template, ctx)

    def post(self, request):
        form = LangForm(request.POST)
        ctx = {'form': form}
        if not form.is_valid():
            return render(request, self.template, ctx)

        make = form.save()
        return redirect(self.success_url)