
import gradio as gr
from gradio_iframe import iFrame


example = iFrame().example_inputs()

with gr.Blocks() as demo:
    with gr.Row():
        iFrame(label="Blank"),  # blank component
        iFrame(value=example, label="Populated", height="1000px"),  # populated component


demo.launch()
