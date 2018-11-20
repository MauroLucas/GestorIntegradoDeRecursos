from sqlalchemy.sql.expression import func
from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from base import db, Usuario
from flask import session
from base import *
import time
import datetime

urlAgregarParticipante = Blueprint('ControladorAgregarParticipante', __name__, url_prefix='/ControladorAgregarParticipante')


@urlAgregarParticipante.route('/agregar_participante', methods=('GET', 'POST'))
def agregar_participante():
    if request.method == 'POST':
        grupo= request.form['grupo']
        participante = request.form['participante']

        error = None
        if not grupo:
            error = 'Grupo is required.'
        if not participante:
            error = 'The group needs the participant'
        if error is None:

            participanteNuevo = db.session.query(Usuario).filter(Usuario.username == participante).one()
            grupoSelect = db.session.query(Grupo).filter(Grupo.nombre == grupo).one()
            db.session.add(UsuarioXGrupo(id_grupo=grupoSelect.id_grupo, id_usuario=participanteNuevo.id_usuario))
            db.session.commit()
            return redirect(url_for('auth.login_succesful'))

        flash(error)
    return render_template('agregarParticipante.html',grupos = (db.session.query(Usuario).filter(Usuario.username == session['user']).one()).grupos)


def get_user_categories(user):
    return db.session.query(Categoria).filter(Categoria.id_usuario == user.id_usuario).all()