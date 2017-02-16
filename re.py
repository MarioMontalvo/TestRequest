import requests
from getpass import getpass
# Definimos la URL
url = "https://accounts.google.com/ServiceLogin?service=mail&passive=true&rm=false&continue=https://mail.google.com/mail/&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1"
# Solicitamos los datos del usuario
user = raw_input("username: ")
passwd = getpass ("password: ")
proy = raw_input("proyecto: ")
# Definimos la cabecera y el diccionario con los datos
cabecera1 = {'Content-type': 'application/json'}
datos = '{"auth":{"passwordCredentials":{"username": "%s", "password": "%s"}, "tenantName":"%s"}}' % (user, passwd, proy)
solicitud = requests.post(url+'tokens', headers = cabecera1, data = datos)
if solicitud.status_code == 200:
    print solicitud.text
    print "Prueba 2 de git"
    print "Prueba 2 de git"
    print 'dos'
