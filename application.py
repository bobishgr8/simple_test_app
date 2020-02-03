from flask import Flask,render_template,request,redirect
import matplotlib.pyplot as plt
import numpy as np
import os


def generate_sin_plot(amplitude=1,frequency=1):
    x = np.arange(0,4*np.pi,0.1)   
    plt.plot(x,amplitude*np.sin(frequency*x))
    plt.savefig("static/Images/graph.png",bbox="tight",pad_inches=2)
    plt.clf()

def input_sanitisation(amp,freq):
    if amp.isnumeric() and freq.isnumeric():
        return float(amp),float(freq)
    else:
        return TypeError

app = Flask("__name__")

@app.route("/")
def landing():
    try:
        
        os.remove("static/Images/graph.png")
    except:
        print("there is no such file existing")
        return render_template("landing.html")
    else:
        return render_template("landing.html")


@app.route("/plot", methods=["POST"])
def plot_graph():
    try:
        amp,freq = input_sanitisation(request.form["Amplitude"],request.form["Frequency"])
    except:
        return "<h1> Input is invalid </h1>"
    else:
        generate_sin_plot(amp,freq)
        return render_template("graph.html")

if __name__ == "__main__":
    app.run()

