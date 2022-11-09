from django.shortcuts import render
from .models import Finch


finches = [
  Finch('Lolo', 'tabby', 'Kinda rude.', 3),
  Finch('Sachi', 'tortoiseshell', 'Looks like a turtle.', 0),
  Finch('Fancy', 'bombay', 'Happy fluff ball.', 4),
  Finch('Bonk', 'selkirk rex', 'Meows loudly.', 6)
]

# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def finches_index(request):
  finches = Finch.objects.all()
  return render(request, 'finches/index.html', { 'finches': finches })

def finches_detail(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
  return render(request, 'finches/detail.html', { 'finch': finch })