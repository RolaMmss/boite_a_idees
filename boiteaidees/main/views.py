from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from .forms import SignupForm,LoginForm, IdeeForm
from .models import Idee


def hello(request):

    return HttpResponse(f"""
        <h1>Hello Django from container!</h1>
""")


def accueil(request):

    idees = Idee.objects.all()

    return render(request, 'main/accueil.html',{'liste_idee': idees})



# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             # Si le formulaire est valide on crée l'utilisateur
#             form.save()
#             # Et ensuite on le log
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('home')
        
#     else:
#         form = UserCreationForm()

#     return render(request, 'main/signup.html', context={'form': form})
#########################################################
def signup(request):
    """Create a signup page view for the app.

    Args:
        request (HttpRequest): The HTTP request.
    
    Returns:
        HttpResponse: The HTTP response with the rendered signup page.    """
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            return redirect('home')
    return render(request, 'main/signup.html', context={'form': form})
# ##############################################

# def log_in(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request.POST)
#         if form.is_valid():
#             # username = form.cleaned_data.get('username')
#             # password = form.cleaned_data.get('password1')
#             # user = authenticate(username=username, password=password)
#             user = authenticate(
#                 username=form.cleaned_data['username'],
#                 password=form.cleaned_data['password'],
#             )
        
#         if user is not None:
#             login(request, user)
#             message = f'Bonjour, {user.username}! Vous êtes connecté.'
#             return redirect('home')
#         else:
#             message = 'Identifiants invalides.'
#             form = AuthenticationForm()

#     return render(request, 'main/log_in.html', context={'form': form,'message':message})
#####################################################################
def log_in(request):
    """The function login_page takes a request object and renders the login.html template with a LoginForm instance and a message. If the request method is POST, the form is validated and the user is authenticated using the provided username and password. If the authentication is successful, the user is logged in and redirected to the home page. Otherwise, an error message is displayed.
        The coach is staff and may sign in with:
            Username: Dr.Django
            Password: passworddjango
    Parameters:
        request: the HTTP request object sent by the client.

    Returns: 
        HttpResponse object that represents the rendered response of the login.html template.
    """
    form = LoginForm()
    message= ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                message = f'Bonjour, {user.username}! Vous êtes connecté.'
                return redirect('home')
            else:
                message = 'Identifiants invalides.'
    return render(request, 'main/login.html', context={'form': form,'message':message})
#########################################################################""
def logout_user(request):
    """Log out the currently authenticated user and redirect them to the login page.

    Args:
        request: The HTTP request object.
    Returns:
        A redirect response to the login page.
    """
    logout(request)
    return redirect('login')
############################################################################
def creer_idee(request):
    if request.method == 'POST':
        form = IdeeForm(request.POST)
        if form.is_valid():
            # form.save()
            formulation=form.cleaned_data['formulation'],
            detail=form.cleaned_data['detail'],
            # sauveguarder l'idée
            idee = Idee.objects.create(
                formulation=formulation,
                detail=detail,
                auteur= request.user,
                )
            return redirect('liste')
    else:
        form = IdeeForm()
    return render(request, 'main/creer.html', {'form': form})

#############################

def idee_list(request):
    idee_list = Idee.objects.all()
    context = {'idee_list': idee_list}
    return render(request, 'main/liste.html', context)

######################################

def like_idee(request, idee_id):
    idee = get_object_or_404(Idee, id=idee_id)
    idee.likes += 1
    idee.save()
    return redirect('detail', idee_id=idee_id)