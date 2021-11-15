# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 16:57:44 2021

@author: nonno
"""

import streamlit as st
st.title("今日のクイズ")
st.write("何問正解できるかな？")

opinion = st.write(
    "11月15日は、「いいインコの日」だそうです。ほっぺたの真っ赤な模様が特徴の「オカメインコ」。歌っている可愛い姿が度々SNSで拡散されたりする人気者ですが、実は、オカメインコはインコではない。◯か×か")
left_column, right_column = st.columns(2)
button1 = left_column.button("〇")
button2 = right_column.button("×")
if on_click = None:
elif button1:
    st.title("正解です！")
else:
    st.title("残念！")