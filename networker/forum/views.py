from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render, render_to_response
from django.core.context_processors import csrf
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


from .models import *


# ---------------------------------------------------------------------listing
def forum_list(request):
	""" Forum Listing """
	forums = Forum.objects.get(pk=1)
	return render(request, 'forum/forum_list.html', {'forum': forums})


def thread_list(request, thread):
	""" Listing of threads in a forum """
	threads = Thread.objects.filter(forum__slug=thread)
	return render(request, 'forum/thread_list.html', {'threads': threads})


def post_list(request, thread, post):
	""" Listing of posts in a forum """
	posts = Post.objects.filter(thread__slug=post).order_by("-created")
	thread_title = Thread.objects.get(slug=post).title
	return render(request, 'forum/post_list.html', {'posts': posts, 'thread_title': thread_title})


# ----------------------------------------------------------------------create
class CreateThread(CreateView):
    """ Creates a thread for a forum """
    model = Thread
    fields = '__all__'
    # success_url = '/'
    title = 'add'
    section = 'Add New Topic'
    button = 'Add'

    def get_initial(self):
        return {
            'creator': self.request.user, 
            'forum': Forum
        }

    # def get_success_url(self):
    #     return reverse('listing_phone', kwargs={
    #         'pk': self.object.user_id.pk,
    #     })


# ----------------------------------------------------------------------unused
# def thread_list(request, pk):
# 	""" Listing of threads in a forum """
# 	threads = Thread.objects.filter(forum=pk).order_by("-created")
# 	threads = mk_paginator(request, threads, 20)

# 	# gets the specific thread
# 	def get_object(self, queryset=None):
# 	    return Thread.objects.get(pk=self.kwargs['thread'])
	
# 	return render(request, 'forum/thread_list.html', {'threads': threads, 'pk': pk})


# class ThreadListing(ListView):
#     """ Listing of threads in a forum """
#     model = Thread

#     # def get_success_url(self):
#     #     return reverse('post_list', kwargs={
#     #         'thread': self.object.pk,
#     #     })


# class PostListing(ListView):
#     """ Listing of posts in a thread """
#     model = Post
    

# def post_list_old(request, pk):
# 	""" Listing of posts in a thread """
# 	posts = Post.objects.filter(thread=pk).order_by('created')
# 	posts = mk_paginator(request, posts, 15)
# 	# title = Thread.objects.get(pk=pk).title
# 	# t = Thread.objects.get(pk=pk)

# 	# gets the specific thread
# 	def get_object(self, queryset=None):
# 	    return Thread.objects.get(pk=self.kwargs['thread'])

	# # gets the specific post
	# def get_object(self, queryset=None):
	#     return Post.objects.get(pk=self.kwargs['post'])

	# return render(request, 'forum/post_list.html', {'posts': posts, 'pk': pk})


# def post(request, ptype, pk):
# 	""" Displays a post form """ 
# 	action = reverse('views.{}'.format(ptype), args=[pk])
# 	if ptype == 'new_thread':
# 	    title = 'Start New Topic'
# 	    subject = ''
# 	elif ptype == 'reply':
# 	    title = 'Reply'
# 	    subject = 'Re: ' + Thread.objects.get(pk=pk).title

# 	return render('forum/post.html', add_csrf(request, subject=subject, action=action, title=title))


# def new_thread(request, pk):
# 	""" Start a new thread """
# 	p = request.POST
# 	if p['subject'] and p['body']:
# 	    forum = Forum.objects.get(pk=pk)
# 	    thread = Thread.objects.create(forum=forum, title=p['subject'], creator=request.user)
# 	    Post.objects.create(thread=thread, title=p['subject'], body=p['body'], creator=request.user)
# 	return HttpResponseRedirect(reverse('networker.networker.views.forum', args=[pk]))


# def reply(request, pk):
# 	""" Reply to a thread """
# 	p = request.POST
# 	if p['body']:
# 		thread = Thread.objects.get(pk=pk)
# 		post = Post.objects.create(thread=thread, title=p['subject'], body=p['body'],
# 	        creator=request.user)
# 	return HttpResponseRedirect(reverse('views.thread', args=[pk]) + '?page=last')


# def add_csrf(request, **kwargs):
# 	""" Add CSRF to dictionary """ 
# 	d = dict(user=request.user, **kwargs)
# 	d.update(csrf(request))
# 	return d


