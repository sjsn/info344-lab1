from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import URL
from .forms import SearchForm

def url_list(request):
	urls = URL.objects.filter(date__lte = timezone.now()).order_by('-date')
	if request.method == "POST":
		form = SearchForm(request.POST)
		if form.is_valid():
			url = form.save(commit = False)
			url.date = timezone.now()
			url.save()
			return redirect('url_detail', pk = url.pk)
	else:
		form = SearchForm
	return render(request, 'urlexpander/url_list.html', {'urls': urls, 'form': SearchForm})

def url_detail(request, pk):
	url = get_object_or_404(URL, pk = pk)
	return render(request, 'urlexpander/url_detail.html', {'url': url})