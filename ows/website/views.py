from django.utils.timezone import datetime
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return render(
        request,
        'website/index.html',
        {
            'date': datetime.now()
        }
    )
