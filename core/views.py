import form as form
from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

from core.forms import FormCliente, FormVeiculo, FormFabricante, FormTabelaPreco, FormRotativo, FormMensalista
from core.models import Cliente, Veiculo, Fabricante, TabelaPreco, Rotativo, Mensalista
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.

def home(request):
    return render(request, 'core/index.html')


class Registrar(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('url_principal')
    template_name = 'registration/registrar.html'


@login_required
def cadastro_cliente(request):
    if request.user.is_staff:
        form = FormCliente(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente cadastrado com sucesso')
            return redirect('url_listagem_cliente')
        contexto = {'form': form, 'txt_title': 'cad_cliente', 'txt_descricao': 'Cadastro de Cliente',
                    'txt_button': 'Cadastrar'}
        return render(request, 'core/cadastro.html', contexto)
    return render(request, 'core/mensagem.html')


@login_required
def listagem_cliente(request):
    if request.POST and request.POST['input_pesquisa']:
        dados = Cliente.objects.filter(nome__contains=request.POST['input_pesquisa'])
    else:
        dados = Cliente.objects.all()

    contexto = {'dados': dados, 'txt': 'Digite o nome do cliente', 'listagem':True}
    return render(request, 'core/listagem_cliente.html', contexto)


def atualiza_cliente(request, id):
    obj = Cliente.objects.get(id=id)
    form = FormCliente(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request, 'Cliente atualizado com sucesso')
        return redirect('url_listagem_cliente')
    contexto = {'form': form, 'txt_title': 'AtualizaCliente', 'txt_button': 'Atualizar'}
    return render(request, 'core/cadastro.html', contexto)


def exclui_cliente(request, id):
    if request.user.is_staff:
        obj = Cliente.objects.get(id=id)
        contexto = {'txt_msg': obj.nome, 'txt_url': '/listagem_cliente/'}
        if request.POST:
            obj.delete()
            messages.success(request, 'Cliente excluido com sucesso')
            contexto.update({'txt_tipo': 'Cliente'})
            return render(request, 'core/mensagem_exclusao.html', contexto)
        else:
            return render(request, 'core/confirma_exclusao.html', contexto)
    return render(request, 'core/mensagem.html')


def cadastro_veiculo(request):
    if request.user.is_staff:
        form = FormVeiculo(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()

            return redirect('url_listagem_veiculo')
        contexto = {'form': form, 'txt_title': 'cad_veic', 'txt_descricao': 'Cadastro de Veiculo',
                    'txt_button': 'Cadastrar'}
        return render(request, 'core/cadastro.html', contexto)
    return render(request, 'core/mensagem.html')


def listagem_veiculo(request):
    if request.POST and request.POST['input_pesquisa']:
        dados = Veiculo.objects.filter(nome__contains=request.POST['input_pesquisa'])
    else:
        dados = Veiculo.objects.all()
    contexto = {'dados': dados, 'txt': 'Pesquise um veiculo', 'listagem':True}
    return render(request, 'core/listagem_veiculo.html', contexto)


def atualiza_veiculo(request, id):
    obj = Veiculo.objects.get(id=id)
    form = FormVeiculo(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('url_listagem_veiculo')
    contexto = {'form': form, 'txt_title': 'AtualizaVeiculo', 'txt_button': 'Atualizar'}
    return render(request, 'core/cadastro.html', contexto)


def exclui_veiculo(request, id):
    obj = Veiculo.objects.get(id=id)
    obj.delete()
    return redirect('url_listagem_veiculo')
    contexto = {'obj': obj, 'txt_title': 'ExcluiVeiculo', 'txt_button': 'Excluir'}
    return render(request, 'core/listagem_veiculo.html', contexto)


def cadastro_tabela(request):
    if request.user.is_staff:
        form = FormTabelaPreco(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('url_listagem_tabela')
        contexto = {'form': form, 'txt_title': 'Cadastro de Tabela', 'txt_descricao': 'Cadastro de Tabela',
                    'txt_button': 'Cadastrar'}
        return render(request, 'core/cadastro.html', contexto)
    return render(request, 'core/mensagem.html')
    return render(request, 'core/cadastro_tabela.html')


def listagem_tabela(request):
    dados = TabelaPreco.objects.all()
    contexto = {'dados': dados, 'listagem':True}
    return render(request, 'core/listagem_tabela.html', contexto)


def atualiza_tabela(request, id):
    obj = TabelaPreco.objects.get(id=id)
    form = FormTabelaPreco(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('url_listagem_tabela')
    contexto = {'form': form, 'txt_title': 'Atualiza Tabela', 'txt_button': 'Atualizar'}
    return render(request, 'core/cadastro.html', contexto)


def exclui_tabela(request, id):
    obj = TabelaPreco.objects.get(id=id)
    obj.delete()
    return redirect('url_listagem_tabela')
    contexto = {'obj': obj, 'txt_title': 'Exclui Tabela', 'txt_button': 'Excluir'}
    return render(request, 'core/listagem_tabela.html', contexto)


def cadastro_fabricante(request):
    if request.user.is_staff:
        form = FormFabricante(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('url_listagem_fabricante')
        contexto = {'form': form, 'txt_title': 'Cadastro de Fabricante', 'txt_descricao': 'Cadastro de Fabricante',
                    'txt_button': 'Cadastrar'}
        return render(request, 'core/cadastro.html', contexto)
    return render(request, 'core/mensagem.html')


def listagem_fabricante(request):
    dados = Fabricante.objects.all()
    contexto = {'dados': dados, 'listagem':True}
    return render(request, 'core/listagem_fabricante.html', contexto)


def atualiza_fabricante(request, id):
    obj = Fabricante.objects.get(id=id)
    form = FormFabricante(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('url_listagem_fabricante')
    contexto = {'form': form, 'txt_title': 'Atualiza Fabricante', 'txt_button': 'Atualizar'}
    return render(request, 'core/cadastro.html', contexto)


def exclui_fabricante(request, id):
    obj = Fabricante.objects.get(id=id)
    obj.delete()
    return redirect('url_listagem_fabricante')
    contexto = {'obj': obj, 'txt_title': 'Exclui Fabricante', 'txt_button': 'Excluir'}
    return render(request, 'core/listagem_fabricante.html', contexto)


def cadastro_rotativo(request):
    if request.user.is_staff:
        form = FormRotativo(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('url_listagem_rotativo')
        contexto = {'form': form, 'txt_title': 'Cadastro de Rotativos', 'txt_descricao': 'Cadastro de Rotativos',
                    'txt_button': 'Cadastrar'}
        return render(request, 'core/cadastro_rotativo_dividido.html', contexto)
    return render(request, 'core/mensagem.html')


def listagem_rotativo(request):
    dados = Rotativo.objects.all()
    contexto = {'dados': dados, 'listagem':True}
    return render(request, 'core/listagem_rotativo.html', contexto)


def atualiza_rotativo(request, id):
    obj = Rotativo.objects.get(id=id)
    form = FormRotativo(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        obj.calcula_total()
        form.save()
        return redirect('url_listagem_rotativo')
    else:
        contexto = {'form': form, 'txt_title': 'Atualiza Rotativo', 'txt_button': 'Atualizar'}
        return render(request, 'core/cadastro.html', contexto)


def exclui_rotativo(request, id):
    obj = Rotativo.objects.get(id=id)
    obj.delete()
    return redirect('url_listagem_rotativo')
    contexto = {'obj': obj, 'txt_title': 'Exclui Rotativo', 'txt_button': 'Excluir'}
    return render(request, 'core/listagem_rotativo.html', contexto)


def cadastro_mensalista(request):
    if request.user.is_staff:
        form = FormMensalista(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('url_listagem_mensalista')
        contexto = {'form': form, 'txt_title': 'Cadastro de Mensalistas', 'txt_descricao': 'Cadastro de Mensalistas',
                    'txt_button': 'Cadastrar'}
        return render(request, 'core/cadastro.html', contexto)
    return render(request, 'core/mensagem.html')


def listagem_mensalista(request):
    dados = Mensalista.objects.all()
    contexto = {'dados': dados, 'listagem':True}
    return render(request, 'core/listagem_mensalista.html', contexto)


def atualiza_mensalista(request, id):
    obj = Mensalista.objects.get(id=id)
    form = FormMensalista(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('url_listagem_rotativo')
    contexto = {'form': form, 'txt_title': 'Atualiza Rotativo', 'txt_button': 'Atualizar'}
    return render(request, 'core/cadastro.html', contexto)


def exclui_mensalista(request, id):
    obj = Mensalista.objects.get(id=id)
    obj.delete()
    return redirect('url_listagem_mensalista')
    contexto = {'obj': obj, 'txt_title': 'Exclui Mensalista', 'txt_button': 'Excluir'}
    return render(request, 'core/listagem_Mensalista.html', contexto)
