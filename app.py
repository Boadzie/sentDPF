from nicegui import app, events, ui

from utils import handle_upload

with ui.element("div").classes("font-black mb-2 bg-slate-600 w-full p-4 rounded-md"):
    ui.label("Sent_pdf").classes("text-4xl  text-blue-400")
    ui.label("Upload a pdf file and get sentiment from the first line").classes("text-lg italic text-slate-400")


ui.upload(auto_upload=True, on_upload=handle_upload).props("accept=.pdf").classes("w-1/2")


ui.run()