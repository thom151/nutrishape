import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from .helpers import *
from .models import *

# Create your views here.


def index(request):
    if request.user.is_authenticated:
        all_threads = Thread.objects.filter(user=request.user)
    else:
        all_threads = []
    return render(request, "nutrition/index.html", {
        "hello": "hello world",
        "all_threads": all_threads
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "nutrition/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "nutrition/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "nutrition/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "nutrition/register.html")


@csrf_exempt
def chat(request):

    if request.method == "POST":
        data = json.loads(request.body)
        message = data.get("message", "")
        if data.get("thread", ""):
            print("got thread")
            thread = data.get("thread", "").strip()
            botResponse = sendMessage(message, thread)
            if botResponse["function_called"]:
                print("IT'S BEEN CALLED BABY!!")
                print(toJson(botResponse["bot_response"]))
                jsonObj = json.loads(toJson(botResponse["bot_response"]))
            else:
                print("no function called")
                jsonObj = botResponse["bot_response"]
            Response = {
                "Response": jsonObj,
                "thread": thread,
                "func_called": botResponse["function_called"]
            }
            return JsonResponse(Response)
        else:
            print("no thread")
            thread = createThread()
            addThread = Thread.objects.create(
                user=request.user, threads=thread)
            addThread.save()
            print("thread added")
            botResponse = sendMessage(message, thread)
            if botResponse["function_called"]:
                print("IT'S BEEN CALLED BABY!!")
                print(toJson(botResponse["bot_response"]))
                jsonObj = json.loads(toJson(botResponse["bot_response"]))
            else:
                print("no function called")
                jsonObj = botResponse["bot_response"]
            Response = {
                "Response": jsonObj,
                "thread": thread,
                "func_called": botResponse["function_called"]
            }
            return JsonResponse(Response)


@csrf_exempt
def getRecipe(request, food_id):
    # Given recipe data
    recipe = fsRecipe(food_id)

# Extracting basic recipe information
    recipe_name = recipe['recipe_name']
    recipe_image = recipe['recipe_images']['recipe_image']
    recipe_description = recipe['recipe_description']
    recipe_url = recipe['recipe_url']
    # Extracting servings, prep time, cooking time, and calories per serving

    servings = recipe['number_of_servings'],
    prep_time = recipe['preparation_time_min'],
    cook_time = recipe['cooking_time_min'],
    cal_per_ser = recipe['serving_sizes']['serving']['calories']

    # Extracting ingredients
    ingredients_list = [ingredient['ingredient_description']
                        for ingredient in recipe['ingredients']['ingredient']]

    # Extracting directions
    directions_list = [direction['direction_description']
                       for direction in recipe['directions']['direction']]

    # Extracting nutritional information
    nutrition_info = {
        'calories': recipe['serving_sizes']['serving']['calories'],
        'carbohydrates': recipe['serving_sizes']['serving']['carbohydrate'],
        'fat': recipe['serving_sizes']['serving']['fat'],
        'protein': recipe['serving_sizes']['serving']['protein'],
        'fiber': recipe['serving_sizes']['serving']['fiber'],
        'sugar': recipe['serving_sizes']['serving']['sugar'],
        'sodium': recipe['serving_sizes']['serving']['sodium']
    }

    # Example usage
    print(f"Recipe Name: {recipe_name}")
    print(f"Image URL: {recipe_image}")
    print(f"Description: {recipe_description}")
    print(f"Ingredients: {ingredients_list}")
    print(f"Directions: {directions_list}")
    print(f"Nutrition Info: {nutrition_info}")

    return render(request, "nutrition/recipe.html", {
        "name": recipe_name,
        "img_src": recipe_image,
        "description": recipe_description,
        "servings": servings,
        "prepTime": prep_time,
        "cookTime": cook_time,
        "calPerServing": cal_per_ser,
        "ingredients": ingredients_list,
        "directions": directions_list,
        "nutriInfo": nutrition_info,
        "recipe_url": recipe_url
    })
