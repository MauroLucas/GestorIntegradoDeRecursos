from flaskr.base import db
from flaskr.base import Categoria,Usuario,Recurso,CategoriaXRecurso,Grupo,UsuarioXGrupo,RecursoXEtiqueta,Comentario,Etiqueta
import datetime

usuario1 = Usuario(username='mauro',password='1234',nombre='mauro',apellido='pereyra',mail='m_l_pereyra')
usuario2 = Usuario(username='gian',password='1234',nombre='mauro',apellido='pereyra',mail='m_l_pereyra')
usuario3 = Usuario(username='lucas',password='1234',nombre='mauro',apellido='pereyra',mail='m_l_pereyra')
usuario4 = Usuario(username='german',password='1234',nombre='mauro',apellido='pereyra',mail='m_l_pereyra')
db.session.add(usuario1)
db.session.add(usuario2)
db.session.add(usuario3)
db.session.add(usuario4)
db.session.commit()
db.session.flush()


categoria1 = Categoria(id_usuario=usuario1.id_usuario,nombre='Videojuegos')
categoria2 = Categoria(id_usuario=usuario1.id_usuario,nombre='Learning')

categoria3 = Categoria(id_usuario=usuario1.id_usuario,nombre='Unla')

db.session.add(categoria1)
db.session.add(categoria2)
db.session.add(categoria3)

db.session.commit()
db.session.flush()


recurso1 = Recurso(recurso='https://unity3d.com',descripcion='Framework Unity',fecha=datetime.datetime.now())
recurso2 = Recurso(recurso='https://www.babylonjs.com',descripcion='Framework de JavaScript',fecha=datetime.datetime.now())
recurso3 = Recurso(recurso='https://www.3djuegos.com',descripcion='Foro de Videojuegos',fecha=datetime.datetime.now())
db.session.add(recurso1)
db.session.add(recurso2)
db.session.add(recurso3)
db.session.commit()
db.session.flush()

recurso4 = Recurso(recurso='https://www.w3schools.com',descripcion='Turoriales de Programacion',fecha=datetime.datetime.now())
recurso5 = Recurso(recurso='https://www.tutorialesprogramacionya.com',descripcion='Turoriales de Programacion',fecha=datetime.datetime.now())
db.session.add(recurso4)
db.session.add(recurso5)
db.session.commit()
db.session.flush()




recurso7 = Recurso(recurso='http://www.unla.edu.ar',descripcion='Sitio Oficial Unla',fecha=datetime.datetime.now())
recurso8 = Recurso(recurso='http://campus.unla.edu.ar',descripcion='Campus Virtual',fecha=datetime.datetime.now())
db.session.add(recurso7)
db.session.add(recurso8)
db.session.commit()
db.session.flush()



etiqueta1= Etiqueta(nombre='programacion')
etiqueta2= Etiqueta(nombre='juegos')
etiqueta3= Etiqueta(nombre='unla')
db.session.add(etiqueta1)
db.session.add(etiqueta2)
db.session.add(etiqueta3)
db.session.commit()
db.session.flush()


recursoXrtiqueta1 = RecursoXEtiqueta(id_recurso=recurso4.id_recurso,id_etiqueta=etiqueta1.id_etiqueta)
recursoXrtiqueta2 = RecursoXEtiqueta(id_recurso=recurso1.id_recurso,id_etiqueta=etiqueta2.id_etiqueta)
recursoXrtiqueta3 = RecursoXEtiqueta(id_recurso=recurso7.id_recurso,id_etiqueta=etiqueta3.id_etiqueta)
db.session.add(recursoXrtiqueta1)
db.session.add(recursoXrtiqueta2)
db.session.add(recursoXrtiqueta3)
db.session.commit()
db.session.flush()



categoriaXrecurso1 = CategoriaXRecurso(id_recurso=recurso1.id_recurso, id_categoria=categoria1.id_categoria)
categoriaXrecurso2 = CategoriaXRecurso(id_recurso=recurso2.id_recurso, id_categoria=categoria1.id_categoria)
categoriaXrecurso3 = CategoriaXRecurso(id_recurso=recurso3.id_recurso, id_categoria=categoria1.id_categoria)

categoriaXrecurso4 = CategoriaXRecurso(id_recurso=recurso4.id_recurso, id_categoria=categoria2.id_categoria)
categoriaXrecurso5 = CategoriaXRecurso(id_recurso=recurso5.id_recurso, id_categoria=categoria2.id_categoria)

categoriaXrecurso6 = CategoriaXRecurso(id_recurso=recurso7.id_recurso, id_categoria=categoria3.id_categoria)
categoriaXrecurso7 = CategoriaXRecurso(id_recurso=recurso8.id_recurso, id_categoria=categoria3.id_categoria)
db.session.add(categoriaXrecurso1)
db.session.add(categoriaXrecurso2)
db.session.add(categoriaXrecurso3)
db.session.add(categoriaXrecurso4)
db.session.add(categoriaXrecurso5)
db.session.add(categoriaXrecurso6)
db.session.add(categoriaXrecurso7)
db.session.commit()
db.session.flush()



grupo1 = Grupo(nombre='Desarrollo de VideoJuegos',id_admin=usuario1.id_usuario)
grupo2 = Grupo(nombre='Desarrollo Web',id_admin=usuario1.id_usuario)
grupo3 = Grupo(nombre='Data Analytics',id_admin=usuario1.id_usuario)
db.session.add(grupo1)
db.session.add(grupo2)
db.session.add(grupo3)
db.session.commit()
db.session.flush()

usuarioXGrupo1 = UsuarioXGrupo(id_usuario=usuario1.id_usuario,id_grupo=grupo1.id_grupo)
usuarioXGrupo2 = UsuarioXGrupo(id_usuario=usuario2.id_usuario,id_grupo=grupo1.id_grupo)
usuarioXGrupo3 = UsuarioXGrupo(id_usuario=usuario3.id_usuario,id_grupo=grupo1.id_grupo)
usuarioXGrupo4 = UsuarioXGrupo(id_usuario=usuario4.id_usuario,id_grupo=grupo1.id_grupo)
db.session.add(usuarioXGrupo1)
db.session.add(usuarioXGrupo1)
db.session.add(usuarioXGrupo1)
db.session.add(usuarioXGrupo1)
db.session.commit()
db.session.flush()

comentario1 = Comentario(comentario="Miren estos links",fecha=datetime.datetime.now(),id_grupo=grupo1.id_grupo,id_categoria=categoria1.id_categoria)
db.session.add(comentario1)
db.session.commit()
db.session.flush()
