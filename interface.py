from socket import *
from _thread import *
import customtkinter
import socket
from CRSA import RSA


customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.RSA = RSA()
        

# Connect to the server
        self.server_address = ('localhost', 5555)
        self.client_socket.connect(self.server_address)
        self.client_socket.send(str(self.RSA.e).encode())
        # configure window
        self.title("Message Me")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=8, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(8, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Menus", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.alg_label = customtkinter.CTkLabel(self.sidebar_frame, text="Algorithm", anchor="w")
        self.alg_label.grid(row=1, column=0, padx=20, pady=(10, 0))
        self.alg_optionmenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["DES", "RSA", "ELGAMMAL", "AES"],
                                                          command=self.change_algorithm_event)
        self.alg_optionmenu.grid(row=2, column=0, padx=20, pady=(10, 10))

        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=3, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=4, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 20))

        # create main entry and button
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Send a message")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", text="Send!", border_width=2, text_color=("gray10", "#DCE4EE"), 
                                                     command=self.send_button_event)
        self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=800, height=400)
        self.textbox.grid(row=0, rowspan=3,column=1,columnspan=3,padx=(10, 10), pady=(10, 10), sticky="nsew")

      
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")
        # self.textbox.insert("0.0", "Hello world")



    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def send_button_event(self):
        message =self.entry.get()
        self.client_socket.send(message.encode())
        self.textbox.insert("100.100","\n" + self.entry.get())
        print("sidebar_button click")
    
    def change_algorithm_event(self):
        print("changing algorithm")


if __name__ == "__main__":
    app = App()
    app.mainloop()
