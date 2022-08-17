from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('chats.html')

@app.route('/chat_gunhee')
def chat_gunhee():
   return render_template('chat_gunhee.html')

@app.route('/chat_seungtae')
def chat_seungtae():
   return render_template('chat_seungtae.html')

@app.route('/chat_sijosijo')
def chat_sijosijo():
   return render_template('chat_sijosijo.html')

@app.route('/chat_woojin')
def chat_woojin():
   return render_template('chat_woojin.html')

@app.route('/chat_yunji')
def chat_yunji():
   return render_template('chat_yunji.html')

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)