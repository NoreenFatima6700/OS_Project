# Disk Usage Analyzer
This project is a Disk Usage Analyzer tool developed using Python. It allows users to select a directory and analyze the disk usage of files within that directory, displaying the results in a scatter plot showing the size of the top 100 largest files.

## How to Run
Follow these step-by-step instructions to run the Disk Usage Analyzer:

1. **Clone the Repository**
    ```bash
    git clone https://github.com/NoreenFatima6700/OS_Project.git
    cd OS_Project
    ```

2. **Install Dependencies**
   
    Ensure you have Python installed. Then, install the required Python libraries using pip:
    ```bash
    pip install pandas matplotlib tkinter
    ```

4. **Run the Application**
   
    Execute the following command to run the Disk Usage Analyzer:
    ```bash
    python Disk_Usage_Analyzer.py
    ```

6. **Use the Application**
    - A GUI window will appear.
    - Click on the "Select Directory" button and choose the directory you want to analyze.
    - Click the "Analyze" button to start the disk usage analysis.
    - After the analysis is complete, click the "Show Analysis" button to view a scatter plot of the top 100 largest files in the selected directory.

## Project Structure
- `Disk_Usage_Analyzer.py`: The main script for the Disk Usage Analyzer application.

## Additional Notes
- Ensure you have the necessary permissions to read files in the directory you choose to analyze.
- The application currently shows the top 100 largest files for better performance and visualization.

