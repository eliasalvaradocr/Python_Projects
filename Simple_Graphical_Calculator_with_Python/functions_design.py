import tkinter as tk
import math

# Definición de colores y estilos
BLACK = "#000000"
WHITE = "#FFFFFF"
SMALL_FONT_STYLE = ("Arial", 16)
LARGE_FONT_STYLE = ("Arial", 40, "bold")
ORANGE = "#FFA07A"
GRAY = "#A9A9A9"
DIMGRAY = "#696969"

# Variables globales para manejar expresiones
total_expression = ""  # Expresión acumulada
current_expression = ""  # Expresión actual

# Función para actualizar las etiquetas de pantalla
def actualizacion_pantalla(total_label, current_label):
    total_label.config(text=total_expression)
    current_label.config(text=current_expression)

# Función para manejar la pulsación de botones
def on_button_click(button, total_label, current_label):
    global total_expression, current_expression

    if button.isdigit() or button == ".":
        # Añadir números o punto a la expresión actual
        current_expression += button
    elif button in ["+", "-", "\u00F7", "\u00D7"]:
        # Añadir operador a la expresión total
        if current_expression:
            total_expression += current_expression + button
            current_expression = ""
    elif button == "=":
        # Calcular el resultado
        total_expression += current_expression
        try:
            current_expression = str(eval(total_expression.replace("\u00F7", "/").replace("\u00D7", "*")))
        except Exception:
            current_expression = "Error"
        total_expression = ""
    elif button == "C":
        # Limpiar la pantalla
        total_expression = ""
        current_expression = ""
    elif button == chr(9003):  # Retroceso
        current_expression = current_expression[:-1]
    elif button == "√":
        # Calcular la raíz cuadrada
        try:
            current_expression = str(math.sqrt(float(current_expression)))
        except ValueError:
            current_expression = "Error"
    actualizacion_pantalla(total_label, current_label)

# Función para crear la ventana principal
def create_window():
    global total_expression, current_expression

    # Configuración de la ventana principal
    window = tk.Tk()
    window.geometry("375x667")
    window.title("Calculadora")
    window.configure(bg=BLACK)

    # Crear el marco de la pantalla
    frame = tk.Frame(window, height=221, bg=BLACK)
    frame.pack(expand=True, fill="both")

    # Etiqueta para la expresión total
    total_label = tk.Label(
        frame,
        text=total_expression,
        anchor=tk.E,
        bg=BLACK,
        fg=WHITE,
        padx=24,
        font=SMALL_FONT_STYLE
    )
    total_label.pack(expand=True, fill="both")

    # Etiqueta para la expresión actual
    current_label = tk.Label(
        frame,
        text=current_expression,
        anchor=tk.E,
        bg=BLACK,
        fg=WHITE,
        padx=24,
        font=LARGE_FONT_STYLE
    )
    current_label.pack(expand=True, fill="both")

    # Crear el marco de botones
    button_frame = tk.Frame(window, bg=BLACK)
    button_frame.pack(expand=True, fill="both")

    # Botones de la calculadora
    buttons = [
        chr(9003), "C", "√", "\u00F7",  
        "7", "8", "9", "\u00D7",
        "4", "5", "6", "-",
        "1", "2", "3", "+",
        ".", "0", "New", "="
    ]

    # Colocar botones en la cuadrícula
    row, col = 0, 0
    for button in buttons:
        button_color = (
            GRAY if button in ['C', "√", chr(9003)] else
            ORANGE if button in ['\u00F7', '\u00D7', '-', '+', '='] else
            DIMGRAY
        )
        b = tk.Button(
            button_frame,
            text=button,
            bg=button_color,
            fg=WHITE,
            font=SMALL_FONT_STYLE,
            borderwidth=0,
            command=lambda x=button: on_button_click(x, total_label, current_label)
        )
        b.grid(row=row, column=col, sticky=tk.NSEW, padx=5, pady=5)
        col += 1
        if col > 3:
            col = 0
            row += 1

    # Configurar el peso de las filas y columnas
    for i in range(4):
        button_frame.columnconfigure(i, weight=1)
    for i in range(5):
        button_frame.rowconfigure(i, weight=1)

    return window
