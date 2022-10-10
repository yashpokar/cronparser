from .handlers import (
    Handler,
    MinutesHandler,
    HoursHandler,
    DayOfMonthsHandler,
    DayOfWeeksHandler,
    MonthsHandler,
    CommandsHandler
)

def parse(*args) -> str:
    if len(args) != 1 or len(args[0]) != 1:
        raise ValueError('Invalid arguments supplied')

    expression = args[0][0].split(' ')

    handler = Handler(
        MinutesHandler(
            HoursHandler(
                DayOfMonthsHandler(
                    MonthsHandler(
                        DayOfWeeksHandler(
                            CommandsHandler()
                        )
                    )
                )
            )
        )
    )
    output = handler.handle(expression)
    return output
