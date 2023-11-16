from django.shortcuts import render
from django.views import View


class Index(View):
    template_name = 'index.html'

    def get(self, request):
        user = request.user
        return render(request=request, template_name=self.template_name)