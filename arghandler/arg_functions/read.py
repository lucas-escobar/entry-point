import logging as log
import datetime as dt
import util


def select_mode(nargs):
    """Returns string representing read mode (relative or absolute).

    Relative mode: accepts single value that can be converted to int
    Absolute mode: accepts two values that are of the date format YYYY-MM-DD
    """
    if nargs > 2:
        raise ValueError("Number of arguments supplied to --read should not \
                         exceed 2")
    return 'absolute' if nargs == 2 else 'relative'


def handle_read(args):
    mode = select_mode(len(args))
    if mode == 'relative' and len(args) > 0:
        try:
            val = int(args[0])
        except ValueError as err:
            val = None
            log.error(err)
        if val is None:
            return
        dates = [dt.datetime.now()-dt.timedelta(days=v) for v in range(val)]
        dates_str = [d.strftime("%Y-%m-%d") for d in dates]
        content = util.get_file_content(dates_str)
        for c in content: print(c)
    else: # 'relative'
        # TODO
        print(args)
