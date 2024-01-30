import gradio as gr
from cweb import pipeline

predict = pipeline()

with gr.Blocks(title="cweb") as webapp:
    gr.Markdown("# Greetings from cweb!")
    inp = gr.Textbox(placeholder="What is your name?")
    out = gr.Textbox()

    inp.change(fn=predict,
               inputs=inp,
               outputs=out)