from django.shortcuts import render, redirect

# Bring in messages
from django.contrib import messages, auth

# Bring in the Django User model
from django.contrib.auth.models import User

# For Dashboard bring in the Contact model
from contacts.models import Contact

# Create your views here.
def register(request):
    if request.method == 'POST':
        # Register the user after successful form app
        # test message
        # messages.error(request, 'Testing error message')
        # return redirect('register')
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # check passwords match
        if password == password2:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is in use')
                    return redirect('register')
                else:
                    # Looks good so create the user
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    # login after registration can log in but prefer to register then login normally
                    # auth.login(request, user)
                    # messages.success(request, 'You are now registered and logged in')
                    # return redirect('register')

                    # Alternative prefered is:
                    user.save();
                    messages.success(request, 'You are now registered and can login')
                    return redirect('login')

        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else: 
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else: 
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You have logged out.')
        return redirect('index') # add import of redirect


def dashboard(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)

    context = {
        'contacts': user_contacts
    }

    return render(request, 'accounts/dashboard.html', context)


