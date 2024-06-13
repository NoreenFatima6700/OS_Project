import os   # For reading file sizes & walking through directories
import pandas as pd     # Data Manipulation & Analysis
import matplotlib.pyplot as plt     # pyplot for creating plots and visualizations
import tkinter as tk    # For creating graphical user interfaces
from tkinter import ttk, filedialog, messagebox     # ttk for Tkinter Themed Widgets, filedialog for File Dialogs, and messagebox for Displaying Message Boxes

class DiskUsageAnalyzer:
    def __init__(self, master):
        self.master = master
        self.master.title("Disk Usage Analyzer")

        self.select_button = ttk.Button(master, text="Select Directory", command=self.select_directory)
        self.select_button.pack(pady=10)

        self.analyze_button = ttk.Button(master, text="Analyze", command=self.analyze, state=tk.DISABLED)
        self.analyze_button.pack(pady=10)

        self.plot_button = ttk.Button(master, text="Show Analysis", command=self.show_analysis, state=tk.DISABLED)
        self.plot_button.pack(pady=10)

        self.directory = ""
        self.data = pd.DataFrame(columns=["Path", "Size"])   # Analysis

    def select_directory(self):
        self.directory = filedialog.askdirectory()
        if self.directory:
            self.analyze_button.config(state=tk.NORMAL)

    def analyze(self):
        if self.directory:
            self.data = self.collect_data(self.directory)
            self.plot_button.config(state=tk.NORMAL)
            messagebox.showinfo("Analysis Complete", "Disk usage analysis complete!")

    def collect_data(self, path):
        file_sizes = []
        for root, dirs, files in os.walk(path):
            for name in files:
                try:
                    filepath = os.path.join(root, name)
                    size = os.path.getsize(filepath)
                    file_sizes.append({"Path": filepath, "Size": size})
                except FileNotFoundError:
                    continue
        return pd.DataFrame(file_sizes)

    def show_analysis(self):
        if not self.data.empty:
            # Sorting the DataFrame by Size in descending order
            self.data = self.data.sort_values(by="Size", ascending=False)
            
            # Filtering to show only the top 100 largest files
            top_files = self.data.head(100)
            
            plt.figure(figsize=(14, 8))  # Increase the figure size
            plt.scatter(top_files['Path'], top_files['Size'])
            plt.xticks(rotation=90, fontsize=8)  # Rotate labels and set font size
            plt.xlabel('File Path')
            plt.ylabel('Size (bytes)')
            plt.title('Disk Usage Analysis')
            plt.tight_layout()
            
            min_size = int(top_files['Size'].min())
            max_size = int(top_files['Size'].max())
            tick_interval = 200  # Adjust this interval as needed

            # Set y-axis ticks
            plt.yticks(range(min_size // tick_interval * tick_interval, max_size // tick_interval * tick_interval + tick_interval, tick_interval))

            plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = DiskUsageAnalyzer(root)
    root.mainloop()     # waits for user interaction and updates the GUI
