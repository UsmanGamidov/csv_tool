from core.processor import CSVProcessor

def test_read_csv():
    processor = CSVProcessor("tests/test_data.csv")
    assert len(processor.data) == 4
    assert processor.data[0]["name"] == "iphone 15 pro"
