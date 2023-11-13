from nicegui import events, ui
from PyPDF2 import PdfReader
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def get_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    vs = analyzer.polarity_scores(text)
    if vs["compound"]  >= 0.05:
       return "Postive"
    elif vs["compound"] > -0.05 and vs["compound"] < 0.05:
        return  "Neutral"
    else:
        return "Negative"
    
def handle_upload(event: events.UploadEventArguments):
    with event.content as f:
        # uploaded_file = Pim.open(f)
        try:
            reader = PdfReader(f)
            page = reader.pages[0]
            text = page.extract_text()
            with ui.element("div").classes("grid grid-cols-1 lg:grid-cols-2 gap-4 w-full"):
                with ui.element("div").classes("shadow-lg p-4 w-full"):
                    ui.label(text).classes("w-full")
                with ui.element("div"):
                    ui.label(get_sentiment(text)).classes("shadow-lg p-4 text-center h-full text-blue-400 text-6xl font-black w-full")
        except Exception as e:
            ui.notify(f"{e} error occurred while uploading the file")    