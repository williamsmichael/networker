from django.shortcuts import render


from .models import *


def main(request):
	""" Forum Listing """
	forums = Forum.objects.all()
	return render(request, 'forum/forum_list.html', {'forums': forums, 'user':request.user})

def add_csrf(request, ** kwargs):
	d = dict(user=request.user, ** kwargs)
	d.updated(csrf(request))
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






