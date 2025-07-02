from core.processor import CSVProcessor
from core.aggregator import Aggregator

def test_aggregate_avg():
    processor = CSVProcessor("tests/test_data.csv")
    result = Aggregator.apply(processor.data, "rating=avg")
    assert "avg(rating)" in result
    assert round(result["avg(rating)"], 2) == 4.67

def test_aggregate_min():
    processor = CSVProcessor("tests/test_data.csv")
    result = Aggregator.apply(processor.data, "price=min")
    assert result["min(price)"] == 199.0

def test_aggregate_max():
    processor = CSVProcessor("tests/test_data.csv")
    result = Aggregator.apply(processor.data, "price=max")
    assert result["max(price)"] == 1199.0
