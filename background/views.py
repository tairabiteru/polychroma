from django.shortcuts import render
import random

from .models import Screen, Background


def index(request):
    return render(request, "index.html", {})


def image_get(request):
    for screen in Screen.objects.all():
        if screen.active is True:
            break
    else:
        raise ValueError("No active screen.")
    
    ctx = {'duration': int(screen.rotate_every.total_seconds())}

    images = Background.objects.all()
    image = random.choice(images)
    ctx['image_url'] = image.file.url
    response = render(request, "image.html", ctx)
    
    if screen.refresh is True:
        response.headers['HX-Refresh'] = "true"
        screen.refresh = False
        screen.save()

    return response


def clock_get(request):
    for screen in Screen.objects.all():
        if screen.active is True:
            break
    else:
        raise ValueError("No active screen.")

    return render(request, "clock.html", {'clock': screen.clock})
