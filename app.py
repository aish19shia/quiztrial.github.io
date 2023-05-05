from flask import Flask, redirect, render_template, request,session
app=Flask(__name__)
app.config['SECRET_KEY']='1234'



attempted_questions = []
@app.route('/')
def home():
    return render_template('instruction_page.html')

@app.route('/qp1', methods=['GET', 'POST'])
def qp1():
    session.clear()
    attempted_questions.clear()
    score=session.get('score',0)
    #user is not available i.e not logged in
    # if session.get('authenticated') != True:
    #     return redirect('/login_page')
    if request.method=='GET':
        return render_template('q1.html')
    elif request.method=='POST':
        correct_ans='c'
        user_option=request.form.get('option')
        message=''
        if "q1" not in attempted_questions:
            attempted_questions.append('q1')
            if user_option==correct_ans:
                message='CORRECT ANSWER'
                score=score+10
                session['score']=score
            else:
                message='INCORRECT ANSWER'
        else:
            message = 'already attempted'
    return render_template('q1.html', message=message)

@app.route('/qp2', methods=['GET', 'POST'])  
def qp2():
    score=session.get('score',0)
    if request.method=='GET':
        return render_template('q2.html')
    elif request.method=='POST':
        correct_ans='b'
        user_option=request.form.get('option')
        message=''
        if "q2" not in attempted_questions:
            attempted_questions.append('q2')
            if user_option==correct_ans:
                message='CORRECT ANSWER'
                score=score+10
                session['score']=score
            else:
                message='INCORRECT ANSWER'
        else:
            message = 'already attempted'
    return render_template('q2.html', message=message)
    
@app.route('/qp3', methods=['GET', 'POST'])
def qp3():
    score=session.get('score',0)
    if request.method=='GET':
        return render_template('q3.html')
    elif request.method=='POST':
        correct_ans='d'
        user_option=request.form.get('option')
        message=''
        if "q3" not in attempted_questions:
            attempted_questions.append('q3')
            if user_option==correct_ans:
                message='CORRECT ANSWER'
                score=score+10
                session['score']=score
            else:
                message='INCORRECT ANSWER'
        else:
            message = 'already attempted'
    return render_template('q3.html', message=message)

@app.route('/qp4', methods=['GET', 'POST'])
def qp4():
    score=session.get('score',0)
    if request.method=='GET':
        return render_template('q4.html')
    elif request.method=='POST':
        correct_ans='c'
        user_option=request.form.get('option')
        message=''
        if "q4" not in attempted_questions:
            attempted_questions.append('q4')
            if user_option==correct_ans:
                message='CORRECT ANSWER'
                score=score+10
                session['score']=score
            else:
                message='INCORRECT ANSWER'
        else:
            message = 'already attempted'
    return render_template('q4.html', message=message)

@app.route('/qp5', methods=['GET', 'POST'])
def qp5():
    score=session.get('score',0)
    if request.method=='GET':
        return render_template('q5.html')
    elif request.method=='POST':
        correct_ans='b'
        user_option=request.form.get('option')
        message=''
        if "q5" not in attempted_questions:
            attempted_questions.append('q5')
            if user_option==correct_ans:
                message='CORRECT ANSWER'
                score=score+10
                session['score']=score
            else:
                message='INCORRECT ANSWER'
        else:
            message = 'already attempted'
    return render_template('q5.html', message=message)

@app.route('/qp6', methods=['GET', 'POST'])
def qp6():
    score=session.get('score',0)
    if request.method=='GET':
        return render_template('q6.html')
    elif request.method=='POST':
        correct_ans='b'
        user_option=request.form.get('option')
        message=''
        if "q6" not in attempted_questions:
            attempted_questions.append('q6')
            if user_option==correct_ans:
                message='CORRECT ANSWER'
                score=score+10
                session['score']=score
            else:
                message='INCORRECT ANSWER'
        else:
            message = 'already attempted'
    return render_template('q6.html', message=message)

@app.route('/qp7', methods=['GET', 'POST'])
def qp7():
    score=session.get('score',0)
    if request.method=='GET':
        return render_template('q7.html')
    elif request.method=='POST':
        correct_ans='c'
        user_option=request.form.get('option')
        message=''
        if "q7" not in attempted_questions:
            attempted_questions.append('q7')
            if user_option==correct_ans:
                message='CORRECT ANSWER'
                score=score+10
                session['score']=score
            else:
                message='INCORRECT ANSWER'
        else:
            message = 'already attempted'
    return render_template('q7.html', message=message)

@app.route('/qp8', methods=['GET', 'POST'])
def qp8():
    score=session.get('score',0)
    if request.method=='GET':
        return render_template('q8.html')
    elif request.method=='POST':
        correct_ans='b'
        user_option=request.form.get('option')
        message=''
        if "q8" not in attempted_questions:  
            attempted_questions.append('q8')  
            if user_option==correct_ans:
                message='CORRECT ANSWER'
                score=score+10
                session['score']=score
            else:
                message='INCORRECT ANSWER'
        else:
            message = 'already attempted'
    return render_template('q8.html', message=message)

@app.route('/qp9', methods=['GET', 'POST'])
def qp9():
    score=session.get('score',0)
    if request.method=='GET':
        return render_template('q9.html')
    elif request.method=='POST':
        correct_ans='d'
        user_option=request.form.get('option')
        message=''
        if "q9" not in attempted_questions:  
            attempted_questions.append('q9')  
            if user_option==correct_ans:
                message='CORRECT ANSWER'
                score=score+10
                session['score']=score
            else:
                message='INCORRECT ANSWER'
        else:
            message = 'already attempted'
    return render_template('q9.html', message=message)

@app.route('/qp10', methods=['GET', 'POST'])
def qp10():
    score=session.get('score',0)
    if request.method=='GET':
        return render_template('q10.html')
    elif request.method=='POST':
        correct_ans='b'
        user_option=request.form.get('option')
        message=''
        if "q10" not in attempted_questions:  
            attempted_questions.append('q10')  
            if user_option==correct_ans:
                message='CORRECT ANSWER'
                score=score+10
                session['score']=score
            else:
                message='INCORRECT ANSWER'
        else:
            message = 'already attempted'
    return render_template('q10.html', message=message)
    
@app.route('/summary')
def summary():
    return render_template('summary.html')

    
if __name__=='__main__':
    app.run(debug=True)




    