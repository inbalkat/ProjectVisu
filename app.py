import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Hardcoded data from the Excel file
data = [
    {"product": "avocado", "year": 2015, "yearly average price": 6.72993197278912},
    {"product": "rice", "year": 2015, "yearly average price": 9.59583333333333},
    {"product": "eggs", "year": 2015, "yearly average price": 23.2333333333332},
    {"product": "banana", "year": 2015, "yearly average price": 3.64772727272727},
    {"product": "onion", "year": 2015, "yearly average price": 3.41371681415929},
    {"product": "fresh ground beef", "year": 2015, "yearly average price": 61.0983333333333},
    {"product": "white cheese", "year": 2015, "yearly average price": 5.0825},
    {"product": "yellow cheese", "year": 2015, "yearly average price": 43.8933333333333},
    {"product": "cottage", "year": 2015, "yearly average price": 5.86333333333333},
    {"product": "honey", "year": 2015, "yearly average price": 19.8266666666667},
    {"product": "chicken breast", "year": 2015, "yearly average price": 33.3125},
    {"product": "milk", "year": 2015, "yearly average price": 6.05},
    {"product": "chocolate bar", "year": 2015, "yearly average price": 6.1125},
    {"product": "tahini", "year": 2015, "yearly average price": 14.5675},
    {"product": "brown bread", "year": 2015, "yearly average price": 5.09666666666666},
    {"product": "white bread", "year": 2015, "yearly average price": 5.09666666666666},
    {"product": "lemon", "year": 2015, "yearly average price": 4.87954545454545},
    {"product": "cucumber", "year": 2015, "yearly average price": 4.52906976744186},
    {"product": "tomato", "year": 2015, "yearly average price": 7.31594827586207},
    {"product": "pasta", "year": 2015, "yearly average price": 5.3425},
    {"product": "white flour", "year": 2015, "yearly average price": 4.0875},
    {"product": "coffee", "year": 2015, "yearly average price": 23.4866666666667},
    {"product": "tomato sauce", "year": 2015, "yearly average price": 1.84583333333333},
    {"product": "olive oil", "year": 2015, "yearly average price": 34.415},
    {"product": "canola oil", "year": 2015, "yearly average price": 10.7408333333333},
    {"product": "strawberry", "year": 2015, "yearly average price": 33.4095238095238},
    {"product": "corn", "year": 2015, "yearly average price": 5.60476190476191},
    {"product": "apple", "year": 2015, "yearly average price": 5.97113402061856},
    {"product": "potato", "year": 2015, "yearly average price": 1.99542483660131},
    {"product": "avocado", "year": 2016, "yearly average price": 11.0311669128508},
    {"product": "rice", "year": 2016, "yearly average price": 9.5675},
    {"product": "eggs", "year": 2016, "yearly average price": 22},
    {"product": "banana", "year": 2016, "yearly average price": 5.59676113360324},
    {"product": "onion", "year": 2016, "yearly average price": 3.22815158546017},
    {"product": "fresh ground beef", "year": 2016, "yearly average price": 60.1366666666667},
    {"product": "white cheese", "year": 2016, "yearly average price": 4.69166666666667},
    {"product": "yellow cheese", "year": 2016, "yearly average price": 41.3},
    {"product": "cottage", "year": 2016, "yearly average price": 5.70583333333333},
    {"product": "honey", "year": 2016, "yearly average price": 20.2775},
    {"product": "chicken breast", "year": 2016, "yearly average price": 32.6483333333333},
    {"product": "milk", "year": 2016, "yearly average price": 5.75},
    {"product": "chocolate bar", "year": 2016, "yearly average price": 6.0525},
    {"product": "tahini", "year": 2016, "yearly average price": 13.2258333333333},
    {"product": "brown bread", "year": 2016, "yearly average price": 5.09666666666666},
    {"product": "white bread", "year": 2016, "yearly average price": 5.09666666666666},
    {"product": "lemon", "year": 2016, "yearly average price": 5.09140811455847},
    {"product": "cucumber", "year": 2016, "yearly average price": 3.9515625},
    {"product": "tomato", "year": 2016, "yearly average price": 5.96967787114846},
    {"product": "pasta", "year": 2016, "yearly average price": 5.48333333333333},
    {"product": "white flour", "year": 2016, "yearly average price": 4.06166666666667},
    {"product": "coffee", "year": 2016, "yearly average price": 23.6108333333333},
    {"product": "tomato sauce", "year": 2016, "yearly average price": 1.73416666666667},
    {"product": "olive oil", "year": 2016, "yearly average price": 33.75},
    {"product": "canola oil", "year": 2016, "yearly average price": 10.405},
    {"product": "strawberry", "year": 2016, "yearly average price": 19.2110091743119},
    {"product": "corn", "year": 2016, "yearly average price": 6.15720720720721},
    {"product": "apple", "year": 2016, "yearly average price": 5.59261744966442},
    {"product": "potato", "year": 2016, "yearly average price": 2.55453815261044},
    {"product": "avocado", "year": 2017, "yearly average price": 10.323395149786},
    {"product": "rice", "year": 2017, "yearly average price": 9.42583333333334},
    {"product": "eggs", "year": 2017, "yearly average price": 22},
    {"product": "banana", "year": 2017, "yearly average price": 6.38966789667897},
    {"product": "onion", "year": 2017, "yearly average price": 3.14852173913044},
    {"product": "fresh ground beef", "year": 2017, "yearly average price": 57.3858333333333},
    {"product": "white cheese", "year": 2017, "yearly average price": 4.54},
    {"product": "yellow cheese", "year": 2017, "yearly average price": 41.3},
    {"product": "cottage", "year": 2017, "yearly average price": 5.64333333333333},
    {"product": "honey", "year": 2017, "yearly average price": 20.5291666666667},
    {"product": "chicken breast", "year": 2017, "yearly average price": 31.8758333333333},
    {"product": "milk", "year": 2017, "yearly average price": 5.75},
    {"product": "chocolate bar", "year": 2017, "yearly average price": 5.90416666666667},
    {"product": "tahini", "year": 2017, "yearly average price": 12.1116666666667},
    {"product": "brown bread", "year": 2017, "yearly average price": 5.09666666666666},
    {"product": "white bread", "year": 2017, "yearly average price": 5.09666666666666},
    {"product": "lemon", "year": 2017, "yearly average price": 4.95505617977528},
    {"product": "cucumber", "year": 2017, "yearly average price": 3.79153225806452},
    {"product": "tomato", "year": 2017, "yearly average price": 5.87507418397627},
    {"product": "pasta", "year": 2017, "yearly average price": 5.305},
    {"product": "white flour", "year": 2017, "yearly average price": 3.9775},
    {"product": "coffee", "year": 2017, "yearly average price": 24.0133333333333},
    {"product": "tomato sauce", "year": 2017, "yearly average price": 1.72333333333333},
    {"product": "olive oil", "year": 2017, "yearly average price": 33.6625},
    {"product": "canola oil", "year": 2017, "yearly average price": 10.345},
    {"product": "strawberry", "year": 2017, "yearly average price": 19.4255639097744},
    {"product": "corn", "year": 2017, "yearly average price": 5.5962962962963},
    {"product": "apple", "year": 2017, "yearly average price": 5.57175849554603},
    {"product": "potato", "year": 2017, "yearly average price": 3.29635145197319},
    {"product": "avocado", "year": 2018, "yearly average price": 12.2313453536755},
    {"product": "rice", "year": 2018, "yearly average price": 9.92833333333333},
    {"product": "eggs", "year": 2018, "yearly average price": 22},
    {"product": "banana", "year": 2018, "yearly average price": 4.19935622317597},
    {"product": "onion", "year": 2018, "yearly average price": 3.7956072351421},
    {"product": "fresh ground beef", "year": 2018, "yearly average price": 56.425},
    {"product": "white cheese", "year": 2018, "yearly average price": 4.54916666666667},
    {"product": "yellow cheese", "year": 2018, "yearly average price": 41.3},
    {"product": "cottage", "year": 2018, "yearly average price": 5.675},
    {"product": "honey", "year": 2018, "yearly average price": 19.7308333333333},
    {"product": "chicken breast", "year": 2018, "yearly average price": 31.75},
    {"product": "milk", "year": 2018, "yearly average price": 5.75},
    {"product": "chocolate bar", "year": 2018, "yearly average price": 5.9525},
    {"product": "tahini", "year": 2018, "yearly average price": 11.6958333333333},
    {"product": "brown bread", "year": 2018, "yearly average price": 5.12},
    {"product": "white bread", "year": 2018, "yearly average price": 5.12},
    {"product": "lemon", "year": 2018, "yearly average price": 4.34924406047516},
    {"product": "cucumber", "year": 2018, "yearly average price": 4.12862745098039},
    {"product": "tomato", "year": 2018, "yearly average price": 6.23728598604946},
    {"product": "pasta", "year": 2018, "yearly average price": 5.33666666666667},
    {"product": "white flour", "year": 2018, "yearly average price": 3.8875},
    {"product": "coffee", "year": 2018, "yearly average price": 24.3008333333333},
    {"product": "tomato sauce", "year": 2018, "yearly average price": 1.6425},
    {"product": "olive oil", "year": 2018, "yearly average price": 33.7975},
    {"product": "canola oil", "year": 2018, "yearly average price": 10.0208333333333},
    {"product": "strawberry", "year": 2018, "yearly average price": 17.8650485436893},
    {"product": "corn", "year": 2018, "yearly average price": 5.89955752212389},
    {"product": "apple", "year": 2018, "yearly average price": 6.71564142194749},
    {"product": "potato", "year": 2018, "yearly average price": 3.08100743187448},
    {"product": "avocado", "year": 2019, "yearly average price": 11.7970588235294},
    {"product": "rice", "year": 2019, "yearly average price": 10.1191666666667},
    {"product": "eggs", "year": 2019, "yearly average price": 21.7},
    {"product": "banana", "year": 2019, "yearly average price": 5.18169398907104},
    {"product": "onion", "year": 2019, "yearly average price": 3.65857933579336},
    {"product": "fresh ground beef", "year": 2019, "yearly average price": 52.8508333333333},
    {"product": "white cheese", "year": 2019, "yearly average price": 4.68166666666667},
    {"product": "yellow cheese", "year": 2019, "yearly average price": 42.7},
    {"product": "cottage", "year": 2019, "yearly average price": 5.66833333333333},
    {"product": "honey", "year": 2019, "yearly average price": 20.0225},
    {"product": "chicken breast", "year": 2019, "yearly average price": 33.245},
    {"product": "milk", "year": 2019, "yearly average price": 5.94},
    {"product": "chocolate bar", "year": 2019, "yearly average price": 6.075},
    {"product": "tahini", "year": 2019, "yearly average price": 12.4708333333333},
    {"product": "brown bread", "year": 2019, "yearly average price": 5.12},
    {"product": "white bread", "year": 2019, "yearly average price": 5.12},
    {"product": "lemon", "year": 2019, "yearly average price": 5.65349344978166},
    {"product": "cucumber", "year": 2019, "yearly average price": 4.34574898785425},
    {"product": "tomato", "year": 2019, "yearly average price": 6.60433869839048},
    {"product": "pasta", "year": 2019, "yearly average price": 5.30333333333333},
    {"product": "white flour", "year": 2019, "yearly average price": 3.79833333333333},
    {"product": "coffee", "year": 2019, "yearly average price": 24.0083333333333},
    {"product": "tomato sauce", "year": 2019, "yearly average price": 1.69333333333333},
    {"product": "olive oil", "year": 2019, "yearly average price": 32.9758333333333},
    {"product": "canola oil", "year": 2019, "yearly average price": 10.0666666666667},
    {"product": "strawberry", "year": 2019, "yearly average price": 19.9045871559633},
    {"product": "corn", "year": 2019, "yearly average price": 6.45544041450777},
    {"product": "apple", "year": 2019, "yearly average price": 7.8690152565881},
    {"product": "potato", "year": 2019, "yearly average price": 3.70612840466926},
    {"product": "avocado", "year": 2020, "yearly average price": 13.8240884718499},
    {"product": "rice", "year": 2020, "yearly average price": 10.2241666666667},
    {"product": "eggs", "year": 2020, "yearly average price": 21.7},
    {"product": "banana", "year": 2020, "yearly average price": 4.72627118644068},
    {"product": "onion", "year": 2020, "yearly average price": 3.39427118644068},
    {"product": "fresh ground beef", "year": 2020, "yearly average price": 51.945},
    {"product": "white cheese", "year": 2020, "yearly average price": 4.7475},
    {"product": "yellow cheese", "year": 2020, "yearly average price": 42.7},
    {"product": "cottage", "year": 2020, "yearly average price": 5.69583333333333},
    {"product": "honey", "year": 2020, "yearly average price": 20.245},
    {"product": "chicken breast", "year": 2020, "yearly average price": 32.9491666666667},
    {"product": "milk", "year": 2020, "yearly average price": 5.94},
    {"product": "chocolate bar", "year": 2020, "yearly average price": 6.00916666666667},
    {"product": "tahini", "year": 2020, "yearly average price": 13.1841666666667},
    {"product": "brown bread", "year": 2020, "yearly average price": 5.12},
    {"product": "white bread", "year": 2020, "yearly average price": 5.12},
    {"product": "lemon", "year": 2020, "yearly average price": 6.07377777777778},
    {"product": "cucumber", "year": 2020, "yearly average price": 4.37215139442231},
    {"product": "tomato", "year": 2020, "yearly average price": 6.64580821917808},
    {"product": "pasta", "year": 2020, "yearly average price": 5.54083333333333},
    {"product": "white flour", "year": 2020, "yearly average price": 3.78083333333333},
    {"product": "coffee", "year": 2020, "yearly average price": 24.6066666666667},
    {"product": "tomato sauce", "year": 2020, "yearly average price": 1.61666666666667},
    {"product": "olive oil", "year": 2020, "yearly average price": 32.4116666666667},
    {"product": "canola oil", "year": 2020, "yearly average price": 10.5658333333333},
    {"product": "strawberry", "year": 2020, "yearly average price": 19.090447761194},
    {"product": "corn", "year": 2020, "yearly average price": 6.54886666666667},
    {"product": "apple", "year": 2020, "yearly average price": 8.09839912280701},
    {"product": "potato", "year": 2020, "yearly average price": 3.74579839429081},
    {"product": "avocado", "year": 2021, "yearly average price": 10.7469626904886},
    {"product": "rice", "year": 2021, "yearly average price": 10.515},
    {"product": "eggs", "year": 2021, "yearly average price": 21.7},
    {"product": "banana", "year": 2021, "yearly average price": 3.18186320754715},
    {"product": "onion", "year": 2021, "yearly average price": 3.11895212765955},
    {"product": "fresh ground beef", "year": 2021, "yearly average price": 53.8391666666667},
    {"product": "white cheese", "year": 2021, "yearly average price": 4.76916666666667},
    {"product": "yellow cheese", "year": 2021, "yearly average price": 42.7},
    {"product": "cottage", "year": 2021, "yearly average price": 5.66833333333333},
    {"product": "honey", "year": 2021, "yearly average price": 19.6716666666667},
    {"product": "chicken breast", "year": 2021, "yearly average price": 31.5016666666667},
    {"product": "milk", "year": 2021, "yearly average price": 5.94},
    {"product": "chocolate bar", "year": 2021, "yearly average price": 5.97583333333333},
    {"product": "tahini", "year": 2021, "yearly average price": 13.4441666666667},
    {"product": "brown bread", "year": 2021, "yearly average price": 5.12},
    {"product": "white bread", "year": 2021, "yearly average price": 5.12},
    {"product": "lemon", "year": 2021, "yearly average price": 4.27706249999997},
    {"product": "cucumber", "year": 2021, "yearly average price": 3.69568749999998},
    {"product": "tomato", "year": 2021, "yearly average price": 5.15909204758919},
    {"product": "pasta", "year": 2021, "yearly average price": 5.47},
    {"product": "white flour", "year": 2021, "yearly average price": 4.03166666666667},
    {"product": "coffee", "year": 2021, "yearly average price": 24.3666666666667},
    {"product": "tomato sauce", "year": 2021, "yearly average price": 1.67583333333333},
    {"product": "olive oil", "year": 2021, "yearly average price": 32.9116666666667},
    {"product": "canola oil", "year": 2021, "yearly average price": 11.055},
    {"product": "strawberry", "year": 2021, "yearly average price": 20.7222680412371},
    {"product": "corn", "year": 2021, "yearly average price": 5.7081666666667},
    {"product": "apple", "year": 2021, "yearly average price": 8.56079938802832},
    {"product": "potato", "year": 2021, "yearly average price": 3.0423440395306},
    {"product": "avocado", "year": 2022, "yearly average price": 8.33198283261802},
    {"product": "rice", "year": 2022, "yearly average price": 11.0383333333333},
    {"product": "eggs", "year": 2022, "yearly average price": 23.2},
    {"product": "banana", "year": 2022, "yearly average price": 4.70057220708448},
    {"product": "onion", "year": 2022, "yearly average price": 3.81651960784314},
    {"product": "fresh ground beef", "year": 2022, "yearly average price": 55.0033333333333},
    {"product": "white cheese", "year": 2022, "yearly average price": 4.81333333333333},
    {"product": "yellow cheese", "year": 2022, "yearly average price": 44.79},
    {"product": "cottage", "year": 2022, "yearly average price": 5.68166666666667},
    {"product": "honey", "year": 2022, "yearly average price": 19.5733333333333},
    {"product": "chicken breast", "year": 2022, "yearly average price": 33.8866666666667},
    {"product": "milk", "year": 2022, "yearly average price": 6.23},
    {"product": "chocolate bar", "year": 2022, "yearly average price": 4.71583333333333},
    {"product": "tahini", "year": 2022, "yearly average price": 13.5758333333333},
    {"product": "brown bread", "year": 2022, "yearly average price": 6.96},
    {"product": "white bread", "year": 2022, "yearly average price": 6.97},
    {"product": "lemon", "year": 2022, "yearly average price": 4.70078353253652},
    {"product": "cucumber", "year": 2022, "yearly average price": 4.29410052910053},
    {"product": "tomato", "year": 2022, "yearly average price": 6.95176367614878},
    {"product": "pasta", "year": 2022, "yearly average price": 5.8275},
    {"product": "white flour", "year": 2022, "yearly average price": 4.51583333333333},
    {"product": "coffee", "year": 2022, "yearly average price": 24.3191666666667},
    {"product": "tomato sauce", "year": 2022, "yearly average price": 1.72833333333333},
    {"product": "olive oil", "year": 2022, "yearly average price": 32.5466666666667},
    {"product": "canola oil", "year": 2022, "yearly average price": 12.9216666666667},
    {"product": "strawberry", "year": 2022, "yearly average price": 22.3228409090909},
    {"product": "corn", "year": 2022, "yearly average price": 6.5923127753304},
    {"product": "apple", "year": 2022, "yearly average price": 8.14779072994727},
    {"product": "potato", "year": 2022, "yearly average price": 3.69328081556997},
    {"product": "avocado", "year": 2023, "yearly average price": 11.4190417690418},
    {"product": "rice", "year": 2023, "yearly average price": 11.1783333333333},
    {"product": "eggs", "year": 2023, "yearly average price": 26.86},
    {"product": "banana", "year": 2023, "yearly average price": 3.71337448559671},
    {"product": "onion", "year": 2023, "yearly average price": 4.7146499102334},
    {"product": "fresh ground beef", "year": 2023, "yearly average price": 56.6841666666667},
    {"product": "white cheese", "year": 2023, "yearly average price": 5.23833333333333},
    {"product": "yellow cheese", "year": 2023, "yearly average price": 48.725},
    {"product": "cottage", "year": 2023, "yearly average price": 5.97333333333333},
    {"product": "honey", "year": 2023, "yearly average price": 19.6183333333333},
    {"product": "chicken breast", "year": 2023, "yearly average price": 39.1675},
    {"product": "milk", "year": 2023, "yearly average price": 6.77999999999999},
    {"product": "chocolate bar", "year": 2023, "yearly average price": 6.25583333333333},
    {"product": "tahini", "year": 2023, "yearly average price": 14.1316666666667},
    {"product": "brown bread", "year": 2023, "yearly average price": 7.3},
    {"product": "white bread", "year": 2023, "yearly average price": 7.31},
    {"product": "lemon", "year": 2023, "yearly average price": 4.41195071868583},
    {"product": "cucumber", "year": 2023, "yearly average price": 5.10772908366534},
    {"product": "tomato", "year": 2023, "yearly average price": 7.90056272586472},
    {"product": "pasta", "year": 2023, "yearly average price": 6.1925},
    {"product": "white flour", "year": 2023, "yearly average price": 4.73},
    {"product": "coffee", "year": 2023, "yearly average price": 24.6508333333333},
    {"product": "tomato sauce", "year": 2023, "yearly average price": 1.89},
    {"product": "olive oil", "year": 2023, "yearly average price": 34.0558333333333},
    {"product": "canola oil", "year": 2023, "yearly average price": 12.6033333333333},
    {"product": "strawberry", "year": 2023, "yearly average price": 28.8746575342466},
    {"product": "corn", "year": 2023, "yearly average price": 6.45277777777778},
    {"product": "apple", "year": 2023, "yearly average price": 8.16536735432501},
    {"product": "potato", "year": 2023, "yearly average price": 4.19650541516246},
    {"product": "avocado", "year": 2024, "yearly average price": 10.419703087886},
    {"product": "rice", "year": 2024, "yearly average price": 11.2716666666667},
    {"product": "eggs", "year": 2024, "yearly average price": 26.86},
    {"product": "banana", "year": 2024, "yearly average price": 4.1726369168357},
    {"product": "onion", "year": 2024, "yearly average price": 5.57551433389545},
    {"product": "fresh ground beef", "year": 2024, "yearly average price": 62.535},
    {"product": "white cheese", "year": 2024, "yearly average price": 5.62833333333333},
    {"product": "yellow cheese", "year": 2024, "yearly average price": 51.14},
    {"product": "cottage", "year": 2024, "yearly average price": 6.25},
    {"product": "honey", "year": 2024, "yearly average price": 20.03},
    {"product": "chicken breast", "year": 2024, "yearly average price": 42.6725},
    {"product": "milk", "year": 2024, "yearly average price": 7.11},
    {"product": "chocolate bar", "year": 2024, "yearly average price": 6.99},
    {"product": "tahini", "year": 2024, "yearly average price": 14.9475},
    {"product": "brown bread", "year": 2024, "yearly average price": 7.3},
    {"product": "white bread", "year": 2024, "yearly average price": 7.31},
    {"product": "lemon", "year": 2024, "yearly average price": 5.85032989690722},
    {"product": "cucumber", "year": 2024, "yearly average price": 5.51621513944223},
    {"product": "tomato", "year": 2024, "yearly average price": 10.2680198511166},
    {"product": "pasta", "year": 2024, "yearly average price": 6.31916666666667},
    {"product": "white flour", "year": 2024, "yearly average price": 4.79083333333333},
    {"product": "coffee", "year": 2024, "yearly average price": 25.735},
    {"product": "tomato sauce", "year": 2024, "yearly average price": 2.05},
    {"product": "olive oil", "year": 2024, "yearly average price": 43.9266666666667},
    {"product": "canola oil", "year": 2024, "yearly average price": 12.3466666666667},
    {"product": "strawberry", "year": 2024, "yearly average price": 33.1804761904762},
    {"product": "corn", "year": 2024, "yearly average price": 8.52699588477366},
    {"product": "apple", "year": 2024, "yearly average price": 8.49472890692955},
    {"product": "potato", "year": 2024, "yearly average price": 5.03435643564357}
]

# Convert to DataFrame
products_df = pd.DataFrame(data)

# Streamlit app title
st.title("Supermarket Product Prices Over Time")

# Define item icons
item_icons = {
    "apple": "🍎",
    "avocado": "🥑",
    "banana": "🍌",
    "brown bread": "🍞",
    "canola oil": "🛢️",
    "chicken breast": "🍗",
    "chocolate bar": "🍫",
    "coffee": "☕",
    "corn": "🌽",
    "cottage": "⬜",
    "cucumber": "🥒",
    "eggs": "🥚",
    "fresh ground beef": "🥩",
    "honey": "🍯",
    "lemon": "🍋",
    "milk": "🥛",
    "olive oil": "🫒",
    "onion": "🧅",
    "pasta": "🍝",
    "potato": "🥔",
    "rice": "🍚",
    "strawberry": "🍓",
    "tahini": "🥣",
    "tomato": "🍅",
    "tomato sauce": "🥫",
    "white bread": "🥖",
    "white cheese": "🫕",
    "white flour": "🌾",
    "yellow cheese": "🧀",
}

# Sort the items alphabetically
item_icons = dict(sorted(item_icons.items()))

# Initialize session state for basket
if "basket" not in st.session_state:
    st.session_state.basket = []

if "selected_products" not in st.session_state:
    st.session_state.selected_products = []

# Display the supermarket layout
st.subheader("Supermarket")
supermarket_html = """
<style>
    .item {
        display: inline-block;
        margin: 10px;
        cursor: pointer;
        font-size: 20px;
        text-align: center;
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 10px;
        white-space: nowrap;
        max-width: 150px;
        overflow: hidden;
        text-overflow: ellipsis;
    }
    .item:hover {
        transform: scale(1.2);
        transition: transform 0.2s;
        background-color: #f0f0f0;
    }
    .cart {
        font-size: 100px;
        margin-top: 20px;
        text-align: right;
        position: relative;
        display: flex;
        align-items: center;
        justify-content: flex-end;
    }
    .cart-items {
        font-size: 40px;
        margin-right: 20px;
    }
</style>
"""

st.markdown(supermarket_html, unsafe_allow_html=True)

columns = st.columns(5)
for index, (product, icon) in enumerate(item_icons.items()):
    with columns[index % 5]:
        if st.button(f"{icon} {product.capitalize()}"):
            if product in st.session_state.selected_products:
                st.session_state.selected_products.remove(product)
                st.session_state.basket.remove(icon)
            else:
                st.session_state.selected_products.append(product)
                st.session_state.basket.append(icon)

# Display the cart
cart_html = f"""
<div class='cart'>
    <div class='cart-items'>{' '.join(st.session_state.basket)}</div>
    🛒
</div>
"""
st.markdown(cart_html, unsafe_allow_html=True)

# Filter the dataset based on selected products
filtered_df = products_df[products_df['product'].isin(st.session_state.selected_products)]

# Calculate the yearly total for the selected products
if not filtered_df.empty:
    total_prices = (
        filtered_df.groupby('year')['yearly average price']
        .sum()
        .reset_index()
    )
else:
    total_prices = pd.DataFrame(columns=['year', 'yearly average price'])

# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(
    total_prices['year'],
    total_prices['yearly average price'],
    marker='o',
    color='black',
    linewidth=2,
    label="Total Basket Cost"
)

# Customize the plot
ax.set_xlabel("Year")
ax.set_ylabel("Total Cost (₪)")
ax.set_title("Yearly Total Cost of Selected Products")
ax.set_xticks(range(2015, 2025))  # Ensure all years are shown on the x-axis
ax.legend()
ax.grid(True)

# Display the plot in Streamlit
st.pyplot(fig)
