from datetime import datetime


def get_days_from_today(date):
    try:
        date = datetime.strptime(date, '%Y-%m-%d').date()
        result = date - datetime.today().date()
        return result.days
    except ValueError:
        print(f'Data {date} does not match format %Y-%m-%d')


print(get_days_from_today('2025-10-09'))
