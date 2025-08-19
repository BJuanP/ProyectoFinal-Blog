# 📝 TECChaco - Blog Django - Proyecto Final

Un sistema de blog completo desarrollado con Django que permite la gestión de artículos, comentarios, categorías y usuarios con una interfaz moderna y responsive.

## 🌟 Características Principales

- **Gestión de Artículos**: Creación, edición y eliminación de artículos con imágenes
- **Sistema de Comentarios**: Los usuarios pueden comentar en los artículos
- **Categorías**: Organización de contenido por categorías
- **Sistema de Usuarios**: Registro, login y gestión de perfiles
- **Artículos Destacados**: Sistema para resaltar artículos principales
- **Panel de Administración**: Interface administrativa completa

## 🛠️ Tecnologías Utilizadas

- **Backend**: Django 5.2.3
- **Base de Datos**: MySQL
- **Frontend**: HTML5, CSS3, JavaScript
- **Procesamiento de Imágenes**: Pillow
- **Frameworks CSS**: CSS personalizado con Sass
- **Fuentes de Iconos**: Font Awesome

## 📁 Estructura del Proyecto

```
Blog/
├── apps/
│   ├── articulos/          # Gestión de artículos
│   ├── categorias/         # Gestión de categorías
│   ├── comentarios/        # Sistema de comentarios
│   └── usuario/            # Gestión de usuarios
├── Blog/
│   ├── settings/           # Configuraciones del proyecto
│   │   ├── base.py        # Configuración base
│   │   ├── local.py       # Configuración desarrollo
│   │   └── production.py  # Configuración producción
│   ├── urls.py            # URLs principales
│   └── views.py           # Vistas principales
├── templates/              # Plantillas HTML
├── static/                 # Archivos estáticos (CSS, JS, imágenes)
├── media/                  # Archivos subidos por usuarios
└── requirements.txt        # Dependencias del proyecto
```

## 🚀 Instalación y Configuración

### Prerrequisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clonar el repositorio**
   ```bash
   git clone <url-del-repositorio>
   cd ProyectoFinal-Blog-main/Blog
   ```

2. **Crear entorno virtual**
   ```bash
   python -m venv venv
   ```

3. **Activar entorno virtual**
   ```bash
   # En Windows
   venv\Scripts\activate
   
   # En Linux/Mac
   source venv/bin/activate
   ```

4. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

5. **Configurar base de datos**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Crear superusuario**
   ```bash
   python manage.py createsuperuser
   ```

7. **Ejecutar el servidor de desarrollo**
   ```bash
   python manage.py runserver
   ```

8. **Acceder a la aplicación**
   - Sitio web: `http://127.0.0.1:8000/`
   - Panel de administración: `http://127.0.0.1:8000/admin/`

## 📱 Funcionalidades

### Para Usuarios
- ✅ Registro e inicio de sesión
- ✅ Visualización de artículos por categorías
- ✅ Lectura de artículos completos
- ✅ Sistema de comentarios
- ✅ Visualización de artículos destacados

### Para Administradores
- ✅ Gestión completa de artículos
- ✅ Moderación de comentarios
- ✅ Gestión de categorías
- ✅ Gestión de usuarios
- ✅ Configuración de artículos destacados

## 🎨 Características del Diseño

- **Interfaz Moderna**: Diseño limpio y profesional
- **Navegación Intuitiva**: Menús desplegables y navegación clara
- **Optimización de Imágenes**: Manejo automático de imágenes subidas
- **Tipografía**: Font Awesome para iconos

## ⚙️ Configuración de Entornos

El proyecto incluye configuraciones separadas para desarrollo y producción:

- **Desarrollo**: `settings/local.py`
- **Producción**: `settings/production.py`
- **Base**: `settings/base.py` (configuración común)

## 📊 Modelos de Datos

### Artículo
- Título, resumen y cuerpo
- Imagen asociada
- Autor y fecha de publicación
- Categoría
- Estado de destacado

### Usuario
- Modelo personalizado de usuario
- Sistema de autenticación integrado

### Comentario
- Asociados a artículos específicos
- Información del autor y fecha

### Categoría
- Organización temática de artículos
- Context processor para disponibilidad global

## 🔧 Comandos Útiles

```bash
#Crear Grupo "Moderador" y "Miembro", y asignar permisos.
python manage.py crear_grupos

# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Recopilar archivos estáticos (producción)
python manage.py collectstatic

# Ejecutar tests
python manage.py test

# Shell interactivo de Django
python manage.py shell
```


## 👥 Autores

*Proyecto Final Informatorio*

• **Bravo Juan Pablo**

• **Obregón César Lautaro**

• **Massad Lucas Yael**

• **Lazarczuk Carlos Agustin**

## 📞 Contacto

Si tienes preguntas o sugerencias, no dudes en contactar a través de:
- GitHub: [Lussad](https://github.com/Lussad)
- GitHub: [BJuanP](https://github.com/BJuanP)

---

⭐ Si este proyecto te ha sido útil, ¡no olvides darle una estrella!
