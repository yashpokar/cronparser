class _Handler(object):
    def __init__(self, next_=None):
        self.nxt = next_

    def handle(self, request, response):
        raise NotImplementedError('handle method is not implemented')

    def next(self, request, response):
        if self.nxt is None:
            return '\n'.join(response)
        return self.nxt.handle(request, response)

    def _build_response(self, items: list, delimiter: str=' ') -> str:
        return delimiter.join(map(str, items))

    def _parse_expression(self, expression: str, low: int, high: int) -> str:
        if expression == '*':
            return self._build_response(range(low, high + 1))

        if '-' in expression:
            range_ = expression.split('-')

            if len(range_) != 2:
                raise ValueError('Invalid arguments')

            start, end = range_

            if not start.isnumeric() or not end.isnumeric():
                raise ValueError('Invalid arguments')

            start = int(start)
            end = int(end)

            if start < low or end > high:
                raise ValueError('Invalid arguments')

            return self._build_response(start, end)

        if '/' in expression:
            first, second = expression.split('/')

            if first == '*':
                if not second.isnumeric():
                    raise ValueError('Invalid arguments')

                second = int(second)

                return self._build_response([item for item in range(low, high + 1) if item % second == 0])

            if not first.isnumeric() or not second.isnumeric():
                raise ValueError('Invalid arguments')

            first, second = int(first), int(second)
            return self._build_response([item for item in range(low, high) if item % second == 0])

        if ',' in expression:
            units = expression.split(',')

            for unit in units:
                if not unit.isnumeric():
                    raise ValueError('Invalid arguments')

            return self._build_response(units)
        return expression


class Handler(_Handler):
    def handle(self, request, response=[]):
        if len(request) != 6:
            raise ValueError('Invalid arguments')

        return self.next(request, response)


class MinutesHandler(_Handler):
    def handle(self, request, response):
        res = 'minute         '
        res += self._parse_expression(request[0], 0, 59)

        response.append(res)

        return self.next(request, response)


class HoursHandler(_Handler):
    def handle(self, request, response):
        hours = request[1]
        res = 'hour           '
        res += self._parse_expression(request[1], 0, 23)

        response.append(res)

        return self.next(request, response)


class DayOfMonthsHandler(_Handler):
    def handle(self, request, response):
        day_of_months = request[2]
        res = 'day of month   '
        res += self._parse_expression(request[2], 1, 31)

        return self.next(request, response)


class MonthsHandler(_Handler):
    def handle(self, request, response):
        months = request[3]
        res = 'month          '
        res += self._parse_expression(request[3], 1, 12)

        response.append(res)

        return self.next(request, response)


class DayOfWeeksHandler(_Handler):
    def handle(self, request, response):
        months = request[4]
        res = 'day of week    '
        res += self._parse_expression(request[2], 1, 7)

        response.append(res)

        return self.next(request, response)


class CommandsHandler(_Handler):
    def handle(self, request, response):
        months = request[5]
        res = 'command        '
        res += request[5]

        response.append(res)

        return self.next(request, response)
