import assemblyai as aai
from docx import Document
from docx.shared import Pt
from docx.oxml.ns import qn

aai.settings.api_key = "46f568c434a349df894e5f74829619d2"

transcriber = aai.Transcriber()

audio_file = "C:/Users/Skywalker/Documents/Transcripciones/mi_entorno/Frogmación150.mp3"

config = aai.TranscriptionConfig(
    speaker_labels=True,
    language_code="es",
)

transcript = transcriber.transcribe(audio_file, config)

if transcript.status == aai.TranscriptStatus.error:
    print(f"Transcription failed: {transcript.error}")
    exit(1)

def ms_to_time(ms):
    seconds = int((ms / 1000) % 60)
    minutes = int((ms / (1000 * 60)) % 60)
    hours = int((ms / (1000 * 60 * 60)) % 24)
    return f"{hours:02}:{minutes:02}:{seconds:02}"

output_file = "transcripcion.docx"
doc = Document()

doc.styles['Normal'].font.name = 'Arial'
doc.styles['Normal']._element.rPr.rFonts.set(qn('w:eastAsia'), 'Arial')

doc.add_heading("Transcripción completa", level=1)
doc.add_paragraph(transcript.text)

doc.add_heading("Transcripción por hablantes", level=1)

def add_styled_paragraph(doc, text, bold=False, underline=False, font_size=12):
    paragraph = doc.add_paragraph()
    run = paragraph.add_run(text)
    run.bold = bold
    run.underline = underline
    run.font.size = Pt(font_size)
    run.font.name = 'Arial'
    run._element.rPr.rFonts.set(qn('w:eastAsia'), 'Arial')

for utterance in transcript.utterances:
    if utterance.speaker == "A":
        speaker_name = "Juan Gabriel Gomila"
    elif utterance.speaker == "B":
        speaker_name = "Carlos Campaña"
    else:
        speaker_name = f"Speaker {utterance.speaker}"

    start_time = ms_to_time(utterance.start)

    add_styled_paragraph(doc, speaker_name, bold=True, font_size=12)

    add_styled_paragraph(doc, start_time, bold=True, underline=True, font_size=12)

    add_styled_paragraph(doc, utterance.text, font_size=11)

    doc.add_paragraph()

doc.save(output_file)

print(f"La transcripción se ha guardado en el archivo: {output_file}")