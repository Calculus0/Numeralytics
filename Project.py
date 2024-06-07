#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 00:23:15 2024

"""
import streamlit as st

st.set_page_config(page_title="My Webpage", layout="wide")
import time


import mathgenerator as mg

import multiprocessing

from gtts import gTTS


#import os
import random

from playsound import playsound  
#import welcome.mp3

def convert_math_expression(expression):

    expression = expression.replace('^', ' raised to the power of')
    expression = expression.replace('*', '')

    return expression

def problemgenerator(problist):
    choice = random.choice(problist)
    problem, solution = eval(choice)
    problem = problem.replace("$", "")
    problem = convert_math_expression(problem)
    return problem


st.title("Welcome to Numeralytics") #CHange


st.write("Kabir") #Change



topic = st.radio(
     'Choose your topic',
     ('Select', 'Calculus', 'Algebra', 'Statistics', 'Basic Math'))

st.write('You selected:', topic)


if topic == 'Calculus':
    st.write("Your question is being generated")
    time.sleep(7.5)
    st.write("Here's your question")
    calclist = ['mg.power_rule_integration()', 'mg.power_rule_differentiation()','mg.definite_integral()', 'mg.stationary_points()']
    problem = problemgenerator(calclist)
    speech = gTTS(problem)
    speech.save("welcome.mp3")
    playsound("welcome.mp3")

if topic == 'Algebra':
    st.write("Your question is being generated")
    time.sleep(7.5)
    st.write("Here's your question")
    alglist = ['mg.basic_algebra()', 'mg.factoring()','mg.system_of_equations()', 'mg.linear_equations()']
    problem = problemgenerator(alglist)
    speech = gTTS(problem)
    speech.save("welcome.mp3")
    playsound("welcome.mp3")

    
if topic == 'Statistics':
    st.write("Your question is being generated")
    time.sleep(7.5)
    st.write("Here's your question")
    statlist = ['mg.combinations()', 'mg.permutation()','mg.dice_sum_probability()', 'mg.data_summary()']
    problem = problemgenerator(statlist)
    speech = gTTS(problem)
    speech.save("welcome.mp3")
    playsound("welcome.mp3")
   
if topic == 'Basic Math':
    st.write("Your question is being generated")
    time.sleep(7.5)
    st.write("Here's your question")
    mathlist = ['mg.factorial()', 'mg.exponentiation()','mg.percentage()', 'mg.is_prime()']
    problem = problemgenerator(mathlist)
    speech = gTTS(problem)
    speech.save("welcome.mp3")
    playsound("welcome.mp3")
    
    

