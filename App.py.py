#importing required packages
import base64
from flask import Flask, Response
from flask_restx import Api
import io
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

app = Flask(__name__)
api = Api(app)

def displayTable(fname):
    print(pd.read_csv(fname).head())

def exporting():
    plt.savefig("test.svg")

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/print-plot')
def plot_png():
    fig = create_figure()
    output = io.BytesIO()
    fig.savefig(output, format="png")
    # Embed the result in the html output.
    data = base64.b64encode(output.getbuffer()).decode("ascii")
    return f"<img src='data:image/png;base64,{data}'/>"

def create_figure():
    df = pd.read_csv("./dummydata.csv").reset_index()
    fig, ax = plt.subplots()

    ax.bar(df["index"], df["Judges"], color = "lightgreen")
    ax.bar(df["index"], df["Participants"], color = "darkgreen")
    print("Correct")

    return fig

create_figure()


if __name__ == '__main__':
    app.run()