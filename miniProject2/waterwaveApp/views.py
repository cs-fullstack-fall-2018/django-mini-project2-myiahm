from django.shortcuts import render

from django.http import HttpResponse
from .models import UserPlaylist


def index(request):
    latest_playlist = UserPlaylist.objects.all()
    context = {'latest_playlist': latest_playlist}
    return render(request, 'waterwaveApp/index.html', context)
