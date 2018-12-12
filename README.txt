#Para uso de Django:
    pip install django

#Superusuario
    User: Admin
    Password: 1234

#Para logearse con redes socieles
    pip install python-social-auth y pip install social-auth-app-django
#En settings.py nos dirigimos a INSTALLED_APPS y agregamos:
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
#Nos logeamos y creamos un proyecto en https://console.developers.google.com/ e ingresamos al final de settings.py :
    SOCIAL_AUTH_GOOGLE_KEY = ''
    SOCIAL_AUTH_GOOGLE_SECRET = ''

#Luego ingresamos al administrador, nos dirigimos a las social account e ingresamos a 'Cuentas sociales'. Agregamos una aplicacion social y cambiamos 
Proveedor: "Google", Name:"---", Client id: "Se obtiene desde el proyecto creado", 
secret key: "Se obtiene desde el proyecto creado" y en Sites: seleccionamos http://localhost:8000/ y lo movemos a la columna 'Sitios elegidos', y guardamos

--------------------------------------------------------------------------------------------------------------
#Para uso de RestFramework instalamos:
    pip install djangorestframework
#INSTALLED_APPS = (
    ...
    'rest_framework',
)
REST_FRAMEWORK = {
}
#Models.py
    from django.contrib.auth.models import User
    from rest_framework import serializers


    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('username', 'email')
#Views.py
    from django.contrib.auth.models import User
    from rest_framework import viewsets

    class UserViewSet(viewsets.ModelViewSet):
        """
        API endpoint that allows users to be viewed or edited.
        """
        queryset = User.objects.all().order_by('-date_joined')
        serializer_class = UserSerializer
#urls.py
    from django.conf.urls import url, include
    from rest_framework import routers

    router = routers.DefaultRouter()
    router.register(r'users', views.UserViewSet)

    urlpatterns = [
        url(r'^', include(router.urls))
    ]
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Para uso de sitio web progresivo con service workers:
    pip install django-pwa
#En settings.py nos dirigimos a INSTALLED_APPS y agregamos:
      'pwa',
Luego al final de settings
PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, 'serviceworker.js')
PWA_APP_NAME = "NombredeProyecto"
PWA_APP_START_URL = '/'
PWA_APP_ICONS = [
{
     ICONO DE APLICACIÓN
    'src':'/static/img/iconos menu/finanzas.jpg',
    'sizes':'160x160'
}]
#Crear archivo serviceworker(Archivos que quiero guardar en cache)
--Nombre de cache
var CACHE_NAME = 'my-site-cache-v1';
--Archivos a guardar en cache
var urlsToCache = [
    '/',
    '/static/css/style.css',
    '/static/img/iconos menu/carrousel1_finanzas-800x400.jpg',
    '/static/img/iconos menu/carrousel2_como-hacer-un-presupuesto-personal.jpg',
    '/static/img/iconos menu/carrousel3_MyValueLanding4.jpg',
    '/static/img/iconos menu/carrousel3_MyValueLanding4.jpg',
    '/static/vendor/bootstrap/css/bootstrap.min.css',
    'https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js',
];

--Evento de llamada para guardar en cache
self.addEventListener('install', function(event) {
    // Perform install steps
    event.waitUntil(
      caches.open(CACHE_NAME)
        .then(function(cache) {
          console.log('Opened cache');
          return cache.addAll(urlsToCache);
        })
    );
  });
  
