from nicegui import app, events, ui

from utils import handle_upload

ui.query('body').classes("bg-[#03045e]")
ui.query('body').classes("text-white")
with ui.element("div").classes("shadow-lg font-black mb-2  w-full p-4 rounded-md"):
    ui.label("SentPDF").classes("text-4xl  text-blue-400")
    ui.label("Upload a pdf file and get sentiment from the first line").classes("text-lg italic text-white")


ui.upload(auto_upload=True, on_upload=handle_upload).props("accept=.pdf").classes("w-1/2")
with ui.footer().classes("shadow-lg bg-[#03045e] mx-5 rounded-md"):
    ui.label("©2023 Daniel Boadzie")

ui.run()