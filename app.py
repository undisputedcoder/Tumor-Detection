import yolov5.detect as detect
import streamlit as st
import os

from PIL import Image

st.title('💀 Brain Tumour Detection')
st.write('### A simple web app to detect possible brain tumour(s)')

st.write('#### Upload an axial MRI image.')
uploaded_file = st.file_uploader('', type=['png', 'jpg', 'jpeg'], accept_multiple_files=False)

if uploaded_file is None:
    st.warning("No file has been uploaded.")
    st.stop()
else:
    if os.path.exists('yolov5/runs/detect/exp'):
        os.rmdir('yolov5/runs/detect/exp')

    image = Image.open(uploaded_file).convert("RGB")
    filename = str(uploaded_file.name)
    image = image.save(filename)

detect.run(weights='yolov5/runs/train/exp3/weights/best.pt', conf_thres=0.1, source=filename)

st.image('yolov5/runs/detect/exp/' + filename)

os.remove(filename)
os.remove('yolov5/runs/detect/exp/' + filename)