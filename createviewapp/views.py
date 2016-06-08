from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index_view(request):
    return HttpResponse("Files of the LaPress Family files in views are: Chucks portfolio, Summers page, and photos of Summer's big day")

def portfolio_view(request):
    return HttpResponse("Chuck's portfolio, including photos of the family")

def summers_page(request):
    return HttpResponse("Landing page for Summer's photo")

def summers_birthday_photos(request):
    return HttpResponse("Photo's from Summers big party June 12th")

def summers_blowing_out_candles(request):
    return HttpResponse("Landing page for full page big moment")



