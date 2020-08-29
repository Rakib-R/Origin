from django.shortcuts import render
from listings.models import Listing
from django.views.generic import ListView ,DetailView,UpdateView

#  your views here.
def index(request):
    listing_num = Listing.objects.all()
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        "listings"  : listings,
        "listing_num" : listing_num
    }
    print(request.user)
    return render (request , "TESTING.html" ,context )

class PostListView(ListView ,):
    #self.kwarg.get(pk=pk)
    model = Listing
    template_name =" pages/index.html"
    context_object_name = "listings"

class PostDetailView(DetailView):
    model = Listing

def about(request):
    return render(request , 'pages/about.html')