import tkinter as tk

chosen_button = "No button"

def button_click(button):
    button_label = button['text']
    print(f"You clicked on button: {button_label}")
    global chosen_button
    chosen_button = button_label

def get_chosen_button():
    return chosen_button