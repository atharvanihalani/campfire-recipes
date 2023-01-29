from django.shortcuts import render
from django.http import HttpRequest
def index(request: HttpRequest):
    """View function for home page of site."""

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context={})

def compute_score(recipe, input_ingredients):
    recipe_ingredients = recipe["ingredients"]
    score = 0
    for ingredient in input_ingredients:
        if ingredient in recipe_ingredients:
            score = score + 1
    return score
    

def searchpage(request: HttpRequest):
    food1 = request.GET['food-1']
    food2 = request.GET['food-2']
    food3 = request.GET['food-3']
    recipes = [{
        "ingredients": ["chicken","bell peppers"],
        "filename": "recipes/template.html",
        "name": "Grilled Chicken Fajitas"
    }, {
        "ingredients": ["asparagus"],
        "filename": "recipes/raw_asparagus.html",
        "name": "Just asparagus"
    }]
    search_results = [
        (compute_score(recipe, [food1, food2, food3]), recipe)
        for recipe 
        in recipes
    ]
    ordered_search_results=sorted(search_results, key=(lambda tuple: -tuple[0]))
    print(ordered_search_results)
    return render(request, 'search-page.html', context={
        "results": ordered_search_results
    })