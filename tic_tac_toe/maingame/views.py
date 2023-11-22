from django.shortcuts import render, HttpResponse
from maingame.models import feed_back

# Create your views here.

def home(request):
    return render(request, 'gamehome.html')

def about(request):
    return render(request, 'aboutme.html')

def play(request):
    return render(request, 'playgame.html')

def feedback(request):
    return render(request, 'feedback.html')

def asubmit(request):
    if request.method == "POST":
        feedback=feed_back()
        print("validation start")
        feed_scale=request.POST.get('choose')
        feed_text=request.POST.get('feed_text')
        feedback.feed_text=feed_text
        feedback.feed_scale=feed_scale
        feedback.save()
        print("data sent")
    return render(request, "feedbacksubmit.html")

