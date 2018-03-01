from django.conf.urls import url

from library import views

app_name="library"

urlpatterns = [
    url(r'^$', views.index, name='base'),
    url(r'^register$', views.UserFormView.as_view(), name='register'),
    url(r'^login_user$', views.login_user, name='login_user'),
    url(r'^logout_user$', views.logout_user, name='logout_user'),
    url(r'^get_books$', views.get_books, name='get_books'),
    url(r'^add_to_cart$', views.add_to_cart, name='add_to_cart'),
    url(r'^cart', views.cart, name='cart'),
    url(r'^admin_page', views.admin_page, name='admin_page')
]