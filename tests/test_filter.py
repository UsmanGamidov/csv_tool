from core.processor import CSVProcessor
from core.filter import Filter

def test_filter_numeric_gt():
    processor = CSVProcessor("tests/test_data.csv")
    result = Filter.apply(processor.data, "price>500")
    assert len(result) == 2
    assert all(float(row["price"]) > 500 for row in result)

def test_filter_text_eq():
    processor = CSVProcessor("tests/test_data.csv")
    result = Filter.apply(processor.data, "brand=xiaomi")
    assert len(result) == 2
    assert all(row["brand"] == "xiaomi" for row in result)
