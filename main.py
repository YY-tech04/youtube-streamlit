import pandas as pd
import numpy as np
import streamlit as st
from PIL import Image
import time


st.title('streamlit 超入門')
st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!'



     






left_column,right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')


expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')
#text= st.text_input('あなたの趣味を教えてください。')
#condition = st.slider('あなたの今の調子は？',0,10,5)

#'あなたの趣味：',text
#'condition:',condition



#option = st.selectbox(
#   'あなたが好きな数字を選んでください',
#   list(range(1,11))
#)




#if st.checkbox('Show Image'):
#   img= Image.open('sample.jpg')
#   st.image(img, caption='aya',use_column_width=True)


   
#df = pd.DataFrame(
#    np.random.rand(100,2)/[50,50]+[35.69,139.70],
#    columns=['lat','lon']
#)

#st.map(df)

#st.dataframe(df.style.highlight_max(axis=0))
#dataferame :表示させるサイズを指定できる。ｗriteは表示だけでサイズは変更できない。table：静的な表を作れる
#axis は、列か行をしていする。　列:0、行:1

