"""tacar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from core.views import home, cadastro_cliente, listagem_cliente, cadastro_veiculo, listagem_veiculo, cadastro_tabela, \
    listagem_tabela, Registrar, atualiza_cliente, exclui_cliente, exclui_veiculo, atualiza_veiculo, atualiza_tabela, \
    exclui_tabela, atualiza_fabricante, exclui_fabricante, listagem_fabricante, cadastro_fabricante, cadastro_rotativo, \
    listagem_rotativo, listagem_mensalista, cadastro_mensalista, exclui_mensalista, atualiza_mensalista, \
    atualiza_rotativo, exclui_rotativo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/registrar/', Registrar.as_view(), name='url_registrar'),
    path('captcha/', include("captcha.urls")),
    path('', home, name='url_principal'),
    path('cadastro_cliente/', cadastro_cliente, name='url_cadastro_cliente'),
    path('listagem_cliente/', listagem_cliente, name='url_listagem_cliente'),
    path('cadastro_veiculo/', cadastro_veiculo, name='url_cadastro_veiculo'),
    path('listagem_veiculo/', listagem_veiculo, name='url_listagem_veiculo'),
    path('cadastro_tabela/', cadastro_tabela, name='url_cadastro_tabela'),
    path('listagem_tabela/', listagem_tabela, name='url_listagem_tabela'),
    path('cadastro_fabricante/', cadastro_fabricante, name='url_cadastro_fabricante'),
    path('listagem_fabricante/', listagem_fabricante, name='url_listagem_fabricante'),
    path('atualiza_cliente/<int:id>/', atualiza_cliente, name='url_atualiza_cliente'),
    path('atualiza_veiculo/<int:id>/', atualiza_veiculo, name='url_atualiza_veiculo'),
    path('atualiza_tabela/<int:id>/', atualiza_tabela, name='url_atualiza_tabela'),
    path('atualiza_fabricante/<int:id>/', atualiza_fabricante, name='url_atualiza_fabricante'),
    path('exclui_cliente/<int:id>/', exclui_cliente, name='url_exclui_cliente'),
    path('exclui_veiculo/<int:id>/', exclui_veiculo, name='url_exclui_veiculo'),
    path('exclui_tabela/<int:id>/', exclui_tabela, name='url_exclui_tabela'),
    path('exclui_fabricante/<int:id>/', exclui_fabricante, name='url_exclui_fabricante'),
    path('cadastro_rotativo/', cadastro_rotativo, name='url_cadastro_rotativo'),
    path('listagem_rotativo/', listagem_rotativo, name='url_listagem_rotativo'),
    path('cadastro_mensalista/', cadastro_mensalista, name='url_cadastro_mensalista'),
    path('listagem_mensalista/', listagem_mensalista, name='url_listagem_mensalista'),
    path('exclui_mensalista/<int:id>/', exclui_mensalista, name='url_exclui_mensalista'),
    path('atualiza_mensalista/<int:id>/', atualiza_mensalista, name='url_atualiza_mensalista'),
    path('atualiza_rotativo/<int:id>/', atualiza_rotativo, name='url_atualiza_rotativo'),
    path('exclui_rotativo/<int:id>/', exclui_rotativo, name='url_exclui_rotativo'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)