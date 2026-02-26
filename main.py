import customtkinter as ctk
from PIL import Image, ImageTk
import os
import sys

def create_app():
    global tk_icon
    
    def resource_path(relative_path):
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS2
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)
    
    # Set appearance and theme
    ctk.set_appearance_mode("System")  # Modes: "System" (default), "Dark", "Light"
    ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"
    
    def center_window(window, width, height):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        window.geometry(f"{width}x{height}+{x}+{y}")

    # Initialize main window
    root = ctk.CTk()
    root.iconbitmap("favicon.ico")
    center_window(root, 400, 300)
    icon_path = os.path.abspath("favicon.png")
    img = Image.open(icon_path)
    tk_icon = ImageTk.PhotoImage(img)
    
    root.iconphoto(True, tk_icon)
    root.title("FileOrganizer")
    root.resizable(width=False, height=False)
    
    

    # Configure grid to center widgets
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)
    
    def show_popup():
        popup = ctk.CTkToplevel(root)
        popup.iconbitmap("favicon.ico")
        center_window(popup, 300, 150)
        popup.title("Success")
        popup.attributes('-topmost', True)
        popup.resizable(width=False, height=False)
        popup.iconphoto(False, tk_icon)
        popup.iconbitmap("favicon.ico")

        popup_label = ctk.CTkLabel(popup, text="ⓘ Folder organized succesfully", font=("Arial", 14))
        popup_label.pack(pady=20)
        popup.iconbitmap("favicon.ico")

        close_button = ctk.CTkButton(popup, text="Close", command=popup.destroy)
        close_button.pack(pady=10)
        popup.after(300, lambda: popup.iconbitmap("favicon.ico"))

    # Load and display logo (place 'logo.png' in the same directory)
    try:
        img = Image.open("logo.png")
        logo_image = ctk.CTkImage(light_image=img, dark_image=img, size=(150, 150))
        logo_label = ctk.CTkLabel(master=root, image=logo_image, text="")
        logo_label.grid(row=0, column=0, pady=(20, 10))
    except Exception as e:
        print(f"Error loading logo: {e}")

    # Create a larger centered button
    def on_button_click():
        ogDir = os.getcwd()
        os.chdir(ctk.filedialog.askdirectory())
        for item in os.listdir():
            filename, extension = os.path.splitext(item)
            proposedDir = os.path.join(os.getcwd(), extension.replace(".", "").upper())
            
            if not os.path.isdir(item):
                
                if not os.path.exists(proposedDir):
                    os.makedirs(os.path.join(os.getcwd(), extension.replace(".", "").upper()))
                    
                os.rename(os.path.abspath(item), os.path.join(proposedDir, item))
        os.chdir(ogDir)
        show_popup()

    button = ctk.CTkButton(
        master=root,
        text="Organize Folder",
        command=on_button_click,
        font=("Product Sans", 14)
    )
    button.grid(row=1, column=0)

    # Start the GUI event loop
    root.mainloop()
    


if __name__ == "__main__":
    create_app()