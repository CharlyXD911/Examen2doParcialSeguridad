from flask import Blueprint
from flask import Flask, redirect, render_template
from flask import request
from flask import url_for
from . import forms
from flask import jsonify,Response
from flask_security import login_required,current_user
from flask_security.decorators import roles_required,roles_accepted
from .models import Productos
from .models import db
import base64


producto=Blueprint('producto', __name__)

@producto.route('/getproduct',methods=['GET'])
@login_required
#@roles_required('')
@roles_accepted('Administrador','Usuario')
def getproduct():
    create_form=forms.UseForm(request.form)
    productos=Productos.query.all()
    #alumnos = Alumnos.query.filter(Alumnos.nombre.like('%CO%')).all()
    return render_template('producto.html',form=create_form,productos=productos)
