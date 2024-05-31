import customtkinter as ctk
from tkinter import messagebox
import os
import subprocess
import ctypes
import sys

def restart_spooler_service():
    if not is_admin():
        elevate()

    try:
        messagebox.showinfo("Avisos - Podium TI", "Parando o serviço de spooler...")
        subprocess.run(['net', 'stop', 'spooler'], check=True, shell=True)
        messagebox.showinfo("Avisos - Podium TI", "Deletando arquivos de spool...")

        spool_path = os.path.join(os.environ['SystemRoot'], 'System32', 'spool', 'PRINTERS')
        for root, dirs, files in os.walk(spool_path):
            for file in files:
                if file.endswith(".SHD") or file.endswith(".SPL"):
                    os.remove(os.path.join(root, file))

        messagebox.showinfo("Avisos - Podium TI", "Iniciando o serviço de spooler...")
        subprocess.run(['net', 'start', 'spooler'], check=True, shell=True)
        messagebox.showinfo("Sucesso", "Serviço de spooler reiniciado com sucesso.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Erro", f"Erro ao reiniciar o serviço de spooler: {e}")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

def is_admin():
    try:
        return os.getuid() == 0
    except AttributeError:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0

def elevate():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit()

def main():
    ctk.set_appearance_mode("System") 
    ctk.set_default_color_theme("blue")  

    root = ctk.CTk()  
    root.title("Impressão | Podium TI")
    root.geometry("400x250")  
    root.configure(bg='grey')  

    restart_button = ctk.CTkButton(root, text="Reiniciar Serviço de Impressão", command=restart_spooler_service, font=('Helvetica', 12, 'bold'))
    restart_button.pack(pady=60)

    footer_label = ctk.CTkLabel(root, text="Desenvolvido pelo colaborador Isllan Toso", font=('Helvetica', 11, 'italic'), bg_color='green')
    footer_label.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
