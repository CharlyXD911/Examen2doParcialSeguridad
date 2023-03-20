from wtforms import Form
from wtforms import StringField, IntegerField
from wtforms import EmailField, FileField
from wtforms import validators

class UseForm(Form):
    id=IntegerField('Id')
    nombre=StringField('Marca',[validators.DataRequired(message='Nombre requerido')])
    apellidos=StringField('Apellidos',[validators.DataRequired(message='Apellido requerido')])
    email=EmailField('Correo',[validators.DataRequired(message='Correo requerido')])
    precio=StringField('Precio',[validators.DataRequired(message='Precio requerido')])
    detalle=StringField('Detalle')
    imagen=FileField('Selecciona imagen...')