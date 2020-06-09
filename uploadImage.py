from flask import Flask, render_template, url_for
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/",methods=["GET","POST"])
def index2():
    if request.method == "POST":
        a = request.form.to_dict()
        print("Access",a["Access"])
        # message = {"Message":"Python Says Hello"}
        # return message
    
    return render_template("index.html")

def runApp():
    app.run(host='192.168.225.92')

if __name__ == "__main__":
    runApp()
