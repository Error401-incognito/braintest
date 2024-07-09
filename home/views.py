from django.shortcuts import render
from .models import EntryTest
from .forms import VideoForm

# Create your views here.
def home_page(request):
    return render(request, "index.html", {})



def showvideo(request):

    firstvideo= EntryTest.objects.last()
    videofile = 0
    if firstvideo:
        videofile= firstvideo.testmaterials.url


    form= VideoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

    context= {'file_url': videofile,
              'form': form
              }

    return render(request, 'video.html', context)