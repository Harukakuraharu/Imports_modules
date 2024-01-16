from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime
import matplotlib.pyplot as plt

value = {'54125': 'Moskow',
         '45967': 'Saint-Petersburg',
         '34545': 'Kazan',
         '32458': 'Ekaterinburg'
         }

def get_pic(value):
    plt.subplots(figsize=(4, 4)) 
    plt.pie(value.keys(), labels=value.values(), autopct='%1.1f', labeldistance=None)
    plt.axis('equal')
    plt.legend(loc='lower right', bbox_to_anchor=(0.25, -0.1), labels=value.values(), fontsize=7)
    plt.title("Рандомные цифры и рандомные города")
    plt.show()


if __name__ == '__main__':
    print(calculate_salary())
    print(get_employees())
    print(f"Сегодня {datetime.now().strftime('%d-%m-%Y')}")
    get_pic(value)
