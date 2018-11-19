from sqlalchemy.sql.expression import func
from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from base import db, Usuario
from flask import session
from base import *
import time
import datetime
import re

urlCategorias = Blueprint('ControladorCategorias', __name__, url_prefix='/ControladorCategorias')


@urlCategorias.route('/mis_categorias', methods=('GET', 'POST'))
def mis_categorias():
    if request.method == 'POST':
        nombre_etiqueta = request.form['etiquetabuscar']
        user = session["user"]
        etiqueta1 = db.session.query(Etiqueta).filter(Etiqueta.nombre == nombre_etiqueta).one()


        flag = False
        error = None
        if not etiqueta1:
            error = 'Inserte etiqueta'
        # if error is None:
        #     if db.session.query(Etiqueta.query.filter(Etiqueta.nombre == etiqueta).exists()).scalar():
        #         usuario = db.session.query(Usuario).filter(Usuario.username == user).one()
        #         etiqueta1 = db.session.query(Etiqueta).filter(Etiqueta.nombre == etiqueta).one()
        #
        #         for categoria in usuario.categorias:
        #             for recurso in categoria.recursos:
        #                 for etiqueta in recurso.recurso.etiquetas:
        #                     if etiqueta.etiqueta.id_etiqueta == etiqueta1.id_etiqueta:
        #
        #                         cate = Categoria(nombre=categoria.nombre)
        #                         cate.recursos.append
        #                         recursosEnEtiqueta.append(cate)
        #                         recursosEnEtiqueta.__getattribute__(categoria).recursos.append(recurso)

        return render_template('categorias.html', etiqueta1=etiqueta1, flag=False,categorias=db.session.query(Usuario).filter(Usuario.username == session['user']).one().categorias)
        flash(error)

        error = None


        flash(error)
    return render_template('categorias.html', categorias=db.session.query(Usuario).filter(Usuario.username == session['user']).one().categorias,flag=True)


def get_user_categories(user):
    return db.session.query(Categoria).filter(Categoria.id_usuario == user.id_usuario).all()
