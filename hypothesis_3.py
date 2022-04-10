import pandas as pd

df = pd.read_csv("investments_VC.csv")  # створюємо DataFrame на основі файлу з даними

df.fillna(-1, inplace=True)  # замінюємо всі пусті значення на -1


def hypot_3():  # знаходимо категорії найуспішніших стартапів
    category = df[df["status"] == "acquired"]["market"].value_counts().index[0:3]
    print(f"Гіпотеза 3:\nНайбільше успішних стартапів пов'язано зі спортом\n"
          f"ВИСНОВОК: Ні.\n"
          f"Найбільше успішних стартапів в категоріях {category[0]}, {category[1]}, {category[2]}\n")
    
    df[df["status"] == "acquired"]["market"].value_counts().head(3).plot(kind = 'pie')  # створення кругової діаграми
    plt.show()
