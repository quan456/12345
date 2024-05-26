# B1: nhap vao 1 ten ai do. Khi bam xac nhan. Thi hien thi xin chao + ten nguoi do.

import streamlit as t
import time as a
t.title("lo")
f = open("so",'r')
n = t.text_input(":")
btn = t.button(".")
pro_t = t.progress(0)
if btn:
  for i in range(0,100):
    a.sleep(0.5)
    pro_t.progress(i)

  t.write("lo",n)

# B2: Tao thanh progress tu tang den 100%



