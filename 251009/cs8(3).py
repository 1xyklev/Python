import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def plot_graph():
    x = float(x_entry.get())
    y = float(y_entry.get())
    x_data.append(x)
    y_data.append(y)
    ax.clear()
    ax.plot(x_data, y_data, marker='o', linestyle='-')
    canvas.draw()  # 그래프 업데이트

# 애플리케이션 초기 설정
root = tk.Tk()
root.title("Dynamic Line Graph")

x_data = []
y_data = []

x_label = tk.Label(root, text="Enter x coordinate:")
x_label.pack()
x_entry = tk.Entry(root)  # ✅ 수정
x_entry.pack()

y_label = tk.Label(root, text="Enter y coordinate:")
y_label.pack()
y_entry = tk.Entry(root)  # ✅ 수정
y_entry.pack()

play_button = tk.Button(root, text="Plot", command=plot_graph)
play_button.pack()

fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(111)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

root.mainloop()