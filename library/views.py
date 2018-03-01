from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from library.forms import UserForm
from .models import books

def index(request):
    return render(request, 'index.html')

def login_user(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST["username"]
            password = request.POST["password"]

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'index.html',
                                  {'success_message' : 'Welcome Back'})
                else:
                    return render(request, 'login_user.html',
                                  {'error_message' : 'Your account has been disabled!'})
            else:
                return render(request, 'login_user.html',
                              {'error_message': 'Incorrect Username / Password!'})

    return render(request, 'login_user.html')


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        'form': form
    }
    return render(request, 'index.html',
                                  {'success_message' : 'Logged Out Successfully'})




class UserFormView(View):
    form_class = UserForm
    template_name = 'registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')

        return render(request, self.template_name, {'form':form})

@csrf_exempt
def get_books(request):
    name_of_book = request.POST['bookName']
    book_instance = books.objects.filter(book_name__contains = name_of_book)
    author_instance = books.objects.filter(author__contains = name_of_book)
    return render(request, 'index.html', {'book_list': book_instance, 'author_list': author_instance})

@csrf_exempt
def add_to_cart(request):
    bookCount = books.objects.count()
    return render(request, 'cart.html')

def cart(request):
    return render(request, 'cart.html')

def admin_page(request):
    return render(request, 'admin_page.html')
