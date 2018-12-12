from django.views.generic import CreateView, ListView, FormView
from .forms import  FormularioLogin , ClienteForm
from .models import *
from django.shortcuts import get_object_or_404, render, redirect, render, reverse
from .forms import ListaForm
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Avg, Count, Min, Sum
from django.urls import reverse_lazy
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
#from viewsets
from rest_framework import viewsets
from Apps.Usuario.serializers import UserSerializers, GroupSerializers

#Contactanos
def contact(request):
    return render(request, 'contact.html')

#Vistas para Usuario
def home(request):
    return render(request, 'home.html')

def inde(request):
    return render(request, 'login.html')

#Cerrar sesion
def salir(request):
    logout(request)
    return render(request, 'home.html', {})

class Login(FormView):
    template_name = 'login.html'
    form_class = FormularioLogin
    success_url = ('mantenedor')
 
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)
 
    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)

class ClienteCreate(CreateView):
    model = User
    form_class = ClienteForm
    template_name = 'formulario.html'
    success_url = reverse_lazy('home')  

# Create your views here.
def IndexView(request):
	listas = Lista.objects.filter(user_id=request.user.id)
	result = []
	for e in listas:
		 result.append(Producto.objects.filter(lista_id=e.pk))
	num = 0
	num2 = 0
	resultadosumacostoP = 0
	resultadosumacostoR = 0
	sumaP = []
	sumaR = []
	prodC = []
	counter = 0
	for i in range(len(result)):
		for u in range(len(result[num])):
			resultadosumacostoP = resultadosumacostoP + result[num][num2].costoP
			resultadosumacostoR = resultadosumacostoR + result[num][num2].costoR
			if result[num][num2].comprado == True:
				counter = counter + 1
			num2 = num2 + 1	
		sumaP.append(resultadosumacostoP)
		sumaR.append(resultadosumacostoR)
		prodC.append(counter)	
		num = num + 1
		num2 = 0
		counter = 0
		resultadosumacostoP = 0
		resultadosumacostoR = 0	
	num = 0


	#el total de productos agregados (Listo)
	#el total de productos ya comprados (Listo)
	#el costo total presupuestado (Listo)
	#el costo total real de los productos comprados (Listo)
	return render(request,'mantenedor.html', {'Lista': listas,'listproduct': result, 'sumaP':sumaP,'sumaR':sumaR, 'counter':prodC})
	
def IndexView2(request, pk):
	producto = Producto.objects.filter(lista_id=pk)
	tiendas = Tienda.objects.all()
	tiendasf = Tienda.objects.filter(verificado=True)
	return render(request,'mantenedorproducto.html', {'producto': producto, 'lista_pk': pk, 'tiendas':tiendas, 'tiendasf':tiendasf})

def IndexView3(request):
	tiendas = Tienda.objects.all()
	tiendasf = Tienda.objects.filter(verificado=True)
	return render(request,'mantenedortienda.html', {'tiendas':tiendas,'tiendasf':tiendasf})

class crud():
	def guardarProducto(request, pk):
		if 'comprado' in request.POST:
			Validador = True
		else:
			Validador = False
		sv = Producto(
		nombreproducto=request.POST['nombreproducto'], 
		costoP=request.POST['costoP'],
		costoR=request.POST['costoR'],
		tienda = Tienda.objects.get(nombretienda=request.POST['tienda']),
		lista= Lista.objects.get(id=pk),
		notas=request.POST['notas'],
		comprado = Validador, )

		sv.save()
		return HttpResponseRedirect(reverse('Usuario:productoconid', args=[pk]))

	def editarProducto(request, data_id):
		data = get_object_or_404(Producto, pk=data_id)
		alldata = Producto.objects.order_by('nombreproducto') 
		return render(request, 'mantenedorproducto.html', {'data': data, 'qid' : data_id, 'getdata' : alldata})
	
	def actualizarProducto(request):
		ed = Producto.objects.get(pk=request.POST['qid'])

		ed.nombreproducto=request.POST['nombreproducto']
		ed.costoP=request.POST['costoP']
		ed.costoR=request.POST['costoR']
		ed.notas=request.POST['notas']
		
		ed.save()

		return HttpResponseRedirect(reverse('Usuario:productoconid', args=[ed.lista.pk]))

def guardarLista(request):
	form = ListaForm(request.POST)
	if form.is_valid():
		asd = form.save(commit=False)
		user = User.objects.get(pk=request.user.id)
		asd.user = user
		asd.save()
		form = ListaForm()
		return redirect('Usuario:mantenedor')
	return render(request, 'guardarLista.html',{'form':form})

def guardarTienda(request):
		if 'esOnline' in request.POST:
			Validador = True
		else:
			Validador = False

		tie = Tienda(
		nombretienda=request.POST['nombretienda'], 
		nombresucursal=request.POST['nombresucursal'],
		esOnline= Validador,
		direccion = request.POST['direccion'],
		ciudad = request.POST['ciudad'],
		region = request.POST['region'])
		
		tie.save()
		return HttpResponseRedirect(reverse('Usuario:tienda'))

def eliminartienda(request, pk):
		dl = Tienda.objects.get(id=pk)
		dl.delete()
		return HttpResponseRedirect(reverse('Usuario:tienda'))

def verificartienda(request, pk):
		dl = Tienda.objects.get(id=pk)
		dl.verificado = True
		dl	.save()
		return HttpResponseRedirect(reverse('Usuario:tienda'))

#vistas para menu
def menu(request):
    return render(request, 'menu.html')
        
def eliminarproducto(request, pk):
		dl = Producto.objects.get(id=pk)
		dl.delete()
		return HttpResponseRedirect(reverse('Usuario:productoconid', args=[dl.lista.pk]))


#Vista para los serializers
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializers


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializers