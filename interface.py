from socket import *
from _thread import *
import customtkinter
import socket
from CRSA import RSA
from CGAMMAL import elgammal


customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
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
        self.alg_optionmenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["RSA", "DES", "ELGAMMAL", "AES"],
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
        self.scaling_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        #get devices button
        self.get_devices_button = customtkinter.CTkButton(self.sidebar_frame, fg_color="transparent", text="Get Devices!", border_width=2, text_color=("gray10", "#DCE4EE"), 
                                                     command=self.get_devices_event)
        self.get_devices_button.grid(row=7, column=0, padx=20, pady=(10, 10))


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
        start_new_thread(self.receive_messages_thread, ())

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.elgammal = elgammal(0,0)

        self.RSA = RSA()
        
        

# Connect to the server
        self.server_address = ('localhost', 5555)
        self.client_socket.connect(self.server_address)
        self.client_socket.send(str(self.RSA.e).encode())
        response = self.client_socket.recv(1024).decode()
        self.client_socket.send("Get_Keys".encode())
        response = self.client_socket.recv(1024).decode()
        keys = response.split('\n')
        for key in keys:
             print("Received key:", key)
 
 
 
        for i in keys:
            if i != self.RSA.e:
                self.RSA.e = int(i)
                break
        """
        we hopefully agree on a (q, a, kSmall) combo in server side and send to both sides then share public keys that can be generated after obtaining q, a, k
        """
        # self.client_socket.send("Get_q_a".encode())
        # response = self.client_socket.recv(1024).decode()
        # keys = response.split(',')
        # self.elgammal = elgammal(keys[0], keys[1])
        # self.elgammal.set_kSmall(keys[2])
        # self.client_socket.send(str(self.elgammal.publicKey).encode())



        """
        if this algo was receiveing then, it should already have (q, a, k) from server side and obtain public key from algo to send 
        """
        
        
        
        

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)  

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def send_button_event(self):
        message =self.entry.get()
        enc = RSA.encrypt(self.RSA,e=self.RSA.e,N=self.RSA.N,msg=message)
        #c1, c2 = self.elgammal.Encrypt(othergammalkey, message)

        """
        SEND C1, C2 ENCRYPTED TO OTHER GAMMAL

        """
        self.client_socket.send(enc.encode())
        self.textbox.insert("100.100","\n" + self.entry.get() + "\n" + enc)
        print("send_button click")
    def get_devices_event(self):
        self.client_socket.send("Get_Keys".encode())
        response = self.client_socket.recv(1024).decode()
        keys = response.split('\n')
        device_list = []
        
        for i, key in enumerate(keys):
            device_list.append(key)
        
        # Create a checklist with the retrieved devices
        self.device_selection_label = customtkinter.CTkLabel(self, text="Select a device:")
        self.device_selection_label.grid(row=4, column=1, columnspan=3, padx=(20, 0), pady=(0, 20), sticky="nsew")

        self.device_list = []

        for i, key in enumerate(device_list):
            device_button = customtkinter.CTkButton(self, text="device_"+str(i))
            device_button.grid(row=i+5, column=1, columnspan=2, padx=(20, 0), pady=(0, 10), sticky="nsew")
            self.device_list.append(device_button)

        self.selected_device_index = None

        # Add a submit button
        self.submit_button = customtkinter.CTkButton(master=self, fg_color="transparent", text="Submit", border_width=2,
                                                    text_color=("gray10", "#DCE4EE"), command=self.submit_devices_event)
        self.submit_button.grid(row=5+len(device_list), column=1, columnspan=2, padx=(20, 0), pady=(0, 20), sticky="nsew")


    def submit_devices_event(self):
        selected_device = self.device_selection.get_selected_items()
       
        print("Selected Device:", selected_device)

    
    def change_algorithm_event(self):
        print("changing algorithm")
    
    def receive_messages_thread(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode()
                # Call the function to handle the received message
                self.handle_received_message(message)
            except:
                break

    def handle_received_message(self, message):
        # This is where you can write the code to handle the received message
        print("Received message:", message)


if __name__ == "__main__":
    app = App()
    app.mainloop()