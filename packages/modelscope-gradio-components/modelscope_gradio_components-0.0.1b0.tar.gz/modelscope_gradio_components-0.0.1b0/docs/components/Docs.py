import os
import re

import gradio as gr

from .parse_markdown import parse_markdown


def remove_formatter(markdown_text):
    pattern = r"^---[\s\S]*?---"

    replaced_text = re.sub(pattern, "", markdown_text)

    return replaced_text


def list_demos(dir_path: str, prefix=''):
    result = []
    if (not os.path.isdir(dir_path)):
        return result
    for name in os.listdir(dir_path):
        path = os.path.join(dir_path, name)

        if os.path.isfile(path):
            result.append(prefix + name)
        elif os.path.isdir(path):
            sub_prefix = prefix + name + '/'
            result.extend(list_demos(path, sub_prefix))

    return result


def get_demo_modules(file_path: str):
    import importlib.util

    demos = [
        demo for demo in list_demos(
            os.path.join(os.path.dirname(file_path), "demos"))
        if demo.endswith(".py")
    ]
    demo_modules = {}
    for demo in demos:
        demo_name = demo.split(".")[0]
        spec = importlib.util.spec_from_file_location(
            "demo", os.path.join(os.path.dirname(file_path), "demos", demo))
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        demo_modules[demo_name] = module
    return demo_modules


class Docs:

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.demo_modules = get_demo_modules(file_path)
        # 只要当前目录的 markdown 文件
        self.markdown_files = [
            file_name for file_name in os.listdir(os.path.dirname(file_path))
            if file_name.endswith(".md")
        ]
        self.demo = self.render()

    def read_file(self, relative_path: str):
        with open(os.path.join(os.path.dirname(self.file_path), relative_path),
                  "r") as f:
            return f.read()

    def render_demo(self, demo_name, prefix='', suffix=''):
        content = self.read_file(f"./demos/{demo_name}.py")
        module = self.demo_modules[demo_name]
        with gr.Accordion("Show Demo", open=False):
            with gr.Row():
                with gr.Column():
                    gr.Markdown(
                        f"""
{prefix}
````python
{content}
````
{suffix}
""",
                        header_links=True,
                    )
                with gr.Column():
                    module.demo.render()

    def render_markdown(self, markdown_file, tabs=None):
        items = parse_markdown(remove_formatter(
            self.read_file(markdown_file), ),
                               read_file=self.read_file)
        for item in items:
            if item["type"] == "text":
                gr.Markdown(item["value"], header_links=True)
            elif item["type"] == "tab-link":

                def get_click(item):

                    def click():
                        href: str = item["href"]
                        return gr.update(selected=href.split("/")[-1])

                    return click

                gr.Button(item["value"] or item["href"],
                          size="sm").click(fn=get_click(item), outputs=[tabs])
            elif item["type"] == "demo":
                self.render_demo(item["name"],
                                 prefix=item["prefix"],
                                 suffix=item["suffix"])

    def render(self):

        with gr.Blocks() as demo:
            if len(self.markdown_files) > 1:
                with gr.Tabs() as tabs:
                    for markdown_file in self.markdown_files:
                        with gr.TabItem(markdown_file, id=markdown_file):
                            self.render_markdown(markdown_file, tabs)
            else:
                self.render_markdown(self.markdown_files[0])
        return demo

    def gradio_demo(self):
        return self.demo
