from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def render_page(request, page):
    print(page)
    return render(request, page)
