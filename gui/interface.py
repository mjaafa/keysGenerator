from tkinter import *
import ttkbootstrap as ttk
from tkinter import filedialog  # Separate import for filedialog
from sslGenerator.sslGenerator import SSLGenerator

class myApp:
    def __init__(self, parent):
        parent.title("Keys Generator")
        parent.geometry("700x500")
        parent.maxsize(1000, 800)
        self.myParent = parent

        # Buttons
        self.button1 = ttk.Button(parent, text="Generate Keys", command=self.generate_keys)
        self.button1.pack(side=LEFT, padx=5, pady=10)

        self.button2 = ttk.Button(parent, text="save", command=self.button2Click)
        self.button2.pack(side=LEFT, padx=5, pady=10)

        # Flood Gauge (Progressbar)
        self.flood_gauge = ttk.Progressbar(parent, orient="horizontal", length=400, mode="determinate")
        self.flood_gauge.pack(pady=10)

        # Entry
        self.bits = StringVar()
        self.bits.set("2048")
        self.input = Entry(parent, textvariable=self.bits, width=30)
        self.input.pack()

        # SSL Generator
        self.sslGen = SSLGenerator()

# LabelFrames for displaying keys
        self.l2 = LabelFrame(parent, text="Private Key", padx=20, pady=20)
        self.l2.pack(side=LEFT, fill="both", expand="yes")

        self.l = LabelFrame(parent, text="Public Key", padx=20, pady=20)
        self.l.pack(side=LEFT, fill="both", expand="yes")

        # Text widgets for displaying keys
        self.private_text = Text(self.l2, wrap=WORD, height=50, width=100)
        self.private_text.pack()

        self.public_text = Text(self.l, wrap=WORD, height=50, width=100)
        self.public_text.pack()

    def setFloodLevel(self, level):
        self.flood_gauge["value"] = level

    def generate_keys(self):
        bits = int(self.bits.get())
        private_key, public_key = self.sslGen.generate(bits)

        # Refresh Private Key
        self.private_text.delete(1.0, END)
        self.private_text.insert(END, private_key.decode())

        # Refresh Public Key
        self.public_text.delete(1.0, END)
        self.public_text.insert(END, public_key.decode())

        # Save keys to files with default names
        #self.save_to_file(private_key, "private_key.pem")
        #self.save_to_file(public_key, "public_key.pem")

    def save_to_file(self, content, default_filename):
        file_path = filedialog.asksaveasfilename(defaultextension=".pem", initialfile=default_filename)
        if file_path:
            with open(file_path, "wb") as file:
                file.write(content)

    def button2Click(self):
        # Call save_to_file when "Cancel" button is clicked
        private_key_content = self.private_text.get(1.0, END)
        public_key_content = self.public_text.get(1.0, END)

        # Save keys to files with default names
        self.save_to_file(private_key_content.encode(), "private_key.pem")
        self.save_to_file(public_key_content.encode(), "public_key.pem")

        #self.myParent.destroy()

if __name__ == "__main__":
    root = Tk()
    app = myApp(root)
    root.mainloop()
