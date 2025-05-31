Descripción
Este script en Python permite transcribir archivos de audio a documentos Word con formato, incluyendo la identificación de hablantes y marcas de tiempo. Utiliza la API de AssemblyAI para la transcripción y la biblioteca python-docx para generar el documento.

📋 Requisitos previos
Para utilizar este script, necesitarás instalar las siguientes dependencias:

bash
pip install assemblyai python-docx
🔑 Configuración necesaria
Necesitarás una API key de AssemblyAI (puedes obtener una gratuita en su página web)

Reemplaza la línea aai.settings.api_key = "46f568c434a349df894e5f74829619d2" con tu propia API key

🚀 Cómo usar el script
Modifica la variable audio_file en la función main() para apuntar a tu archivo de audio local

Ejecuta el script:

bash
python tu_script.py
El script generará un archivo transcripcion.docx con los resultados

⚙️ Características
Transcripción automática de audio a texto

Identificación de diferentes hablantes

Formateo profesional en documento Word

Reintentos automáticos en caso de fallos

Marcas de tiempo para cada intervención

Soporte para idioma español

📄 Estructura del documento generado
El documento Word resultante contendrá:

Una sección con la transcripción completa

Una sección con la transcripción organizada por hablantes, incluyendo:

Nombre del hablante (en negrita)

Marca de tiempo (subrayada)

Texto transcrito

⚠️ Notas importantes
El script está configurado para identificar específicamente a "Juan Gabriel Gomila" (Speaker A) y "Sebastián Barajas Caseny" (Speaker B). Modifica estos nombres según tus necesidades.

Para archivos largos, la transcripción puede tardar varios minutos.

La versión gratuita de AssemblyAI tiene límites de uso.

📌 Dependencias técnicas
El script utiliza las siguientes bibliotecas:

assemblyai: Para la conexión con la API de transcripción

python-docx: Para la generación del documento Word

time y sys: Para manejo de tiempos y salidas del sistema
