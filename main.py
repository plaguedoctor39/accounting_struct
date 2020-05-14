from application.slry import calculate_salary
from application.db.people import get_employees
import datetime as dt
if __name__ == '__main__':
    current_date = dt.date
    print(current_date.today())
    get_employees()
    calculate_salary()