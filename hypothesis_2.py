import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("investments_VC.csv")  # створюємо DataFrame на основі файлу з даними

df.fillna(-1, inplace=True)  # замінюємо всі пусті значення на -1


def hypot_2():  # знаходимо країну з найб к-тью успішних стартапів
    country = df[df["status"] == "acquired"]["country_code"].value_counts().index[0]
    print(f"Гіпотеза 2:\nНайбільше успішних стартапів в Китаї\n"
          f"ВИСНОВОК: Ні. Найбільше успішних стартапів в {country}\n")

    df[df["status"] == "acquired"]["country_code"].value_counts().head(5).plot(
        kind='pie')  # створення кругової діаграми
    plt.show()
