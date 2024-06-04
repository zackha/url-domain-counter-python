# URL Domain Counter

This Python script reads a column of URLs from an Excel file, extracts the domain names, counts their occurrences, and writes the results to a new Excel file.

## Prerequisites

- Python 3.x
- Pandas
- Openpyxl

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/url-domain-counter.git
   ```
2. Navigate to the project directory:
   ```sh
   cd url-domain-counter
   ```
3. Install the required Python packages:
   ```sh
   pip install pandas openpyxl
   ```

## Usage

1. Run the script:
   ```sh
   python url_domain_counter.py
   ```
2. Select the input Excel file containing the URLs.
3. Select the output location and file name to save the results.

## Code Explanation

- The script uses `tkinter` to open file dialogs for selecting the input and output files.
- It reads the URLs from the third column (C column) of the input Excel file.
- It extracts the domain names from the URLs using the `urllib.parse` module.
- It counts the occurrences of each domain using the `collections.Counter` class.
- It writes the results to a new Excel file using `pandas`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
