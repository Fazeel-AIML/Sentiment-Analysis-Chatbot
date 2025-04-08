from flask import Flask, render_template, request
from emotion_detector import detect_emotion
from response_generator import generate_response

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    user_input = ''
    response = ''
    emotion = ''
    
    if request.method == 'POST':
        user_input = request.form['user_input']
        emotion = detect_emotion(user_input)
        response = generate_response(user_input)

    return render_template('index.html', user_input=user_input, emotion=emotion, response=response)

if __name__ == '__main__':
    app.run(debug=True)
