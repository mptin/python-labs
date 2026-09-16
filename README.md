# python-labs — лабораторные работы по дисциплине «Программирование на Python»

**Ашихмин Кирилл, группа P3124.**

Отчёты по всем работам собраны на сайте-портфолио: **<https://mptin.github.io>**

## Состав

| № | Тема | Код | Отчёт |
|---|---|---|---|
| 1 | Статический сайт на MkDocs, GitHub Pages | [mptin/mptin.github.io](https://github.com/mptin/mptin.github.io) | [LR-1](https://mptin.github.io/LR-1) |
| 2 | Основы NumPy: массивы и векторные операции | [lab_02](lab_02) | [LR-2](https://mptin.github.io/LR-2) |
| 3 | CI/CD для статического сайта в SourceCraft | [mptin/mptin.github.io](https://github.com/mptin/mptin.github.io) | [LR-3](https://mptin.github.io/LR-3) |
| 4 | Классификация, Scikit-Learn | [lab_04](lab_04) | [LR-4](https://mptin.github.io/LR-4) |
| 5 | Регрессия, Scikit-Learn | [lab_05](lab_05) | [LR-5](https://mptin.github.io/LR-5) |
| 6 | Очистка и трансформация данных, pandas | [lab_06](lab_06) | [LR-6](https://mptin.github.io/LR-6) |
| 7 | Анализ текста | [lab_07](lab_07) | [LR-7](https://mptin.github.io/LR-7) |
| 8 | Скрапинг и анализ текста | [lab_08](lab_08) | [LR-8](https://mptin.github.io/LR-8) |
| 9 | Графика, SourceCraft CI/CD, артефакты | [lab_09](lab_09) | [LR-9](https://mptin.github.io/LR-9) |
| 10 | ML-сервис предсказания одобрения ипотеки | [anthony-004/lr-10](https://sourcecraft.dev/anthony-004/lr-10) | [LR-10](https://mptin.github.io/LR-10) |

Три работы живут в собственных репозиториях, и это не разброс, а требование
заданий.

* **ЛР 1 и ЛР 3** делают один и тот же сайт-портфолио, он же `username.github.io`.
  Репозиторий обязан называться именно так, иначе GitHub Pages не отдаст сайт
  по нужному адресу. Здесь в папках `lab_01` и `lab_03` лежат только указатели.
* **ЛР 9** начинается с форка чужого репозитория на SourceCraft, поэтому она
  живёт [там](https://sourcecraft.dev/anthony-004/itmo-python-lab-template).
  В `lab_09` лежит её копия, чтобы работа была видна вместе с остальными.
* **ЛР 10** — командный проект с собственным CI на SourceCraft, отдельный
  [репозиторий](https://sourcecraft.dev/anthony-004/lr-10).

## Блокноты в Colab

Работы 4–8 сдаются ссылкой на блокнот с открытым доступом. Ссылки лежат в
отчётах на сайте; в этом репозитории — выгруженные копии `.ipynb` со всеми
выполненными ячейками и их выводом.

## Данные, которых здесь нет

Крупные датасеты (около 55 МБ) не коммитятся, их скачивает первая ячейка
соответствующего ноутбука: `training_data.csv` и `test_data.csv` для ЛР 4,
таблицы цен на жильё для ЛР 5, корпус твитов `positive.csv` / `negative.csv`
для ЛР 7. Список — в [.gitignore](.gitignore).

Датасеты поменьше лежат рядом с работой: Titanic в `lab_06/data/`,
`StudentsPerformance.csv` в `lab_09/data/`, оценки студентов в `lab_02/data/`.

## Как запустить

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate

# ЛР 2: тесты и графики
cd lab_02
pip install -r requirements.txt
python -m pytest test.py -v
python main.py

# Ноутбуки
pip install jupyter
jupyter notebook
```

## Про качество кода

Код ЛР 2 и ЛР 10 писался под требования DAST/DATS: тесты (`pytest`),
аннотации типов (PEP 484), докстринги (PEP 257), стиль (PEP 8, проверка
`flake8` без дополнительных аргументов, то есть с лимитом 79 символов).
