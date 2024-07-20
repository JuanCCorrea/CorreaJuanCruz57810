from django.shortcuts import render, redirect

from .models import *

from .forms import *

from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.views import PasswordChangeView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required




def home(request):
    return render(request, 'AppCoder/index.html')

@login_required
def acerca(request):
    return render(request, 'AppCoder/acerca.html')

#______Surf

class SurfList(LoginRequiredMixin, ListView):
    model = Surf

class SurfCreate(LoginRequiredMixin, CreateView):
    model = Surf
    fields= ["clases", "valor"]
    success_url = reverse_lazy("surf")

class SurfUpdate(LoginRequiredMixin, UpdateView):
    model = Surf
    fields= ["clases", "valor"]
    success_url = reverse_lazy("surf")

class SurfDelete(LoginRequiredMixin, DeleteView): 
    model = Surf
    success_url = reverse_lazy("surf")



#______Body

class BodyList(LoginRequiredMixin, ListView):
    model = Body


class BodyCreate(LoginRequiredMixin, CreateView):
    model = Body
    fields= ["clases", "valor"]
    success_url = reverse_lazy("body")

class BodyUpdate(LoginRequiredMixin, UpdateView):
    model = Body
    fields= ["clases", "valor"]
    success_url = reverse_lazy("body")

class BodyDelete(LoginRequiredMixin, DeleteView):
    model = Body
    success_url = reverse_lazy("body")
    
#______Horarios

class HorarioList(LoginRequiredMixin, ListView):
    model = Horario

class HorarioCreate(LoginRequiredMixin, CreateView):
    model = Horario
    fields= ["horario"]
    success_url = reverse_lazy("horario")

class HorarioUpdate(LoginRequiredMixin, UpdateView): 
    model = Horario
    fields= ["horario"]
    success_url = reverse_lazy("horario")

class HorarioDelete(LoginRequiredMixin, DeleteView): 
    model = Horario
    success_url = reverse_lazy("horario")
    

#______Reserva

class ReservaList(LoginRequiredMixin, ListView):
    model = Reserva

class ReservaCreate(LoginRequiredMixin, CreateView):
    model = Reserva
    fields= ["nombre", "apellido", "email", "fecha"]
    success_url = reverse_lazy("reserva")

class ReservaUpdate(LoginRequiredMixin, UpdateView): 
    model = Reserva
    fields= ["nombre", "apellido", "email", "fecha"]
    success_url = reverse_lazy("reserva")

class ReservaDelete(LoginRequiredMixin, DeleteView): 
    model = Reserva
    success_url = reverse_lazy("reserva")

#______Buscar

@login_required
def buscarSurf(request):
    return render(request, 'AppCoder/buscarsurf.html')

@login_required
def encontrarSurf(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        clases = Surf.objects.filter(clases__icontains = patron)
        contexto = {"surf": clases}
    else:
        contexto = {"surf": Surf.objects.all()}
        
    return render(request, 'AppCoder/surf.html', contexto)

@login_required
def buscarbody(request):
    return render(request, 'AppCoder/buscarbody.html')

@login_required
def encontrarbody(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        clases = Body.objects.filter(clases__icontains = patron)
        contexto = {"body": clases}
    else:
        contexto = {"body": Body.objects.all()}
        
    return render(request, 'AppCoder/body.html', contexto) 

@login_required
def buscarhorario(request):
    return render(request, 'AppCoder/buscarhorario.html')

@login_required
def encontrarhorario(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        horario = Horario.objects.filter(horario__icontains = patron)
        contexto = {"horario": horario}
    else:
        contexto = {"horario": Horario.objects.all()}
        
    return render(request, 'AppCoder/horario.html', contexto)

@login_required
def buscarreserva(request):
    return render(request, 'AppCoder/buscarreserva.html')

@login_required
def encontrarreserva(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        reserva = Reserva.objects.filter(nombre__icontains = patron)
        reserva = Reserva.objects.filter(apellido__icontains = patron)
        reserva = Reserva.objects.filter(email__icontains = patron)
        reserva = Reserva.objects.filter(fecha__icontains = patron)
        contexto = {"reserva": reserva}
    else:
        contexto = {"reserva": Reserva.objects.all()}
        
    return render(request, 'AppCoder/reserva.html', contexto) 





    

#______ Login, Logout, Registration

def login_view(request):
    if request.method == "POST": 
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar

            #______________________________________________________________
            return render(request, "AppCoder/index.html")
        else:
            return redirect(reverse_lazy('login'))

    else:
        miForm = AuthenticationForm()

    return render(request, "AppCoder/login.html", {"form": miForm})

def Registro(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)
        if miForm.is_valid():
            miForm.save()
            return redirect(reverse_lazy('home'))
    else:
        miForm = RegistroForm()

    return render(request, "AppCoder/registro.html", {"form": miForm})  

#______ Edicion de Perfil, Avatar
@login_required
def editProfile(request):
    usuario = request.user
    if request.method == "POST":
        miForm = UserEditForm(request.POST)
        if miForm.is_valid():
            user = User.objects.get(username=usuario)
            user.email = miForm.cleaned_data.get("email")
            user.first_name = miForm.cleaned_data.get("first_name")
            user.last_name = miForm.cleaned_data.get("last_name")
            user.save()
            return redirect(reverse_lazy("home"))
    else:
        miForm = UserEditForm(instance=usuario)
    return render(request, "AppCoder/editarPerfil.html", {"form": miForm})


class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = "AppCoder/cambiar_clave.html"
    success_url = reverse_lazy("home")
  
@login_required
def agregarAvatar(request):
    if request.method == "POST":
        miForm = AvatarForm(request.POST, request.FILES)
        if miForm.is_valid():
            usuario = User.objects.get(username=request.user)
            imagen = miForm.cleaned_data["imagen"]
            
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            
            avatar = Avatar(user=usuario, imagen=imagen)
            avatar.save()

            
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen
            
            return redirect(reverse_lazy("home"))
    else:
        miForm = AvatarForm()
    return render(request, "AppCoder/agregarAvatar.html", {"form": miForm})    