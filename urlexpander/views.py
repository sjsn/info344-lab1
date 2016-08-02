from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.utils import timezone
import requests
from bs4 import BeautifulSoup
from .models import URL
from .forms import SearchForm

def url_list(request):
	urls = URL.objects.filter(date__lte = timezone.now()).order_by('-date')
	if request.method == "POST":
		form = SearchForm(request.POST)
		if form.is_valid():
			new_url = form.save(commit = False)
			new_url.date = timezone.now()
			response = requests.get(new_url)
			page = BeautifulSoup(response.content, "lxml")
			if page.title is not None:
				title = page.title.string
			else:
				title = "No Title Available"
			new_url.status = response.status_code
			new_url.final_url = response.url
			new_url.title = title
			new_url.save()
			return redirect('url_detail', pk = new_url.pk)	
	else:
		form = SearchForm
	return render(request, 'urlexpander/url_list.html', {'urls': urls, 'form': SearchForm})

def url_detail(request, pk):
	url = get_object_or_404(URL, pk = pk)
	return render(request, 'urlexpander/url_detail.html', {'url': url})

def delete_url(request, pk):
	url = get_object_or_404(URL, pk = pk)
	url.delete()
	return	HttpResponseRedirect('../')
