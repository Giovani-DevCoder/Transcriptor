Implementando importantes ajustes de seguridad y manejo del proyecto.

# 📝 Transcriptor de Audio a Documento Word

Este proyecto es un transcriptor automático que convierte archivos de audio en transcripciones estructuradas en un documento Microsoft Word (`.docx`), utilizando la API de [AssemblyAI](https://www.assemblyai.com/). También organiza la transcripción por hablantes con marcas de tiempo.

## 🚀 Características

- Transcripción automática de archivos `.mp3`
- Soporte para identificación de hablantes
- Reintentos automáticos en caso de error
- Generación de documento `.docx` con formato legible
- Soporte para idioma español (`es`)


## ⚙️ Dependencias

Este proyecto requiere Python 3.8 o superior y las siguientes bibliotecas:

- `assemblyai`
- `python-docx`


## 🔑 Configuración

Antes de ejecutar el script, asegúrate de colocar tu clave de API de AssemblyAI en esta línea del código:
aai.settings.api_key = "TU_API_KEY_AQUI"


Puedes obtener una clave gratuita en: https://www.assemblyai.com/

## 🧠 ¿Cómo funciona?

1. El script intenta transcribir el archivo de audio local utilizando AssemblyAI.
2. Si ocurre un error, realiza hasta 3 reintentos automáticos con una espera progresiva.
3. Una vez que la transcripción es exitosa, se genera un documento `.docx` con:
   - El texto completo transcrito
   - Un desglose por hablante con formato y marcas de tiempo

## 🛠️ Uso

1. Coloca tu archivo `.mp3` en la ruta especificada en el script, modificando la variable `audio_file`.
2. Ejecuta el script desde la terminal o tu entorno de desarrollo:


3. El documento `transcripcion.docx` se generará en la misma carpeta del script.

## ✍️ Ejemplo de salida

- **Encabezado:** "Transcripción completa"
- **Texto:** Todo el audio transcrito en un solo bloque
- **Por hablantes:** Texto estructurado por nombre (si corresponde), hora de inicio y contenido

## 👥 Personalización de hablantes

El script asigna nombres personalizados si los identificadores de los hablantes son `"A"` o `"B"`. Puedes editar este fragmento del código para personalizar los nombres de los hablantes:


## 📌 Notas

- El script está configurado para trabajar con idioma español (`language_code="es"`).
- El archivo de salida `transcripcion.docx` se sobrescribirá si ya existe.
- La lógica de reintentos ayuda a manejar errores de red o problemas temporales con la API.

## 🧪 Ejemplo rápido

Modifica las siguientes líneas para establecer tu archivo de entrada y el nombre del archivo de salida:


## 📄 Permisos

Siéntete libre de modificar, distribuir y mejorar el código según tus necesidades.
