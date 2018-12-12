var CACHE_NAME = 'my-site-cache-v1';
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
  
  self.addEventListener('fetch', function(event){
      event.respondWith(
          caches.match(event.request).then(function(response) {
              if(response) {
                  return response;
              }
  
              return fetch(event.request);
          })
      );
  });