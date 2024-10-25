import tkinter as tk

def switch_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

#окно игры
window = tk.Tk()
window.title("tic-tac-toe")

#игровое поле (пустая сетка)
cell_size = 100
cell_otst = 5
board = tk.Canvas(window, width=300, height=300)
board.pack()

# Создание пустой сетки
for row in range(3):
    for col in range(3):
        x1 = col * cell_size + cell_otst 
        y1 = row * cell_size + cell_otst 
        x2 = x1 + cell_size - cell_otst 
        y2 = y1 + cell_size - cell_otst 
        board.create_rectangle(x1, y1, x2, y2)

window.mainloop()
