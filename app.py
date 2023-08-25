from flask import Flask, render_template, flash, get_flashed_messages, redirect, url_for, request
import datetime

import forms

app=Flask(__name__)
app.config['SECRET_KEY']='MauricioRafael2103'

@app.route('/solution', methods=['GET', 'POST'])
def solution(diff, date1, date2):
    answr=str(diff)
    resp=answr.split()
    return render_template('solution.html', 
    difference=(resp[0]+" days"), date1=date1, date2=date2)

@app.route('/')
@app.route('/calculation', methods=['GET', 'POST'])
def calculation():
    form = forms.InputDatesForm()
    if form.validate_on_submit():
        date1 = form.date1.data
        date2 = form.date2.data
        if date2>date1:
            diff= date2-date1
        else:
            diff=date1-date2
        return solution(diff, date1, date2)
    return render_template('calculation.html', form=form)



if __name__ == '__main__':
    app.run(debug=True)
