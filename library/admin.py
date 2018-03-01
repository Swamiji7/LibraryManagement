from django.contrib import admin
from .models import books
from .models import cart
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

admin.site.register(books)

admin.site.register(cart)