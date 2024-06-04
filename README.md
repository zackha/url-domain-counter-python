# URL Domain Counter

This Python script reads an Excel file, extracts domain names from URLs in the specified column (C column), and counts how many times each domain appears. The results are then saved to a new Excel file.

## Prerequisites

- Python 3.x
- pandas
- openpyxl

## Installation

Install the required Python packages using pip:

```bash
pip install pandas openpyxl
```

## Usage

1. Clone the repository:

```bash
git clone https://github.com/zackha/url-domain-counter-python.git
cd url-domain-counter-python
```

2. Run the script:

```bash
python url_domain_counter.py
```

3. Follow the prompts to select an input Excel file and specify an output file for the results.

## How It Works

- The script opens a file dialog for you to select an Excel file.
- It reads URLs from the C column of the selected Excel file.
- It extracts the domain names from the URLs and counts the occurrences of each domain.
- It saves the results to a new Excel file, with domain names in the A column and their counts in the B column.

## Example

Input Excel file (C column):

```
https://example.com/page1
https://example.com/page2
https://anotherdomain.com/page1
https://example.com/page3
```

Output Excel file:

| Domain            | Count |
| ----------------- | ----- |
| example.com       | 3     |
| anotherdomain.com | 1     |

## License

This project is licensed under the MIT License.
