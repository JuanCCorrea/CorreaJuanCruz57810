from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView, LoginView


urlpatterns = [
    
    path('', home, name = "home"),
    
    path ('acerca/', acerca, name = "acerca"),
    
    #______Surf
    path ('surf/', SurfList.as_view(), name = "surf"),
    path ('surfCreate/', SurfCreate.as_view(), name = "surfCreate"),
    path ('surfUpdate/<int:pk>/', SurfUpdate.as_view(), name = "surfUpdate"),
    path ('surfDelete/<int:pk>/', SurfDelete.as_view(), name = "surfDelete"),
    
    #______Body
    path ('body/', BodyList.as_view(), name = "body"),
    path ('bodyCreate/', BodyCreate.as_view(), name = "bodyCreate"),
    path ('bodyUpdate/<int:pk>/', BodyUpdate.as_view(), name = "bodyUpdate"),
    path ('bodyDelete/<int:pk>/', BodyDelete.as_view(), name = "bodyDelete"),
    
    #______Horarios
    path ('horario/', HorarioList.as_view(), name = "horario"),
    path ('horarioCreate/', HorarioCreate.as_view(), name = "horarioCreate"),
    path ('horarioUpdate/<int:pk>/', HorarioUpdate.as_view(), name = "horarioUpdate"),
    path ('horarioDelete/<int:pk>/', HorarioDelete.as_view(), name = "horarioDelete"),
    
    
    #______Reserva
    path ('reserva/', ReservaList.as_view(), name = "reserva"),
    path ('reservaCreate/', ReservaCreate.as_view(), name = "reservaCreate"),
    path ('reservaUpdate/<int:pk>/', ReservaUpdate.as_view(), name = "reservaUpdate"),
    path ('reservaDelete/<int:pk>/', ReservaDelete.as_view(), name = "reservaDelete"),
    
    #______Buscar
    path ('buscarSurf/', buscarSurf, name = "buscarSurf"),
    path ('encontrarSurf/', encontrarSurf, name = "encontrarSurf"),
    path ('buscarbody/', buscarbody, name = "buscarbody"),
    path ('encontrarbody/', encontrarbody, name = "encontrarbody"),
    path ('buscarhorario/', buscarhorario, name = "buscarhorario"),
    path ('encontrarhorario/', encontrarhorario, name = "encontrarhorario"), 
    path ('buscarreserva/', buscarreserva, name = "buscarreserva"),
    path ('encontrarreserva/', encontrarreserva, name = "encontrarreserva"), 
    
    #______ Login, Logout, Registration
    path ('login/', login_view, name = "login"),
    path ('logout/', LogoutView.as_view(template_name="AppCoder/logout.html"), name="logout"),
    path ('registro/', Registro, name = "registro"),
    
#______ Edicion de Perfil, Avatar

    path('perfil/', editProfile, name= "perfil"),
    path('<int:pk>/password/', CambiarClave.as_view(), name="cambiarClave"),
    path('agregarAvatar/', agregarAvatar, name= "agregar_avatar"),

]

