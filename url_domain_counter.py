import pandas as pd
from urllib.parse import urlparse
from collections import Counter
from tkinter import Tk, filedialog

# Tkinter kullanarak dosya seçme penceresi açma
root = Tk()
root.withdraw()  # Tkinter ana penceresini gizle
file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls")])

if file_path:
    # Excel dosyasını oku
    df = pd.read_excel(file_path)

    # C sütunundaki URL'leri al
    urls = df.iloc[:, 2]  # C sütunu üçüncü sütun olduğu için iloc[:, 2]

    # Alan adlarını çıkar
    domains = [urlparse(url).netloc for url in urls if isinstance(url, str)]

    # Alan adlarının kaç defa kullanıldığını say
    domain_counts = Counter(domains)

    # Sonuçları yeni bir DataFrame'e yaz
    result_df = pd.DataFrame(list(domain_counts.items()), columns=['Domain', 'Count'])

    # Sonuçları yeni bir Excel dosyasına yaz
    output_file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx *.xls")])
    if output_file_path:
        result_df.to_excel(output_file_path, index=False)
        print(f"Sonuçlar {output_file_path} dosyasına kaydedildi.")
    else:
        print("Çıktı dosyası seçilmedi.")
else:
    print("Dosya seçilmedi.")
