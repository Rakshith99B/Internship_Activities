import tkinter as tk
from tkinter import scrolledtext
import random
import time
import threading

def start_simulation():
    name = name_entry.get()
    try:
        target = int(target_entry.get())
    except ValueError:
        output_area.insert(tk.END, "Please enter valid target distance!\n")
        return

    output_area.delete("1.0", tk.END)

    distance_travelled = []
    direction_taken = []
    distance = 0

    output_area.insert(tk.END, f"🤖 Robot Name: {name}\n")
    output_area.insert(tk.END, f"🎯 Target Distance: {target} meters\n\n")

    while distance < target:
        obstacle = random.choice(['y','n'])
        output_area.insert(tk.END, f"Obstacle? : {obstacle}\n")

        if obstacle == 'y':
            which_obstacle = random.choice(['h','e'])
            output_area.insert(tk.END, f"Obstacle Type (h/e): {which_obstacle}\n")

            if which_obstacle == "h":
                output_area.insert(tk.END, "👤 Human Detected... Waiting...\n")
                root.update()
                time.sleep(1)
                direction = random.choice(['Forward','Left','Right'])
                steps = 2
            else:
                direction = random.choice(['Forward','Left','Right'])
                output_area.insert(tk.END, f"⚠ Object detected. Moving {direction}\n")
                steps = 4
        else:
            direction = random.choice(['Forward','Left','Right'])
            output_area.insert(tk.END, f"✅ No Obstacle. Moving {direction}\n")
            steps = 6

        distance += steps
        distance_travelled.append(steps)
        direction_taken.append(direction)

        output_area.insert(tk.END, f"Distance Covered: {distance}\n\n")
        output_area.see(tk.END)
        root.update()
        time.sleep(1)

    output_area.insert(tk.END, f"🤖 Robot Name: {name}\n\n")
    output_area.insert(tk.END, f"🎯 Target Distance: {target}\n\n")
    output_area.insert(tk.END, "🎉 Target Reached!\n\n")
    output_area.insert(tk.END, f"Total Distance: {distance}\n")
    output_area.insert(tk.END, f"Steps Taker: {distance_travelled}\n")
    output_area.insert(tk.END, f"Directions: {direction_taken}\n")


# ------------------- UI DESIGN -------------------

root = tk.Tk()
root.title("RoboController 1.0")
root.geometry("600x600")
root.config(bg="#1e1e2f")   # Dark background

title_label = tk.Label(root, text="🤖 RoboController 1.0",
                       font=("Arial", 22, "bold"),
                       bg="#1e1e2f", fg="#00ffcc")
title_label.pack(pady=20)

frame = tk.Frame(root, bg="#2c2c3e")
frame.pack(pady=15, padx=25, fill="both", expand=True)

tk.Label(frame, text="Robot Name:",
         bg="#2c2c3e", fg="white",
         font=("Arial", 12)).pack(pady=5)

name_entry = tk.Entry(frame, font=("Arial", 12),
                      bg="#44475a", fg="white",
                      insertbackground="white")
name_entry.pack(pady=5)

tk.Label(frame, text="Target Distance (meters):",
         bg="#2c2c3e", fg="white",
         font=("Arial", 12)).pack(pady=5)

target_entry = tk.Entry(frame, font=("Arial", 12),
                        bg="#44475a", fg="white",
                        insertbackground="white")
target_entry.pack(pady=5)

start_button = tk.Button(frame, text="Start Simulation",
                         font=("Arial", 12, "bold"),
                         bg="#00cc99", fg="black",
                         activebackground="#00ffcc",
                         command=lambda: threading.Thread(target=start_simulation).start())
start_button.pack(pady=15)

output_area = scrolledtext.ScrolledText(frame,
                                        width=60, height=15,
                                        font=("Consolas", 10),
                                        bg="#111827",
                                        fg="#00ffcc")
output_area.pack(pady=10)

root.mainloop()
