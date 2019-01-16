#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 15:01:07 2019

@author: donaldwalker
"""
# import necessary libraries
from flask import Flask, render_template
from valuation import stock_data_df, fin_dict
# create instance of Flask app
app = Flask(__name__)

print(fin_dict.keys())
# Set dataframe variables
comp_names = fin_dict['Name']
comp_price = fin_dict['Price']
comp_drange = fin_dict['Day Range']
comp_yr_range = fin_dict['52W_Range']
comp_avg_vol = fin_dict['Average Volume']
comp_mcap = fin_dict['Market Cap']
comp_yield = fin_dict['Dividend Yield']
comp_beta = fin_dict['Beta']
comp_eps = fin_dict['EPS']
comp_pe = fin_dict['PE']
comp_target = fin_dict['Target']
comp_recc = fin_dict['Reccomendation']

print(comp_names.values())

# create route that renders stocks_flask.html template
@app.route("/")
def index():

    return render_template("stocks_flask.html", stocks=comp_names,
                                                price=comp_price,
                                                prange=comp_drange,
                                                yrange=comp_yr_range,
                                                vol=comp_avg_vol,
                                                mcap=comp_mcap,
                                                pyield=comp_yield,
                                                betas = comp_beta,
                                                eps = comp_eps,
                                                pe = comp_pe,
                                                beta = comp_target,
                                                recc=comp_recc
                                                )

if __name__ == "__main__":
    app.run(debug=True)