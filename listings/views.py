from django.shortcuts import render
from .models import Listing

def index(request):
    listings = Listing.objects.all()

    context ={
        'listings': listings
    }
    render(request, "listings/listings.html" ,context)

def listing (request ,listing_id):
    listing = Listing.objects.get(id =listing_id)
    context ={
        "listing ": listing
    }
    render (request ,"listings/l_of_listings.html" ,context)

def search(request):
    render (request , "listings/search.html")
