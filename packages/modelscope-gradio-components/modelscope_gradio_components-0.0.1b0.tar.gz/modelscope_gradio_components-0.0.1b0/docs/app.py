import gradio as gr
from components.Chatbot.app import demo as chatbot_demo
from components.Docs import Docs
from components.MutilmodalInput.app import demo as mutilmodel_input_demo

readme_demo = Docs(__file__).gradio_demo()

demo = gr.TabbedInterface([readme_demo, chatbot_demo, mutilmodel_input_demo],
                          ["开始使用", "Chatbot", "MultimodalInput"])

demo.queue().launch()
