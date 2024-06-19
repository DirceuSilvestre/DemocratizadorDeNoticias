import re
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk, ImageDraw

def is_valid_url(url):
    regex = re.compile(
        r'^(http|https)://' 
        r'(([A-Za-z0-9.-]+)' 
        r'(\.[A-Z|a-z]{2,})+)' 
    )
    return re.match(regex, url) is not None

def process_url():
    url = url_entry.get()
    if not is_valid_url(url):
        messagebox.showerror("Erro", "URL inválida. Por favor, insira uma URL válida.")
        return
    
    options = Options()
    options.headless = False 
    
    driver = webdriver.Firefox(options=options)
    
    try:
        driver.get(url)
        time.sleep(5)
        
        body_tag = driver.find_element(By.TAG_NAME, 'body')
        html_tag = driver.find_element(By.TAG_NAME, 'html')
        driver.execute_script("arguments[0].setAttribute('class', '')", body_tag)
        driver.execute_script("arguments[0].style.overflow = 'auto'", body_tag)
        driver.execute_script("arguments[0].style.overflow = 'auto'", html_tag)
        
        parent_divs = driver.find_elements(By.XPATH, '/html/body/div')
        for div in parent_divs:
            style = div.get_attribute('style')
            if style:
                new_style = re.sub(r'overflow\s*:\s*hidden\s*;', 'overflow: auto;', style, flags=re.IGNORECASE)
                new_style = re.sub(r'display\s*:\s*[^;]+;', 'display: none;', new_style, flags=re.IGNORECASE)
                driver.execute_script("arguments[0].setAttribute('style', arguments[1])", div, new_style)
            
            styles = div.find_elements(By.CSS_SELECTOR, 'style')
            for style_tag in styles:
                style_content = style_tag.get_attribute('innerHTML')
                new_style_content = re.sub(r'overflow\s*:\s*hidden\s*;', 'overflow: auto;', style_content, flags=re.IGNORECASE)
                new_style_content = re.sub(r'display\s*:\s*[^;]+;', 'display: none;', new_style_content, flags=re.IGNORECASE)
                driver.execute_script("arguments[0].innerHTML = arguments[1]", style_tag, new_style_content)
    
    except Exception as e:
        messagebox.showerror("Erro", f"Falha ao processar a página: {e}")
    finally:
        inteiro = 1

def create_rounded_rectangle(width, height, radius, color):
    image = Image.new('RGB', (width, height), color)
    draw = ImageDraw.Draw(image)
    draw.rounded_rectangle([(0, 0), (width, height)], radius, fill=color)
    return ImageTk.PhotoImage(image)

root = tk.Tk()
root.title("Democratizador de Informações")
root.geometry("400x300")
root.configure(bg="#FF6F61")

style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 15), background="#FF6F61", foreground="white")
style.configure("TButton", font=("Helvetica", 15), padding=10)
style.map("TButton",
    background=[('active', '#E94E3D')],
    foreground=[('active', 'white')])

frame = tk.Frame(root, bg="#FF6F61", bd=2)
frame.pack(expand=True)

bg_image = create_rounded_rectangle(450, 450, 50, "#FF6F61")
bg_label = tk.Label(frame, image=bg_image, bd=0)
bg_label.place(x=25, y=25)

title_label = ttk.Label(frame, text="Democratizador de Informações", font=("Helvetica", 16, "bold"))
title_label.pack(pady=30)

url_label = ttk.Label(frame, text="Insira a URL do site:")
url_label.pack(pady=10)

url_entry = ttk.Entry(frame, width=50)
url_entry.pack(pady=5)

process_button = ttk.Button(frame, text="Processar", command=process_url)
process_button.pack(pady=20)

root.mainloop()
