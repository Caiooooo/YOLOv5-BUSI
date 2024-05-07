import gradio  as gr
import torch
import cv2
def file_path(input):
    return input

model = torch.hub.load("./", "custom", path="best.pt",source="local", force_reload=True)
iface = gr.Interface(inputs=["image"],outputs=["image"],fn=lambda img:model(img).render()[0])
iface.launch(server_name="0.0.0.0", server_port=8080)