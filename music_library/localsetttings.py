
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-bz_=bk5=h+i5o_)s7#f53^4aj(ehc&()qc!1602(gd5p4c+-7u'


DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'music_database',
        'USER': 'root',
        'PASSWORD': 'Addison2007!',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
                'autocommit': True
        }
    
    }
}
