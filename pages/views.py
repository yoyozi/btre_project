from django.shortcuts import render
from django.http import HttpResponse

# Add this to get the selection drop down lists in python dictionaries
# file choices in listing folder, then pass it into index.html to be used
# in the searching main bar
from listings.choices import price_choices, bedroom_choices, state_choices

# To get a list of listing from Listing model
from listings.models import Listing

# To get a list of listing from realtor model
from realtors.models import Realtor

# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
    }
    # passing into index.html
    return render(request, 'pages/index.html', context)
    #return HttpResponse('<h1>Hello World</h1>')

def about(request):
    # Get all the realtors and send to model and page
    realtors = Realtor.objects.order_by('-hire_date')

    # Get the mvp
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }

    return render(request, 'pages/about.html', context)

