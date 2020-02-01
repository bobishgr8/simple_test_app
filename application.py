from flask import Flask,render_template,request,redirect
import matplotlib.pyplot as plt
import numpy as np
import os


def generate_sin_plot(amplitude,frequency):
    x = np.arange(0,4*np.pi,0.1)   
    plt.plot(x,amplitude*np.sin(frequency*x))
    plt.savefig("static/Images/graph.png",bbox="tight",pad_inches=2)
    plt.clf()


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
    amp = int(request.form["Amplitude"])
    freq = int(request.form["frequency"])
    generate_sin_plot(amp,freq)
    return render_template("graph.html")

if __name__ == "__main__":
    app.run()

