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


productos=Blueprint('productos', __name__)

@productos.route('/getpro',methods=['GET'])
@login_required
#@roles_required('')
@roles_accepted('Administrador')
def getpro():
    create_form=forms.UseForm(request.form)
    productos=Productos.query.all()
    #alumnos = Alumnos.query.filter(Alumnos.nombre.like('%CO%')).all()
    return render_template('ABCompleto.html',form=create_form,productos=productos)


@productos.route("/agregar", methods=['GET','POST'])
@login_required
#@roles_required('')
@roles_accepted('Administrador')
def agregar():
    create_form=forms.UseForm(request.form)
    if request.method=='POST':
        imagen = request.files['imagen']
        pro=Productos()
        pro.nombre=create_form.nombre.data
        pro.precio=create_form.precio.data
        pro.detalle=create_form.detalle.data
        if imagen :
            imagen_base64 = base64.b64encode(imagen.read())
            pro.data = imagen_base64
        else :
            pro.data=''
        db.session.add(pro)
        #userDataStore.create_producto(nombre=nombre, data=encoded_image)
        db.session.commit()
        return redirect(url_for('productos.getpro'))
    return render_template('agregar.html',form=create_form)

@productos.route("/modificar",methods=['GET','POST'])
@login_required
#@roles_required('')
@roles_accepted('Administrador')
def modificar():
    create_form=forms.UseForm(request.form)
    if request.method=='GET':
        id=request.args.get('id')
        pro1=db.session.query(Productos).filter(Productos.id==id).first()
        create_form.id.data=request.args.get('id')
        create_form.nombre.data=pro1.nombre
        create_form.imagen.data=pro1.data
        create_form.precio.data=pro1.precio
        create_form.detalle.data=pro1.detalle
    if request.method=='POST' and create_form.nombre.data != '' and create_form.precio.data != '':
        id=create_form.id.data
        pro=db.session.query(Productos).filter(Productos.id==id).first()
        pro.nombre=create_form.nombre.data
        pro.precio=create_form.precio.data
        pro.detalle=create_form.detalle.data
        imagen=''
        try:
            imagen = request.files['imagen']
            if imagen :
                imagen_base64 = base64.b64encode(imagen.read())
                pro.data=imagen_base64
            else :
                pro.data=request.form.get("imagen1").value
            db.session.add(pro)
            db.session.commit()
            return redirect(url_for('productos.getpro'))
        except :
            db.session.add(pro)
            db.session.commit()
        return redirect(url_for('productos.getpro'))
    return render_template('modificar.html',form=create_form)

@productos.route("/eliminar",methods=['GET','POST'])
@login_required
#@roles_required('')
@roles_accepted('Administrador')
def eliminar():
    create_form=forms.UseForm(request.form)
    if request.method=='GET':
        id=request.args.get('id')
        pro1=db.session.query(Productos).filter(Productos.id==id).first()
        create_form.id.data=request.args.get('id')
        create_form.nombre.data=pro1.nombre
        create_form.imagen.data=pro1.data
        create_form.precio.data=pro1.precio
        create_form.detalle.data=pro1.detalle
    if request.method=='POST':
        id=create_form.id.data
        pro=db.session.query(Productos).filter(Productos.id==id).first()
        pro.nombre=create_form.nombre.data
        pro.precio=create_form.precio.data
        pro.detalle=create_form.detalle.data
        imagen=''
        try:
            imagen = request.files['imagen']
            if imagen :
                imagen_base64 = base64.b64encode(imagen.read())
                pro.data=imagen_base64
            else :
                pro.data=request.form.get("imagen1").value
            db.session.delete(pro)
            db.session.commit()
            return redirect(url_for('productos.getpro'))
        except :
            db.session.delete(pro)
            db.session.commit()
        return redirect(url_for('productos.getpro'))
    return render_template('eliminar.html',form=create_form)
