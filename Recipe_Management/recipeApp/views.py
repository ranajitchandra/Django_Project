from django.shortcuts import render, redirect
from recipeApp.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def signin_page(request):
    if request.method=="POST":
        user_name=request.POST.get('username')
        pass_word=request.POST.get('password')
        login_user=authenticate(username=user_name,password=pass_word,)
        login(request, login_user)
        
        return redirect('home_page')
    # HEll0
    
    return render(request, 'signin.html')

def logout_user(request):
    logout(request)
    return redirect('signin_page')

def signup_page(request):
    if request.method=="POST":
        display_name=request.POST.get('display_name')
        user_name=request.POST.get('username')
        pass_word=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        User_email=request.POST.get('email')
        age=request.POST.get('age')
        city=request.POST.get('city')
        country=request.POST.get('country')
        userType=request.POST.get('userType')
        gender=request.POST.get('gender')
        user_Image=request.FILES.get('user_Image')
        if pass_word==confirm_password:
            save_user=custom_user.objects.create_user(
                username=user_name,
                password=confirm_password,
                email=User_email,
            )
            save_user.display_name=display_name
            save_user.age=age
            save_user.city=city
            save_user.country=country
            save_user.user_type=userType
            save_user.gender=gender
            save_user.user_image=user_Image
            save_user.save()
            return redirect('signin_page')
    return render(request, 'signup.html')
@login_required
def add_recipe(request):
    if request.method=="POST":
        recipeTitle=request.POST.get('recipeTitle')
        ingredients=request.POST.get('ingredients')
        instructions=request.POST.get('instructions')
        preparationTime=request.POST.get('preparationTime')
        cookingTime=request.POST.get('cookingTime')
        totalTime=request.POST.get('totalTime')
        nutritionalInfo=request.POST.get('nutritionalInfo')
        difficultyLevel=request.POST.get('difficultyLevel')
        recipe_category=request.POST.get('recipe_category')
        Tag_type=request.POST.get('Tag_type')
        totalCalories=request.POST.get('totalCalories')
        recipeImage=request.FILES.get('recipeImage')
        
        save_data=add_recipe_model(
            recipeTitle=recipeTitle,
            ingredients=ingredients,
            instructions=instructions,
            preparationTime=preparationTime,
            cookingTime=cookingTime,
            totalTime=totalTime,
            nutritionalInfo=nutritionalInfo,
            difficultyLevel=difficultyLevel,
            recipe_category=recipe_category,
            Tag_type=Tag_type,
            totalCalories=totalCalories,
            recipeImage=recipeImage,
            created_by=request.user,
        )
        save_data.save()
        return redirect('view_recipe')
    
    return render(request, 'add_recipe.html')
@login_required
def view_recipe(request):
    view_recipe_data=add_recipe_model.objects.filter(created_by = request.user)
    
    return render(request, 'view_recipe.html', {'data' : view_recipe_data})

@login_required
def view2_recipe(request):
    view_recipe_data=add_recipe_model.objects.all()
    
    return render(request, 'view2.html', {'data' : view_recipe_data})

@login_required
def base(request):
    
    return render(request, 'base.html')
@login_required
def datele_recipe(request, recipe_id):
    delete_data=add_recipe_model.objects.get(id=recipe_id)
    delete_data.delete()
    return redirect('view_recipe')
@login_required
def edit_recipe(request, recipe_id):
    edit_data=add_recipe_model.objects.get(id=recipe_id)
    
    return render(request, 'edit_recipe.html', {'data' : edit_data})
@login_required
def update_recipe(request):
    if request.method=="POST":
        recipe_id=request.POST.get('recipe_id')
        recipeTitle=request.POST.get('recipeTitle')
        ingredients=request.POST.get('ingredients')
        instructions=request.POST.get('instructions')
        preparationTime=request.POST.get('preparationTime')
        cookingTime=request.POST.get('cookingTime')
        totalTime=request.POST.get('totalTime')
        nutritionalInfo=request.POST.get('nutritionalInfo')
        difficultyLevel=request.POST.get('difficultyLevel')
        recipe_category=request.POST.get('recipe_category')
        Tag_type=request.POST.get('Tag_type')
        totalCalories=request.POST.get('totalCalories')
        pre_recipeImage=request.POST.get('pre_recipeImage')
        recipeImage=request.FILES.get('recipeImage')
        if recipeImage==None:
            save_data=add_recipe_model(
                id=recipe_id,
                recipeTitle=recipeTitle,
                ingredients=ingredients,
                instructions=instructions,
                preparationTime=preparationTime,
                cookingTime=cookingTime,
                totalTime=totalTime,
                nutritionalInfo=nutritionalInfo,
                difficultyLevel=difficultyLevel,
                recipe_category=recipe_category,
                Tag_type=Tag_type,
                totalCalories=totalCalories,
                recipeImage=pre_recipeImage,
                created_by=request.user.username
            )
            save_data.save()
            return redirect('view_recipe')
        else:
            save_data=add_recipe_model(
                id=recipe_id,
                recipeTitle=recipeTitle,
                ingredients=ingredients,
                instructions=instructions,
                preparationTime=preparationTime,
                cookingTime=cookingTime,
                totalTime=totalTime,
                nutritionalInfo=nutritionalInfo,
                difficultyLevel=difficultyLevel,
                recipe_category=recipe_category,
                Tag_type=Tag_type,
                totalCalories=totalCalories,
                recipeImage=recipeImage,
                created_by=request.user.username
            )
            save_data.save()
            return redirect('view_recipe')
        
@login_required
def user_profile(request):
    return render(request, 'user_profile_page.html')

def home_page(request):
    return render(request, 'home.html')

def chef_profile_page(request):
    if request.user.user_type == 'chef':
        get_chef=chef_profile.objects.get()
    else:
        get_chef=viewer_profile.objects.get()
    
    return render(request, 'chef_profile.html', {'chef_profile':get_chef})
