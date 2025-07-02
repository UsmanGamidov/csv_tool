import argparse
import sys
from tabulate import tabulate

from core.processor import CSVProcessor
from core.filter import Filter
from core.aggregator import Aggregator


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file")
    parser.add_argument("--where")
    parser.add_argument("--aggregate")

    args = parser.parse_args()

    try:
        processor = CSVProcessor(args.file)
    except Exception as e:
        print(f"Ошибка чтения файла: {e}")
        sys.exit(1)

    if args.where:
        try:
            filtered_data = Filter.apply(processor.data, args.where)
            print(tabulate(filtered_data, headers="keys"))
        except Exception as e:
            print(f"Ошибка фильтрации: {e}")
            sys.exit(1)

    elif args.aggregate:
        try:
            result = Aggregator.apply(processor.data, args.aggregate)
            print(tabulate([result.items()], headers=["Метрика", "Значение"]))
        except Exception as e:
            print(f"Ошибка агрегации: {e}")
            sys.exit(1)

    else:
        print(tabulate(processor.data, headers="keys"))


if __name__ == "__main__":
    main()
