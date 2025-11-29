🎉 Aplicación de Registro de Eventos – Django

Proyecto académico – Formularios, Validaciones y Plantillas Reutilizables

📌 Descripción del Proyecto

Este proyecto tiene como objetivo desarrollar una aplicación en Django que permita registrar eventos mediante formularios dinámicos y validados. Los estudiantes ponen en práctica:

Creación de formularios con FormClass

Validación de datos del lado del servidor

Uso de plantillas reutilizables

Manejo de solicitudes GET y POST

Integración con modelos en Django

La aplicación permite registrar un evento con múltiples participantes, validando la información ingresada antes de almacenarla o procesarla.

🎯 Objetivo General

Desarrollar una aplicación en Django que permita a los usuarios registrar eventos, aplicando buenas prácticas en:

Construcción de formularios

Validación

Manejo de vistas

Modularización mediante plantillas reutilizables

Uso de modelos

🧩 Funcionalidades del Proyecto
✔️ Formulario de Registro de Eventos

El formulario principal incluye:

Nombre del Evento (CharField, obligatorio, máx. 100 caracteres)

Fecha del Evento (DateField, obligatorio, debe ser futura)

Ubicación (CharField, opcional)

Validaciones implementadas:

La fecha debe ser posterior a la fecha actual

El nombre del evento debe ser menor o igual a 100 caracteres

✔️ Formulario para Participantes

Se permite registrar múltiples participantes por evento.

Campos:

Nombre del Participante (obligatorio)

Correo Electrónico (EmailField, obligatorio)

🛠️ Tecnologías Utilizadas

Python

Django

HTML

CSS (opcional)

Bootstrap (opcional para estilos de formularios)

🧱 Estructura del Proyecto

La aplicación incluye:

📄 FormClass

EventoForm → para el formulario del evento

ParticipanteForm → para los participantes

👁️ Vistas

Se implementa una vista que maneja:

GET → muestra los formularios vacíos

POST → recibe los datos, valida y procesa

🧩 Plantillas Reutilizables

base.html

Parciales como:

evento_form.html

participante_form.html

messages.html

Estas plantillas emplean bloques para permitir extensiones específicas según la vista.

🧪 Validaciones y Manejo de Errores

Los errores se muestran debajo de cada campo incorrecto.

Los errores generales se muestran mediante {{ form.non_field_errors }}.

Si el formulario es válido, se muestra un mensaje de confirmación.

🚀 Flujo de la Aplicación

1️⃣ El usuario accede al formulario de registro.
2️⃣ Completa la información del evento y de los participantes.
3️⃣ Django valida la información:

Fecha futura

Nombre < 100 caracteres

Email válido
4️⃣ Si hay errores, se muestran en pantalla.
5️⃣ Si todo es válido, se procesa y se muestra un mensaje de éxito.

📚 Aprendizajes Clave

🟦 Creación de formularios con forms.Form y forms.ModelForm
🟦 Uso de validaciones personalizadas (clean() y clean_<field>)
🟦 Manejo de formularios múltiples en una misma vista
🟦 Reutilización de interfaces con plantillas base
🟦 Manejo de métodos HTTP (GET/POST)
🟦 Renderizado limpio de formularios y sus errores

📎 Cómo Ejecutar el Proyecto
# Crear entorno virtual (opcional)
python -m venv myenv

# Activar entorno
myenv\Scripts\activate  # Windows
source myenv/bin/activate  # Linux/Mac

# Instalar dependencias
pip install -r requirements.txt

# Aplicar migraciones
python manage.py migrate

# Ejecutar servidor
python manage.py runserver

🙌 Autores

Proyecto desarrollado con fines educativos por estudiantes del módulo Django.