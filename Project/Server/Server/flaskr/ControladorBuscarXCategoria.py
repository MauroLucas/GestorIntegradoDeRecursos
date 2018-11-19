from sqlalchemy.sql.expression import func
from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from base import db, Usuario
from flask import session
from base import *
import time
import datetime

urlBuscarXCategoria = Blueprint('ControladorBuscarXCategoria', __name__, url_prefix='/ControladorBuscarXCategoria')

@urlBuscarXCategoria.route('/buscar_categoria', methods=('GET', 'POST'))
def buscar_categoria():
    if request.method == 'POST':
        user = db.session.query (Usuario).filter (Usuario.username == session['user']).one ()
        categoria = request.form['categoriabuscar'] #CATEGORIASELECCIONADA
        recursosEnCategoria = []
        error = None
        if not categoria:
            error = 'Seleccione categoria'
        if error is None:
            categoria1 = db.session.query(Categoria).filter(Categoria.nombre == categoria).one()
            for cate in categoria1.recursos:
                    recursosEnCategoria.append(cate.recurso.recurso)
            return render_template('buscar_por_categoria.html', recursosBuscadosCat=recursosEnCategoria)
        flash (error)
    return render_template('buscar_por_categoria.html')