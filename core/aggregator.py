class Aggregator:
    @staticmethod
    def apply(data, operation):
        if '=' not in operation:
            raise ValueError("Неверный формат агрегации")

        column, func = operation.split('=')
        column, func = column.strip(), func.strip().lower()

        try:
            values = [float(row[column]) for row in data]
        except ValueError:
            raise ValueError("Агрегация возможна только по числовым значениям")

        if func == 'avg':
            result = sum(values) / len(values)
        elif func == 'min':
            result = min(values)
        elif func == 'max':
            result = max(values)
        else:
            raise ValueError(f"Аггрегация '{func}' не поддерживается")

        return {f"{func}({column})": round(result, 2)}
