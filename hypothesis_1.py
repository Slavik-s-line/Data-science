import pandas as pd

df = pd.read_csv("investments_VC.csv")  # створюємо DataFrame на основі файлу з даними

df.fillna(-1, inplace=True)  # замінюємо всі пусті значення на -1

answer = {"more_100k_succes": 0,
          "more_100k_fail": 0,
          "less_100k_succes": 0,
          "less_100k_fail": 0}  # створюємо словник з даними про успішність стартапів та їх фінансування


def hypot_1():
    def make_usd(usd):  # функція для змінення значень в стовпчику "funding_total_usd"
        if str(usd) == " -   ":
            return 0
        else:
            return int(usd.replace(",", ""))

    df["funding_total_usd"] = df["funding_total_usd"].apply(make_usd)

    def debt_fin_succes(debt):  # функція для сортування успішних стартапів за фінансуванням
        global answer
        if debt < 100000:
            answer["less_100k_succes"] += 1
        elif debt >= 100000:
            answer["more_100k_succes"] += 1

    def debt_fin_fail(debt):  # функція для сортування невдалих стартапів за фінансуванням
        global answer
        if debt < 100000:
            answer["less_100k_fail"] += 1
        elif debt >= 100000:
            answer["more_100k_fail"] += 1

    # застосовуємо фільтрацію на успішність та викликаємо функції користувача
    df[df["status"] == "acquired"]["funding_total_usd"].apply(debt_fin_succes)
    df[df["status"] == "closed"]["funding_total_usd"].apply(debt_fin_fail)

    # обраховуємо умовірність успіху стартапів
    chance_more_100k_succes = round(answer["more_100k_succes"] /
                                    (answer["more_100k_succes"] + answer["more_100k_fail"]), 1)
    chance_less_100k_succes = round(answer["less_100k_succes"] /
                                    (answer["less_100k_succes"] + answer["less_100k_fail"]), 1)
    print(f"Гіпотеза 1:\nПри інвестуванні понад 100 тис. доларів США ймовірність успішності стартапу вище\n"
          f"ВИСНОВОК: так, це правда\n"
          f"Стартапи з фінансуванням більше 100,000$ стають успішними з умовірністю: {chance_more_100k_succes}\n"
          f"Стартапи з фінансуванням менше 100,000$ стають успішними з умовірністю: {chance_less_100k_succes}\n")
    
    s = pd.Series(data=[chance_more_100k_succes, chance_less_100k_succes],
                  index=[">100,000$", "<100,000$"])
    s.plot(kind = 'barh')  # створення стовпчатої діаграми
    plt.show()

