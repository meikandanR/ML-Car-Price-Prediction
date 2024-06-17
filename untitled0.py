from flask import Flask
app=Flask(__name__)
app.route('/')
def helo():
    return "helo meikandan"

if __name__=="__main__":
    app.run(debug=True)