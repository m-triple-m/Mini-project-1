from os import times

import cv2
import numpy as np
from pyzbar.pyzbar import decode
from PIL import Image
import cv2,time
import csv
import streamlit as st

present_students = set()

video = cv2.VideoCapture(0)


st.title('Attendence system')

students =[]

sidebar = st.sidebar

sidebar.title('Present student list')

for stu in present_students:
    st.sub_title(stu)

with open('Book1.csv','r') as file:
    reader=csv.reader(file)
    for row in reader:
        students.append((row[1]))

print(students)

run = st.checkbox('Run')
if run:
    while True:
        check,frame= video.read()
        d=decode(frame) 
        try:
            for obj in d:
                name=d[0].data.decode()
                print(name)
                if name in students:
                    students.remove(name)
                    present_students.add(name)
                    print('deleted.....')


        except:
            print('error')


        cv2.imshow('Attendence',frame)
        key=cv2.waitKey(1)
        if key==ord('q'):
            print(students)
            break

video.release()
cv2.destroyAllWindows()                    

     
     
