import tkinter as tk
import numpy as np


class GridApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Grid Configuration")

        # Create a 10x10 grid
        self.grid_size = 10
        self.grid_matrix = [[0] * self.grid_size for _ in range(self.grid_size)]

        # Create buttons for each cell in the grid
        self.buttons = [[tk.Button(root, width=10, height=5, command=lambda row=row, col=col: self.toggle_cell(row, col))
                         for col in range(self.grid_size)] for row in range(self.grid_size)]

        # Place buttons in the grid
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                self.buttons[row][col].grid(row=row, column=col)

        # Submit button to save the configuration
        self.submit_button = tk.Button(root, text="Submit", command=self.save_configuration)
        self.submit_button.grid(row=self.grid_size, columnspan=self.grid_size)

    def savee_configuration(self):
        # Save the grid_matrix to a text file
        with open("configuration.txt", "w") as file:
            for row in self.grid_matrix:
                file.write(" ".join(map(str, row)) + "\n")

        print("Configuration saved to configuration.txt")

    def load_configuration(self):
        try:
            # Load the grid_matrix from the text file
            with open("configuration.txt", "r") as file:
                self.grid_matrix = [list(map(int, line.split())) for line in file]

            print("Configuration loaded from configuration.txt")
        except FileNotFoundError:
            print("No previous configuration found. Starting with an empty grid.")
        for i in range(10):
            for j in range(10):
                if self.grid_matrix[i][j] == 1:
                    self.buttons[i][j].configure(bg="black")
    def toggle_cell(self, row, col):
        # Toggle the state of the cell (1 or 0)
        self.grid_matrix[row][col] = 1 - self.grid_matrix[row][col]

        # Change the button appearance based on the state
        if self.grid_matrix[row][col] == 1:
            self.buttons[row][col].configure(bg="black")
        else:
            self.buttons[row][col].configure(bg="white")

    def save_configuration(self):
        # Update the external matrix variable
        global matrix
        matrix = self.grid_matrix

        # Print the grid matrix
        print("Configuration:")
        for row in matrix:
            print(row)

if __name__ == "__main__":
    root = tk.Tk()
    app = GridApp(root)
    app.load_configuration()  # Load configuration at the start
    root.mainloop()
    app.savee_configuration()

    # Save configuration after each use

# Access the matrix outside the class
print("Accessing matrix outside the class:")
for row in matrix:
    print(row)

chances = [[0] * 10 for _ in range(10)]
ships = [1, 0, 1, 1]

for k in range(ships[0]):
    for i in range(10):
        for j in range(9):
            if matrix[i][j] == 0 and matrix[i][j+1] == 0:
                chances[i][j] += 1
                chances[i][j + 1] += 1

    for i in range(10):
        for j in range(9):
            if matrix[j][i] == 0 and matrix[j+1][i] == 0:
                chances[j][i] += 1
                chances[j+1][i] += 1

for k in range(ships[1]):
    for i in range(10):
        for j in range(8):
            if matrix[i][j] == 0 and matrix[i][j+1] == 0 and matrix[i][j+2] == 0:
                chances[i][j] += 1
                chances[i][j + 1] += 1
                chances[i][j + 2] += 1

    for i in range(10):
        for j in range(8):
            if matrix[j][i] == 0 and matrix[j+1][i] == 0 and matrix[j+2][i] == 0:
                chances[j][i] += 1
                chances[j+1][i] += 1
                chances[j+2][i] += 1

for k in range(ships[2]):
    for i in range(10):
        for j in range(7):
            if matrix[i][j] == 0 and matrix[i][j+1] == 0 and matrix[i][j+2] == 0 and matrix[i][j+3] == 0:
                chances[i][j] += 1
                chances[i][j + 1] += 1
                chances[i][j + 2] += 1
                chances[i][j + 3] += 1

    for i in range(10):
        for j in range(7):
            if matrix[j][i] == 0 and matrix[j+1][i] == 0 and matrix[j+2][i] == 0 and matrix[j+3][i] == 0:
                chances[j][i] += 1
                chances[j+1][i] += 1
                chances[j+2][i] += 1
                chances[j+3][i] += 1

for k in range(ships[3]):
    for i in range(10):
        for j in range(6):
            if matrix[i][j] == 0 and matrix[i][j+1] == 0 and matrix[i][j+2] == 0 and matrix[i][j+3] == 0 and matrix[i][j+4] == 0:
                chances[i][j] += 1
                chances[i][j + 1] += 1
                chances[i][j + 2] += 1
                chances[i][j + 3] += 1
                chances[i][j + 4] += 1

    for i in range(10):
        for j in range(6):
            if matrix[j][i] == 0 and matrix[j+1][i] == 0 and matrix[j+2][i] == 0 and matrix[j+3][i] == 0 and matrix[j+4][i] == 0:
                chances[j][i] += 1
                chances[j+1][i] += 1
                chances[j+2][i] += 1
                chances[j+3][i] += 1
                chances[j+4][i] += 1
print()
for row in chances:
    print(row)

best3 = [(0,0),(0,1),(0,2)]

for i in range(10):
    for j in range(10):
        if chances[i][j] > chances[best3[0][0]][best3[0][1]]:
            best3[2]=best3[1]
            best3[1]=best3[0]
            best3[0]=(i,j)
        elif chances[i][j] > chances[best3[1][0]][best3[1][1]]:
            best3[2]=best3[1]
            best3[1]=(i,j)
        elif chances[i][j] > chances[best3[2][0]][best3[2][1]]:
            best3[2] = (i, j)
print("best3", best3)
data = chances

# Normalize the data to be in the range [0, 255]
max_value = max(map(max, data))
normalized_data = [[int(value / max_value * 255) for value in row] for row in data]

class HeatmapApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Heatmap")

        # Create a canvas
        self.canvas = tk.Canvas(root, width=len(data[0]) * 20, height=len(data) * 20)
        self.canvas.pack()

        # Draw the heatmap on the canvas
        for y, row in enumerate(normalized_data):
            for x, value in enumerate(row):
                color = "#{:02x}{:02x}{:02x}".format(value, 0, 255 - value)  # Gradient from white to red
                self.canvas.create_rectangle(x * 20, y * 20, (x + 1) * 20, (y + 1) * 20, fill=color, outline="")

if __name__ == "__main__":
    root = tk.Tk()
    app = HeatmapApp(root)
    root.mainloop()