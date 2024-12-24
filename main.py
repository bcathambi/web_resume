import streamlit as sg

col1, col2 = sg.columns(2)

with col1:
	sg.image('../images/photo.png')

with col2:
	sg.title('Nallathambi L')
	content ='''
	Having 3.5years experience in Automotive sector.
	Expertize in Entertainment, IVIS, OTA and NVH.
	'''
	sg.write(content)