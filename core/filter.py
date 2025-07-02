class Filter:
    @staticmethod
    def apply(data, condition):
        ops = ['>=', '<=', '>', '<', '=']
        for op in ops:
            if op in condition:
                column, value = condition.split(op)
                column, value = column.strip(), value.strip()
                return [row for row in data if Filter._compare(row[column], value, op)]
        raise ValueError("Неверное условие фильтрации")

    @staticmethod
    def _compare(a, b, op):
        try:
            a_val = float(a)
            b_val = float(b)
        except ValueError:
            a_val = a
            b_val = b

        if op == '=':
            return a_val == b_val
        if op == '>':
            return a_val > b_val
        if op == '<':
            return a_val < b_val
        if op == '>=':
            return a_val >= b_val
        if op == '<=':
            return a_val <= b_val
