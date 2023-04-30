from flask import Flask, render_template, request
import response

application = Flask(__name__)

@application.route('/')
def main_handler():
    print("main_handler -- ")
    return render_template('index.html')

@application.route('/piepie', methods=['POST'])
def piepie_handler():
    input_text = request.form['input_text']
    print("PiePieHandler --", input_text)
    piepie_text = "input:\t" + input_text + "\nresponse:\t" + response.piepie_response(input_text)
    return piepie_text

if __name__ == '__main__':
    print("__main__ --")
    application.run(host='0.0.0.0', port=5000, debug=True)
