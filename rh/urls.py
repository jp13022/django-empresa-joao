from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('produtos/',views.produtos, name='produtos'),
    path('clientes/',views.clientes, name='clientes'),
    path('funcionarios/',views.funcionarios, name='funcionarios'),
   # A URL para a página do formulário
    # Ex: http://127.0.0.1:8000/contato/
    path('contato/', views.formulario_contato_view, name='contatos'),
    # A URL para onde o usuário é enviado após o sucesso
    # Ex: http://127.0.0.1:8000/contato/sucesso/
    path('contato/sucesso/', views.contato_sucesso_view, name='contato_sucesso'),
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.register, name='register'),
    path('produtos/', views.lista_produtos, name='lista_produtos'),
    path('clientes/', views.lista_clientes, name='lista_clientes'),

]
    

