from components.Docs import Docs

demo = Docs(__file__).gradio_demo()

if __name__ == "__main__":
    demo.queue().launch()
