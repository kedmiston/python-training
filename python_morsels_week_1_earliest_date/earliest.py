
def get_earliest(newer, older):
    newer_revised = _get_revised_format(newer)
    older_revised = _get_revised_format(older)
    return older if newer_revised > older_revised else newer


def get_earliest_bonus(*args):
    earliest = None
    for date in args:
        earliest_revised = _get_revised_format(earliest)
        date_revised = _get_revised_format(date)
        if date_revised < earliest_revised or earliest_revised is None:
            earliest = date
    return earliest


def _get_revised_format(date):
    if date is None:
        return None

    split = date.split('/')
    return int('{}{}{}'.format(split[2].zfill(4), split[0].zfill(2), split[1].zfill(2)))


def treys_bonus_solution(*dates):
    """
    Trey's solution -- received on 4/4/2018
    """
    def date_key(date):
        (m, d, y) = date.split('/')
        return y, m, d
    return min(dates, key=date_key)

