ROOT_URLCONF = 'apps.jmutube.urls'
JMUTUBE_LOGIN_URL = '/accounts/login/'

SSL_PORT = ':8443'

LOGFILENAME = 'jmutube'

HANDLER404 = 'apps.jmutube.views.jmutube404'
HANDLER500 = 'apps.jmutube.views.jmutube500'
