import streamlit as st
import pandas as pd
import openpyxl
import requests
import json

title = st.text_input("输入标题")
text = st.text_area("输入文本")

def raw_to_df(data):
    raw_list = data.splitlines(False)
    # header = raw_list[1].split()
    header = ['英文名', 'PWR', '平均抓位', '平均打出回合', '分发次数', '选择次数', '打出次数', '获胜次数(含未打出)', '获胜次数(仅统计打出)']
    df = pd.DataFrame(columns = header)
    for index in range(2, len(raw_list) - 1):
        l, r = 0, 0
        for i in range(len(raw_list[index]) - 1):
            if not raw_list[index][i].isalpha() and raw_list[index][i+1].isalpha() and l <= 0: l = i
            if raw_list[index][i].isalpha() and not raw_list[index][i+1].isalpha(): r = i
        tmp = [raw_list[index][l + 1 : r + 1]]
        tmp += raw_list[index][r + 2 :].split()
        df.loc[df.shape[0] - 1] = tmp
    df.reset_index(inplace=True, drop=True)
    # res['机翻'] = res['英文名'].apply(translate)
    return df
    # res.to_excel('./sample.xlsx', index = False)
    # res.tail(20)
    
if title != '':
    path = './'+title+'.xlsx'
    output_file = raw_to_df(text).to_excel(path, index=False)

    with open(path, 'rb') as my_file:
        st.download_button(label = 'Download', data = my_file, file_name = title+'.xlsx', mime = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')    
