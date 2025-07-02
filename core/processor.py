import csv

class CSVProcessor:
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = self._read_csv()

    def _read_csv(self):
        with open(self.filepath, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            return list(reader)
