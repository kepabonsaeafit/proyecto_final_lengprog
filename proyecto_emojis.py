import os
import re
import tkinter as tk

# Ruta de la carpeta que contiene los archivos de texto
ruta_carpeta = r"C:\Users\kepab\OneDrive\Documentos\dict_rae_txt\dics"

# Obtener la lista de archivos en la carpeta
lista_archivos = os.listdir(ruta_carpeta)

# Crear un conjunto con todas las palabras en español de los archivos de texto
palabras_espanol = set()

for archivo in lista_archivos:
    # Comprobar que el archivo es un archivo de texto
    if archivo.endswith(".txt"):
        # Crear la ruta completa del archivo
        ruta_archivo = os.path.join(ruta_carpeta, archivo)
        
        # Abrir el archivo y leer su contenido
        with open(ruta_archivo, "r", encoding="utf-8") as f:
            contenido = f.read()
            # Agregar todas las palabras del archivo al conjunto
            palabras_espanol.update(re.findall(r'\b\w+\b', contenido))

# Definición de la gramática BNF para emojis
emojis_bnf = r"(:\)|:\(|:D|;\)|:P|xD|:-\)|:-\(|\(y\)|\(n\)|<3|\\m/|:-O|:O|:-\||:\||:\*|>:\(|\^\^|:-\])"

# Función para analizar la cadena de entrada
def analizador_lexicografico(cadena):
    # Utilizar expresiones regulares para identificar emojis
    emojis = re.findall(emojis_bnf, cadena)
    
    # Dividir la cadena en palabras en español
    palabras = [palabra for palabra in cadena.split() if palabra.isalpha() and palabra.lower() in palabras_espanol]
    
    # Reemplazar los emojis en la cadena original con imágenes de alta definición
    cadena_con_emojis = re.sub(emojis_bnf, lambda x: f"🙂" if x.group() == ":)" else
                                                   f"😢" if x.group() == ":(" else
                                                   f"😄" if x.group() == ":D" else
                                                   f"😉" if x.group() == ";)" else
                                                   f"😛" if x.group() == ":P" else
                                                   f"😆" if x.group() == "xD" else
                                                   f"😃" if x.group() == ":-)" else
                                                   f"😭" if x.group() == ":-(" else
                                                   f"👍" if x.group() == "(y)" else
                                                   f"👎" if x.group() == "(n)" else
                                                   f"❤️" if x.group() == "<3" else
                                                   f"🤘" if x.group() == "\\m/" else
                                                   f"😲" if x.group() == ":-O" else
                                                   f"😲" if x.group() == ":O" else
                                                   f"😐" if x.group() == ":-|" else
                                                   f"😐" if x.group() == ":|" else
                                                   f"😘" if x.group() == ":*" else
                                                   f"😡" if x.group() == ">:(" else
                                                   f"😊" if x.group() == "^^" else
                                                   ":]" if x.group() == ":-]" else
                                                   f"😃", cadena)
    
    return cadena_con_emojis, len(palabras), len(emojis)

# Función para mostrar la salida en la interfaz gráfica
def mostrar_salida():
    entrada = entrada_text.get("1.0", "end-1c")
    resultado, palabras_en_espanol, emojis_identificados = analizador_lexicografico(entrada)
    salida_text.delete("1.0", "end")
    salida_text.insert("1.0", resultado)
    palabras_label.config(text=f"Palabras en español: {palabras_en_espanol}")
    emojis_label.config(text=f"Emoticones identificados: {emojis_identificados}")

# Crear la ventana de la interfaz gráfica
ventana = tk.Tk()
ventana.title("Analizador Lexicográfico de Emojis")

# Crear caja de texto para la entrada
entrada_text = tk.Text(ventana, height=10, width=40)
entrada_text.grid(row=0, column=0, padx=10, pady=10)

# Botón para analizar la entrada
analizar_button = tk.Button(ventana, text="Analizar", command=mostrar_salida)
analizar_button.grid(row=1, column=0, padx=10, pady=10)

# Caja de texto para la salida
salida_text = tk.Text(ventana, height=10, width=40)
salida_text.grid(row=2, column=0, padx=10, pady=10)

# Etiquetas para mostrar la cantidad de palabras en español y emojis identificados
palabras_label = tk.Label(ventana, text="")
palabras_label.grid(row=3, column=0, padx=10, pady=10)
emojis_label = tk.Label(ventana, text="")
emojis_label.grid(row=4, column=0, padx=10, pady=10)

ventana.mainloop()

