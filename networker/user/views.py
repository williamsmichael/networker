from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

from .models import NetworkerUser
from .forms import UserForm, NetworkerUserForm


def index(request):
    """ Navigates to the index or home page """
    return render(request, 'networker/index.html', {})

def user_list(request):
    """ List of all users """

    users = NetworkerUser.objects.all()
    return render(request, 'user/user_list.html', {'users': users})

def register(request):
    """ Register a user """

	# A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':

        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        networker_user_form = NetworkerUserForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and networker_user_form.is_valid():

            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            # We also establish a link between the two model instances that we create. After creating a new User model instance, we reference it in the UserProfile instance with the line profile.user_extension = user. This is where we populate the user attribute of the UserProfileForm form
            profile = networker_user_form.save(commit=False)
            profile.user_extension = user

            # # Did the user provide a profile picture?
            # # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'profile_image' in request.FILES:

                profile.profile_image = request.FILES['profile_image']

            # Save the UserProfile model instance
            profile.save()

            # Update the variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print(user_form.errors, networker_user_form.errors)

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        networker_user_form = NetworkerUserForm()

    # Render the template depending on the context.
    return render(request, 'user/register.html', { 'user_form': user_form, 'networker_user_form': networker_user_form, 'registered': registered })

def user_login(request):
    """ Login for a user """

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
            # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
            # because the request.POST.get('<variable>') returns None, if the value does not exist,
            # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/users/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse('Your Networker account is disabled.')
        else:
            # Bad login details were provided. So we cannot log the user in.
            print("Invalid login details: {}, {}".format(username, password))
            return HttpResponse('Invalid login details supplied.')

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the 
        # blank dictionary object 
        return render(request, 'user/login.html', {})

@login_required
def restricted(request):
    """ Restricting Access with a Decorator """
    return HttpResponse("Since you are logged in, you can see this text!")

# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out
    logout(request)

    # Take the user back to the homepage
    return HttpResponseRedirect('/users/')


