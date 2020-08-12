from django.shortcuts import render, redirect

# import ther standard messages
from django.contrib import messages

# import the contact model
from .models import Contact

# import the send_mail module
from django.core.mail import send_mail


# Create your views here.
def contact(request):
    # return
    if request.method == 'POST':
        # print('HELLO')
        # return
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        message = request.POST['message']
        realtor_email = request.POST['realtor_email']

        # check if user has made an inquirey already
        if request.user.is_authenticated:
            user_id = request.user.id 
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already sumitted an inquiry regarding this listing')
                return redirect('/listings/'+listing_id)

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id )
        contact.save()

        # Send a mail via settings
        send_mail(
            'Property Listing Inquiry',
            'There has been an inquiry for '+ listing +'. Sign in to admin panel for details',
            'charlybrown@zenergize.co.za',
            [realtor_email, 'craig@yoyozi.com'],
            fail_silently=False
        )

        messages.success(request, 'Your inquiry is lodged, a realtor will get back to you soon')
        return redirect('/listings/'+listing_id)
