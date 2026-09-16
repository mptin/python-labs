"""Лабораторная работа 2: основы NumPy — массивы и векторные операции.

Модуль содержит функции для создания массивов, векторных и матричных
операций, статистического анализа и визуализации данных.
"""

import os

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Рисуем графики сразу в файл, без открытия окна — чтобы работало и в тестах.
matplotlib.use("Agg")

PLOTS_DIR = "plots"


def _save_plot(filename: str) -> None:
    """Сохранить текущий график в папку plots и закрыть его.

    Args:
        filename: Имя файла, например "histogram.png".
    """
    os.makedirs(PLOTS_DIR, exist_ok=True)
    plt.savefig(os.path.join(PLOTS_DIR, filename))
    plt.close()


# 1. Создание и обработка массивов

def create_vector() -> np.ndarray:
    """Создать массив от 0 до 9.

    Returns:
        Массив чисел от 0 до 9 включительно.
    """
    return np.arange(10)


def create_matrix() -> np.ndarray:
    """Создать матрицу 5x5 со случайными числами из диапазона [0, 1).

    Returns:
        Матрица 5x5 со случайными значениями.
    """
    return np.random.rand(5, 5)


def reshape_vector(vec: np.ndarray) -> np.ndarray:
    """Преобразовать массив формы (10,) в форму (2, 5).

    Args:
        vec: Входной массив формы (10,).

    Returns:
        Тот же массив в форме (2, 5).
    """
    return vec.reshape(2, 5)


def transpose_matrix(mat: np.ndarray) -> np.ndarray:
    """Транспонировать матрицу (строки становятся столбцами).

    Args:
        mat: Входная матрица.

    Returns:
        Транспонированная матрица.
    """
    return mat.T


# 2. Векторные операции

def vector_add(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Сложить два вектора поэлементно (без циклов, векторизованно).

    Args:
        a: Первый вектор.
        b: Второй вектор той же длины.

    Returns:
        Результат поэлементного сложения.
    """
    return a + b


def scalar_multiply(vec: np.ndarray, scalar: float) -> np.ndarray:
    """Умножить вектор на число.

    Args:
        vec: Входной вектор.
        scalar: Число-множитель.

    Returns:
        Каждый элемент вектора, умноженный на scalar.
    """
    return vec * scalar


def elementwise_multiply(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Перемножить два массива поэлементно.

    Args:
        a: Первый массив.
        b: Второй массив такой же формы.

    Returns:
        Результат поэлементного умножения.
    """
    return a * b


def dot_product(a: np.ndarray, b: np.ndarray) -> float:
    """Вычислить скалярное произведение двух векторов.

    Args:
        a: Первый вектор.
        b: Второй вектор той же длины.

    Returns:
        Сумма попарных произведений элементов.
    """
    return np.dot(a, b)


# 3. Матричные операции

def matrix_multiply(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Перемножить две матрицы по правилу матричного умножения.

    Args:
        a: Первая матрица.
        b: Вторая матрица (число её строк равно числу столбцов a).

    Returns:
        Произведение матриц.
    """
    return a @ b


def matrix_determinant(a: np.ndarray) -> float:
    """Вычислить определитель квадратной матрицы.

    Args:
        a: Квадратная матрица.

    Returns:
        Определитель матрицы.
    """
    return np.linalg.det(a)


def matrix_inverse(a: np.ndarray) -> np.ndarray:
    """Вычислить обратную матрицу.

    Args:
        a: Квадратная невырожденная матрица.

    Returns:
        Обратная матрица: при умножении на исходную даёт единичную.
    """
    return np.linalg.inv(a)


def solve_linear_system(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Решить систему линейных уравнений A @ x = b.

    Args:
        a: Матрица коэффициентов A.
        b: Вектор свободных членов b.

    Returns:
        Вектор решения x.
    """
    return np.linalg.solve(a, b)


# 4. Статистический анализ

def load_dataset(path: str = "data/students_scores.csv") -> np.ndarray:
    """Загрузить CSV-файл и вернуть его содержимое как массив NumPy.

    Args:
        path: Путь к CSV-файлу.

    Returns:
        Данные таблицы (без заголовка) в виде двумерного массива.
    """
    return pd.read_csv(path).to_numpy()


def statistical_analysis(data: np.ndarray) -> dict[str, float]:
    """Посчитать основные статистические характеристики набора данных.

    Args:
        data: Одномерный массив данных (например, оценки по математике).

    Returns:
        Словарь с ключами: mean, median, std, min, max, p25, p75.
    """
    return {
        "mean": np.mean(data),
        "median": np.median(data),
        "std": np.std(data),
        "min": np.min(data),
        "max": np.max(data),
        "p25": np.percentile(data, 25),
        "p75": np.percentile(data, 75),
    }


def normalize_data(data: np.ndarray) -> np.ndarray:
    """Выполнить min-max нормализацию: привести значения к диапазону [0, 1].

    Формула: (x - min) / (max - min).

    Args:
        data: Входной массив данных.

    Returns:
        Нормализованный массив.
    """
    minimum = np.min(data)
    maximum = np.max(data)
    return (data - minimum) / (maximum - minimum)


# 5. Визуализация

def plot_histogram(data: np.ndarray) -> None:
    """Построить и сохранить гистограмму распределения оценок.

    Args:
        data: Данные для гистограммы.
    """
    plt.hist(data, bins=5, color="steelblue", edgecolor="black")
    plt.title("Распределение оценок по математике")
    plt.xlabel("Балл")
    plt.ylabel("Количество студентов")
    _save_plot("histogram.png")


def plot_heatmap(matrix: np.ndarray) -> None:
    """Построить и сохранить тепловую карту корреляции предметов.

    Args:
        matrix: Матрица корреляции.
    """
    sns.heatmap(matrix, annot=True, cmap="coolwarm")
    plt.title("Корреляция между предметами")
    _save_plot("heatmap.png")


def plot_line(x: np.ndarray, y: np.ndarray) -> None:
    """Построить и сохранить график зависимости "студент -> оценка".

    Args:
        x: Номера студентов.
        y: Оценки студентов.
    """
    plt.plot(x, y, marker="o")
    plt.title("Оценки студентов по математике")
    plt.xlabel("Номер студента")
    plt.ylabel("Балл")
    _save_plot("line.png")


def main() -> None:
    """Продемонстрировать работу функций на учебном наборе данных."""
    data = load_dataset()
    math_scores = data[:, 0]

    print("Статистика по математике:")
    for name, value in statistical_analysis(math_scores).items():
        print(f"  {name}: {value:.2f}")

    normalized = np.round(normalize_data(math_scores), 2)
    print("\nНормализованные оценки:", normalized)

    plot_histogram(math_scores)
    plot_heatmap(np.corrcoef(data.T))
    plot_line(np.arange(1, len(math_scores) + 1), math_scores)
    print(f"\nГрафики сохранены в папку {PLOTS_DIR}/")


if __name__ == "__main__":
    main()
