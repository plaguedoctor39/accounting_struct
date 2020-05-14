from application.db.people import *
from application.slry import *
import datetime as dt
if __name__ == '__main__':
    current_date = dt.date
    print(current_date.today())
    get_employees()
    calculate_salary()