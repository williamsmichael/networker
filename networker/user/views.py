from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from .models import *
from .forms import *


def index(request):
    """ Navigates to the index or home page """
    return render(request, 'index.html', {})


# -----------------------------------------------------------------------lists

class ListingUser(ListView):
    """ List of all users """
    model = NetworkerUser


class ListingPhone(ListView):
    """ List of all user phone """
    model = UserPhone
    title = 'phone'
    section = 'Phone'
    queryset = UserPhone.objects.select_related('user_id').all()

    def get_queryset(self):
        # import pdb; pdb.set_trace()
        # return UserPhone.objects.filter(user_id=self.request.user.networkeruser)
        return self.queryset.filter(user_id=self.request.user.networkeruser)


class ListingEmail(ListView):
    """ List of all user email """
    model = UserEmail
    title = 'email alternate'
    section = 'Alternate Email'
    queryset = UserEmail.objects.select_related('user_id').all()

    def get_queryset(self):
        # import pdb; pdb.set_trace()
        # return UserEmail.objects.filter(user_id=self.request.user.networkeruser)
        return self.queryset.filter(user_id=self.request.user.networkeruser)


class ListingAddress(ListView):
    """ List of all user address """
    model = UserAddress
    title = 'address'
    section = 'Address'
    queryset = UserAddress.objects.select_related('user_id').all()

    def get_queryset(self):
        # import pdb; pdb.set_trace()
        # return UserEmail.objects.filter(user_id=self.request.user.networkeruser)
        return self.queryset.filter(user_id=self.request.user.networkeruser)


# ---------------------------------------------------------------------details

def UserDetail(request, pk):
    """ Details of a user """
    # """ is_staff: List of all users """
    # if request.user.is_authenticated() and request.user.is_staff:
    # print(NetworkerUser.objects.all())
    # for networker_user in NetworkerUser.objects.all():
    #     print(networker_user.user_extension.first_name)
    # users = NetworkerUser.objects.all()
    # return render(request, 'user/user_detail.html', {'users': users})
    # else:
    #     return HttpResponse("Unauthorized Access!")

    user = get_object_or_404(NetworkerUser, pk=pk)
    return render(request, 'user/user_detail.html', {'member': user})


# ----------------------------------------------------------------------create

class CreatePhone(CreateView):
    """ Creates a phone number for user """
    model = UserPhone
    fields = '__all__'
    print('phone')
    # success_url = '/'
    title = 'add'
    section = 'Add Phone'
    button = 'create'

    def get_initial(self):
        return {
            'user_id': self.request.user
        }

    def get_success_url(self):
        return reverse('listing_phone', kwargs={
            'pk': self.object.user_id.pk,
        })


class CreateEmail(CreateView):
    """ Creates a email for user """
    model = UserEmail
    fields = '__all__'
    # success_url = '/users/'
    title = 'add'
    section = 'Add Email'
    button = 'create'

    def get_initial(self):
        return {
            'user_id': self.request.user
        }

    def get_success_url(self):
        return reverse('user_detail', kwargs={
            'pk': self.object.user_id.pk,
        })


class CreateAddress(CreateView):
    """ Creates a address for user """
    model = UserAddress
    fields = '__all__'
    # success_url = '/users/'
    title = 'add'
    section = 'Add'
    button = 'create'

    def get_initial(self):
        return {
            'user_id': self.request.user
        }

    def get_success_url(self):
        return reverse('user_detail', kwargs={
          'pk': self.object.user_id.pk,
        })


class CreateSocialMedia(CreateView):
    """ Creates a social media for user """
    model = UserSocialMedia
    fields = '__all__'
    # success_url = '/users/'
    title = 'add'
    section = 'Add'
    button = 'create'

    def get_initial(self):
        return {
            'user_id': self.request.user
        }

    def get_success_url(self):
        return reverse('user_detail', kwargs={
          'pk': self.object.user_id.pk,
        })


class CreateJob(CreateView):
    """ Creates a job for user """
    model = UserJob
    fields = '__all__'
    # success_url = '/users/'
    title = 'add'
    section = 'Add'
    button = 'create'

    def get_initial(self):
        return {
            'user_id': self.request.user
        }

    def get_success_url(self):
        return reverse('user_detail', kwargs={
          'pk': self.object.user_id.pk,
        })


class CreateSkill(CreateView):
    """ Creates a skill for user """
    model = UserSkill
    fields = '__all__'
    # success_url = '/users/'
    title = 'add'
    section = 'Add'
    button = 'create'

    def get_initial(self):
        return {
            'user_id': self.request.user
        }

    def get_success_url(self):
        return reverse('user_detail', kwargs={
          'pk': self.object.user_id.pk,
        })


# ----------------------------------------------------------------------update

class UserUpdateMain(UpdateView):
    """ Update auth-user details for a user """
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'is_active']
    # success_url = '.'
    section = "Main"
    title = 'update'
    button = 'update'

    def get_success_url(self):
        return reverse('update_main', kwargs={
            'pk': self.object.pk,
        })


class UserUpdateAdditional(UpdateView):
    """ Update networker-user-extension details for a user """
    model = NetworkerUser
    fields = '__all__'
    # success_url = '/users/'
    section = 'Additional'
    title = 'update'
    button = 'update'

    def get_success_url(self):
        return reverse('update_additional', kwargs={
            'pk': self.object.pk,
        })


class UserUpdateMembership(UpdateView):
    """ Update membership details for a user """
    model = User
    fields = ['groups']
    # success_url = '/users/'
    section = "Membership"
    title = 'update'
    button = 'update'

    def get_success_url(self):
        return reverse('update_membership', kwargs={
            'pk': self.object.pk,
        })


class UserUpdatePhone(UpdateView):
    """ Update phone details for a user """

    def get_object(self, queryset=None):
        return UserPhone.objects.get(pk=self.kwargs['phone'])

    model = UserPhone
    fields = '__all__'
    # success_url = '/users/'
    section = "Phone"
    title = 'update'
    button = 'update'

    def get_success_url(self):
        return reverse('listing_phone', kwargs={
            'pk': self.object.user_id.pk,
        })


class UserUpdateEmail(UpdateView):
    """ Update email details for a user """

    def get_object(self, queryset=None):
        return UserEmail.objects.get(pk=self.kwargs['email'])

    # fields = ['email_category_id', 'email']
    fields = '__all__'
    # success_url = '/users/'
    section = "Alternate Email"
    title = 'update'
    button = 'update'

    def get_success_url(self):
        return reverse('listing_email', kwargs={
            'pk': self.object.user_id.pk,
        })


class UserUpdateAddress(UpdateView):
    """ Update address details for a user """
    model = UserAddress
    fields = '__all__'
    # success_url = '/users/'
    section = "Address"
    title = 'update'
    button = 'update'

    def get_success_url(self):
        return reverse('listing_address', kwargs={
            'pk': self.object.user_id.pk,
        })


class UserUpdateSocialMedia(UpdateView):
    """ Update social media details for a user """
    model = UserSocialMedia
    fields = '__all__'
    # success_url = '/users/'
    section = "Social Media"
    title = 'update'
    button = 'update'

    def get_success_url(self):
        return reverse('user_detail', kwargs={
            'pk': self.object.pk,
        })


class UserUpdateJob(UpdateView):
    """ Update job details for a user """
    model = UserJob
    fields = '__all__'
    # success_url = '/users/'
    section = "Job"
    title = 'update'
    button = 'update'

    def get_success_url(self):
        return reverse('user_detail', kwargs={
            'pk': self.object.pk,
        })


class UserUpdateSkill(UpdateView):
    """ Update skill details for a user """
    model = UserSkill
    fields = '__all__'
    # success_url = '/users/'
    section = "Skill"
    title = 'update'
    button = 'update'

    def get_success_url(self):
        return reverse('user_detail', kwargs={
            'pk': self.object.pk,
        })


# --------------------------------------------------------------authentication

def register(request):
    """ Register a user """
    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration
    # succeeds.
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
            # We also establish a link between the two model instances that we
            # create. After creating a new User model instance, we reference it
            # in the UserProfile instance with the line profile.user_extension
            # = user. This is where we populate the user attribute of the
            # UserProfileForm form
            profile = networker_user_form.save(commit=False)
            profile.user_extension = user

            # # Did the user provide a profile picture?
            # # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'profile_image' in request.FILES:

                profile.profile_image = request.FILES['profile_image']

            # Save the UserProfile model instance
            profile.save()

            # Update the variable to tell the template registration was
            # successful.
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
    return render(request, 'user/register.html', {'user_form': user_form, 'networker_user_form': networker_user_form, 'registered': registered})


def user_login(request):
    """ Login for a user """

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
            # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
            # because the request.POST.get('<variable>') returns None, if the value does not exist,
            # while the request.POST['<variable>'] will raise key error
            # exception
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
                return HttpResponseRedirect('/')
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


# Use the login_required() decorator to ensure only those logged in can
# access the view.
@login_required
def user_logout(request):
    """ Logout functionality """
    # Since we know the user is logged in, we can now just log them out
    logout(request)

    # Take the user back to the homepage
    return HttpResponseRedirect('/')


# ----------------------------------------------------------------------unused

# class DeletePhone(DeleteView):
#     model = UserPhone
#     success_url = '/users/'
#     section = "Confirm"
#     button = "delete"


# class DeleteEmail(DeleteView):
#     model = UserEmail
#     success_url = '/users/'
#     section = "Confirm"
#     button = "delete"


# class DeleteAddress(DeleteView):
#     model = UserAddress
#     success_url = '/users/'
#     section = "Confirm"
#     button = "delete"

# class UserDelete(DeleteView):
#     model = NetworkerUser
#     success_url = '/users/'
#     section = "Confirm Delete"
#     button = "delete"

#     def get_success_url(self):
#         return reverse('user_detail', kwargs={
#             'pk': self.object.pk,
#         })


# def user_listing(request):
#     """ Simple list of all users """

#     users = NetworkerUser.objects.all()
#     return render(request, 'user/user_listing.html', {'users': users})


# class UpdateContactView(UpdateView):
#     model = NetworkerUser
#     template_name = 'user_edit.html'

#     def get_success_url(self):
#         return reverse('user_listing')

#     def get_context_data(self, **kwargs):
#         context = super(UpdateContactView, self).get_context_data(**kwargs)
#         context['action'] = reverse('user-edit', kwargs={'pk': self.get_object().id})
#         return context


# def user_detail_main(request, pk):
#     """ Details of a user section=MAIN """
#     user = get_object_or_404(NetworkerUser, pk=pk)
#     return render(request, 'user/user_detail_main.html', {'user': user})


# def user_detail_main_edit(request, pk):
#     """ Update user section=MAIN """
#     user = get_object_or_404(NetworkerUser, pk=pk)
#     if request.method == "POST":
#         form = UserDetailMainForm(request.POST, user=request.user)
#         if form.is_valid():
#             user = form.save()
#             return redirect('views.user_detail', pk=NetworkerUser.post)

#     else:
#         form = UserDetailMainForm(user=request.user)

#     return render(request, 'user/user_detail_main_edit.html', {'form': form})


# def user_new(request):
#     """ Makes a new user profile """
#     if request.method == "POST":
#         print(request.POST, 'before validation')
#         form = UserNewForm(request.POST or None)

#         if form.is_valid():
#             updated_data = form.save(commit=False)

#             updated_data.save() # actually saves it
#             print(updated_data, "after validation")
#             return redirect('/users/', pk=updated_data.pk)

#     else:
#         form = UserNewForm()

#     return render(request, 'user/user_new.html', {'form': form})


# def user_edit(request, pk):
#     """ Makes a new user profile """
#     updated_data = get_object_or_404(Updated_Data, pk=pk)
#     if request.method == "POST":
#         print(request.POST, 'before validation')
#         form = UserNewForm(request.POST or None, instance=updated_data)

#         if form.is_valid():
#             updated_data = form.save(commit=False)

#             updated_data.save() # actually saves it
#             print(updated_data, "after validation")
#             return redirect('/users/', pk=updated_data.pk)

#     else:
#         form = UserNewForm(instance=updated_data)

#     return render(request, "user/user_new.html", {'form': form})
