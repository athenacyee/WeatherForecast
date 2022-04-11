import numpy as np
from weather import *
from tkinter import *
from forecastWeather import *
from datetime import datetime, timedelta
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



root = Tk()
root.title("Weather")
root.geometry("700x750")
root.resizable(0,0)


def search():
    input_location(locationEntry.get())
    timeLabel.config(text=get_curenttime())
    locationLabel.config(text="Location: " + get_location())
    sunsetLabel.config(text="Sunset Time (local time): " + get_sunset())
    sunriseLabel.config(text="Sunrise Time(local time): " + get_sunrise())
    statusLabel.config(text="Status: " + get_status())
    tempLabel.config(text="Temperature: " + get_temp() + "°F")
    windLabel.config(text="Wind speed: " + get_windspeed() + "miles/hr")
    forecast_temp()
    plot()



def plot():
    plt = figure.add_subplot(1, 1, 1)
    x = []
    for i in range(0, 6):
        time = datetime.now() + timedelta(hours=i)
        f_time = time.strftime('%H:%M')
        x.append(f_time)

    y = np.array(forecast_temp())
    plt.plot(x, y, marker='*', linestyle="--")
    plt.set_title("Temperture for the next 5 hours")
    plt.set_xlabel("Time")
    plt.set_ylabel("Temperature(°F)")
    figure.canvas.draw()


inputLabel = Label(root, text="Enter a place to look for weather")
inputLabel.pack(pady=30)
locationEntry = Entry(root)
locationEntry.pack()
searchButton = Button(root, text='Search', command=search)
searchButton.pack()

timeLabel = Label(root, text=get_curenttime())
timeLabel.pack(pady=20)
locationLabel = Label(root)
locationLabel.pack()
sunsetLabel = Label(root)
sunsetLabel.pack()
sunriseLabel = Label(root)
sunriseLabel.pack()
statusLabel = Label(root)
statusLabel.pack()

tempLabel = Label(root)
tempLabel.pack()
windLabel = Label(root)
windLabel.pack()

figure = Figure(figsize=(6, 6), dpi=100)
canvas = FigureCanvasTkAgg(figure, root)
canvas.get_tk_widget().pack()



mainloop()