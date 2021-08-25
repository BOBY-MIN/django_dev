'''
Created on 2021. 4. 29.

@author: 이상민
'''


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'web_test',
        'USER': 'root',
        'PASSWORD': 'passwd',
        'HOST': 'host',
        'PORT': '3306',
    }
}
SECRET_KEY = 'django-insecure-vtqo&=$8+%y-@@3x$i)pa84_3$c4&^(kt566p_huxb*0$$n1rd'