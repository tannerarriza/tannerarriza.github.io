from flask import Flask, render_template
import plotly
from plotly import io
import plotly.graph_objects as go
import pandas as pd
import json

# Configure application
app = Flask(__name__, template_folder='./templates')

@app.route('/index', methods=['POST', 'GET'])
@app.route('/', methods=['POST', 'GET'])
def index():
    greeting = "Hi, I'm Tanner, a Data Scientist in the SF Bay Area 🌁"
    intro = "On this site, you can find my blogs, personal projects, and data science educational content I've developed over the years."
    personal_education = "For 2021, I made a promise to myself learn new topics across a multitude of domains, including finance, software engineering, reinforcement learning, and many other topics. I will be documenting my progress on this website, and will try to share notes/personal projects that apply to the topic. My first topic of focus is investing! Check out the box to the right to learn more."
    current_project = "Currently, I am really interested in algorithmic trading, and have been reading a lot about powerful techniques in quantitative finance. My goal is to conduct much better portfolio analysis over time, and try my hand at deploying algorithms to try to make a positive ROI. Click the box to left to see my progress."

    return render_template('/index.html', 
                            greeting=greeting, 
                            intro=intro, 
                            personal_education=personal_education, 
                            current_project=current_project)

@app.route('/portfolio', methods=['POST', 'GET'])
def portfolio():
    portfolio_intro = "Glad to see you are interested in my work! This page is currently under construction, as my goal is to make this my entire portfolio filterable. But for the time being, make sure to check out my projects I've done in my free time."
    
    return render_template('/portfolio.html', 
                            portfolio_intro=portfolio_intro)

@app.route('/education', methods=['POST', 'GET'])
def education():
    education_intro = "After graduating college, I felt that I was still craving to learn more about a variety of topics — especially the intersection of data science and business. Thus, I have taken it upon myself to gradually gain knowledge in fields I find interesting. Further, I have always been an advocate of sharing knowledge at any level, so whenever I tackle a new subject, I will make sure to post my notes, Jupyter notebooks, and other materials here! In addition, I have developed my own workshops on topics in the past, so feel free to check those out as well."

    return render_template('/education.html', 
                            education_intro=education_intro)

@app.route('/investing', methods=['POST', 'GET'])
def investing():
    return render_template('/investing.html')

@app.route('/data_engineering', methods=['POST', 'GET'])
def data_engineering():
    return render_template('/data_engineering.html')

@app.route('/experimentation', methods=['POST', 'GET'])
def experimentation():
    return render_template('/experimentation.html')

@app.route('/recommendation', methods=['POST', 'GET'])
def recommendation():
    return render_template('/recommendation.html')

@app.route('/reinforcement_learning', methods=['POST', 'GET'])
def reinforcement_learning():
    return render_template('/reinforcement_learning.html')

@app.route('/ui_ux', methods=['POST', 'GET'])
def ui_ux():
    return render_template('/ui_ux.html')