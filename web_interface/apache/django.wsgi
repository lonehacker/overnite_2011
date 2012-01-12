import os, sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
sys.path.append('/home/overnite/server/overnite_2011')
sys.path.append('/home/overnite/server/overnite_2011/web_interface')
sys.path.append('/home/overnite/server/overnite_2011/web_interface/main')

os.environ['DJANGO_SETTINGS_MODULE'] = 'web_interface.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()

