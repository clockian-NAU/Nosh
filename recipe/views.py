from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import Recipe
from .forms import RecipeForm
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.contrib.auth.views import login
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q
import operator
import re

# Create your views here.
def recipe_list(request):
	recipes = Recipe.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'recipe/recipe_list.html', {'recipes': recipes})

def recipe_detail(request, pk):
	recipe = get_object_or_404(Recipe, pk=pk)
	return render(request, 'recipe/recipe_detail.html', {'recipe': recipe})

def recipe_new(request):
	if request.method == "POST":
		form = RecipeForm(request.POST, request.FILES)

		if form.is_valid():
			recipe = form.save(commit=False)
			recipe.author = request.user
			recipe.published_date = timezone.now()
			recipe.save()
			return redirect('recipe_detail', pk=recipe.pk)
	else:
		form = RecipeForm()

	return render(request, 'recipe/recipe_edit.html', {'form': form})

def recipe_edit(request, pk):
	recipe = get_object_or_404(Recipe, pk=pk)
	if request.method == "POST":
		form = RecipeForm(request.POST, request.FILES, instance=recipe)
		if form.is_valid():
			recipe = form.save(commit=False)
			recipe.author = request.user
			recipe.published_date = timezone.now()
			recipe.save()
			return redirect('recipe_detail', pk=recipe.pk)
	else:
		form = RecipeForm(instance=recipe)
	return render(request, 'recipe/recipe_edit.html', {'form': form})

def loginView(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request,user)
			return redirect('recipe_list.html')
	else:
		form = AuthenticationForm()
		return render(request, 'login.html',{'form':form})

def search(request):
	query_string = ''
	found_entries = None

	if ('q' in request.GET) and request.GET['q'].strip():
		query_string = request.GET['q']
		entry_query = get_query(query_string, ['title', 'ingredients',])
		found_entries = Recipe.objects.filter(entry_query).order_by('-published_date')
	return render(request, 'recipe/search_results.html',
		{ 'query_string': query_string, 'found_entries': found_entries})

# Support Function
def normalize_query(query_string,
					findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
					normspace=re.compile(r'\s{2,}').sub):
	return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)]

def get_query(query_string, search_fields):
	query = None
	terms = normalize_query(query_string)
	for term in terms:
		or_query = None
		for field_name in search_fields:
			q = Q(**{"%s__icontains" % field_name: term})
			if or_query is None:
				or_query = q
			else:
				or_query = or_query | q
		if query is None:
			query = or_query
		else:
			query = query & or_query
	return query

