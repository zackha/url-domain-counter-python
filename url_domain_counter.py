import pandas as pd
from urllib.parse import urlparse
from collections import Counter
from tkinter import Tk, filedialog

# Use Tkinter to open file dialog for selecting the input file
root = Tk()
root.withdraw()  # Hide Tkinter main window
file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls")])

if file_path:
    # Read the selected Excel file
    df = pd.read_excel(file_path)

    # Get the URLs from the third column (C column)
    urls = df.iloc[:, 2]  # C column is the third column, so iloc[:, 2]

    # Extract domains from the URLs
    domains = [urlparse(url).netloc for url in urls if isinstance(url, str)]

    # Count the occurrences of each domain
    domain_counts = Counter(domains)

    # Write the results to a new DataFrame
    result_df = pd.DataFrame(list(domain_counts.items()), columns=['Domain', 'Count'])

    # Use file dialog to save the output file
    output_file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx *.xls")])
    if output_file_path:
        result_df.to_excel(output_file_path, index=False)
        print(f"Results saved to {output_file_path}.")
    else:
        print("Output file not selected.")
else:
    print("Input file not selected.")
