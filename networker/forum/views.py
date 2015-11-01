from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.core.context_processors import csrf
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


from .models import *


def main(request):
	""" Forum Listing """
	forums = Forum.objects.all()
	return render(request, 'forum/forum_list.html', {'forums': forums, 'user': request.user})

def add_csrf(request, **kwargs):
	""" Add CSRF to dictionary """ 
	d = dict(user=request.user, **kwargs)
	d.update(csrf(request))
	return d

def mk_paginator(request, items, num_items):
	""" Create and return a paginator """
	paginator = Paginator(items, num_items)
	try: page = int(request.GET.get('page', '1'))
	except ValueError: page = 1

	try: 
		items = paginator.page(page)
	except (InvalidPage, Empty,Page):
		items = paginator.page(paginator.num_pages)
	return items

def forum(request, pk):
	""" Listing of threads in a forum """
	threads = Thread.objects.filter(forum=pk).order_by("-created")
	threads = mk_paginator(request, threads, 20)
	return render(request, 'forum/forum.html', add_csrf(request, threads=threads, pk=pk))
	

def thread(request, pk):
	""" Listing of posts in a thread """
	posts = Post.objects.filter(thread=pk).order_by('created')
	posts = mk_paginator(request, posts, 15)
	title = Thread.objects.get(pk=pk).title
	return render(request, 'forum/thread.html', add_csrf(request, posts=posts, title=title, media_url=MEDIA_URL))






