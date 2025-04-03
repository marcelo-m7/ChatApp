def main(page: ft.Page):
    # ...
    ax.legend(title="Fruit color")
    chart1 = MatplotlibChart(fig, isolated=True, expand=True)
    page.add(chart1)
    sleep(5)
    ax.legend(title="Colors")
    chart1.update()

ft.app(main)

import matplotlib
import matplotlib.pyplot as plt
import flet as ft
from flet.matplotlib_chart import MatplotlibChart

matplotlib.use("svg")

def main(page: ft.Page):
    fig, ax = plt.subplots()
    fruits = ["apple", "blueberry", "cherry", "orange"]
    counts = [40, 100, 30, 55]
    bar_labels = ["red", "blue", "red", "orange"]
    bar_colors = ["tab:red", "tab:blue", "tab:red", "tab:orange"]
    ax.bar(fruits, counts, label=bar_labels, color=bar_colors)
    ax.set_ylabel("fruit supply")
    ax.set_title("Fruit supply by kind and color")
    ax.legend(title="Fruit color")
    page.add(MatplotlibChart(fig, expand=True))

ft.app(main)

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import flet as ft
from flet.matplotlib_chart import MatplotlibChart

matplotlib.use("svg")

def main(page: ft.Page):
    np.random.seed(19680801)
    dt = 0.01
    t = np.arange(0, 30, dt)
    nse1 = np.random.randn(len(t))
    nse2 = np.random.randn(len(t))
    s1 = np.sin(2 * np.pi * 10 * t) + nse1
    s2 = np.sin(2 * np.pi * 10 * t) + nse2
    fig, axs = plt.subplots(2, 1)
    axs[0].plot(t, s1, t, s2)
    axs[0].set_xlim(0, 2)
    axs[0].set_xlabel("time")
    axs[0].set_ylabel("s1 and s2")
    axs[0].grid(True)
    cxy, f = axs[1].cohere(s1, s2, 256, 1.0 / dt)
    axs[1].set_ylabel("coherence")
    fig.tight_layout()
    page.add(MatplotlibChart(fig, expand=True))

ft.app(main)

import matplotlib.pyplot as plt
import numpy as np
import flet as ft
from flet.matplotlib_chart import MatplotlibChart

matplotlib.use("svg")

def main(page: ft.Page):
    # Dados
    t = np.arange(0., 5., 0.2)
    y1 = np.power(t, 2)
    y2 = np.exp(t)

    # Criando subplots
    fig, (ax1, ax2) = plt.subplots(2, 1)
    ax1.plot(t, y1, 'b-')
    ax1.set_title("Gráfico de Linha - t^2")
    ax1.set_ylabel("y1")

    ax2.scatter(t, y2, color='r')
    ax2.set_title("Gráfico de Dispersão - e^t")
    ax2.set_xlabel("t")
    ax2.set_ylabel("y2")

    fig.tight_layout()

    # Adicionando ao Flet
    page.add(MatplotlibChart(fig, expand=True))

ft.app(main)

import matplotlib.pyplot as plt
import numpy as np
import flet as ft
from flet.matplotlib_chart import MatplotlibChart

matplotlib.use("svg")

def main(page: ft.Page):
    # Gerando dados
    data = np.random.normal(loc=0, scale=1, size=1000)
    
    # Criando a figura
    fig, ax = plt.subplots()
    ax.hist(data, bins=30, color='blue', alpha=0.7)
    ax.set_title("Histograma de Distribuição Normal")
    ax.set_xlabel("Valores")
    ax.set_ylabel("Frequência")

    # Adicionando ao Flet
    page.add(MatplotlibChart(fig, expand=True))

ft.app(main)

import matplotlib.pyplot as plt
import numpy as np
import flet as ft
from flet.matplotlib_chart import MatplotlibChart
import time

matplotlib.use("svg")

def main(page: ft.Page):
    # Dados
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    
    # Desenho inicial
    fig, ax = plt.subplots()
    line, = ax.plot(x, y)
    ax.set_title("Gráfico de Seno - Inicial")
    
    chart = MatplotlibChart(fig, expand=True)
    page.add(chart)
    
    # Espera antes de atualizar
    time.sleep(5)  # espera 5 segundos
    
    # Atualização do gráfico
    y_new = np.cos(x)
    line.set_ydata(y_new)
    ax.set_title("Gráfico de Cosseno - Atualizado")
    chart.update()

ft.app(main)
