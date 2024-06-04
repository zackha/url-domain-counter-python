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

````

### GitHub Repository Setup

1. Create a new repository on GitHub. Name it `url-domain-counter` or another appropriate name.
2. Clone the repository to your local machine:
   ```sh
   git clone https://github.com/yourusername/url-domain-counter.git
````

3. Navigate to the repository directory:
   ```sh
   cd url-domain-counter
   ```
4. Create the `url_domain_counter.py` script file and paste the Python code into it.
5. Create the `README.md` file and paste the README content into it.
6. (Optional) Create a `.gitignore` file to ignore unnecessary files:
   ```plaintext
   __pycache__/
   *.pyc
   *.pyo
   ```
7. Commit the changes and push to GitHub:
   ```sh
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

### Python Code File: `url_domain_counter.py`

Now, create the `url_domain_counter.py` file in the repository directory and paste the provided Python code into it. Your repository should now contain the following files:

- `url_domain_counter.py`
- `README.md`
- `.gitignore` (optional)

After following these steps, your repository will be ready to share on GitHub. If you have any other preferences or need further adjustments, please let me know!
