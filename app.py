import streamlit as st
import cv2
import numpy as np
from style_converter import *

def app():
    st.title("Season Translation using CycleGAN")
    st.write("Manav Ukani - 20BCP167")
    st.write("Jenis Gundaraniya - 20BCP157")

    style="summer2winter"
    styles = ['winter2summer', 'summer2winter']
    style = st.selectbox('Select a style:', styles)
    
    season = style[:6]
    image_file = st.file_uploader(f"Upload an {season} image file", type=["jpg", "jpeg", "png"])
    
    if image_file is not None:
        image = np.asarray(bytearray(image_file.read()), dtype=np.uint8)
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        st.image(image, channels='BGR', caption='Uploaded Image')
        
        
        color_coverted = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image_1=Image.fromarray(color_coverted.astype('uint8'), 'RGB')

        final=stylise(image_1,style)
        st.image(np.array(final), caption="Processed image")

if __name__ == '__main__':
    app()