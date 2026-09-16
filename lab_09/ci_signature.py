"""Дописывает в последнюю ячейку ноутбука отметку о том, где он выполнялся.

Скрипт запускается после `nbconvert --execute` и до сборки HTML, чтобы отметка
попала и в ноутбук, и в отчёт.

Задание требует доказать, что ячейки выполнил раннер SourceCraft, а не ноутбук
на моей машине и не Google Colaboratory. Одних переменных окружения для этого
мало: их несложно выставить руками локально, и тогда отметка начнёт врать.
Поэтому проверяются четыре независимых признака, и вывод "выполнено в CI"
делается, только если сходятся все четыре.

Запуск:
    python ci_signature.py [путь_к_ноутбуку]
"""

import json
import os
import platform
import sys
from datetime import datetime, timezone
from pathlib import Path

NOTEBOOK_PATH = sys.argv[1] if len(sys.argv) > 1 else "lab.ipynb"

# По этой строке находим и удаляем отметку от предыдущего запуска,
# чтобы при повторной сборке они не накапливались.
MARKER = "<!-- ci-signature -->"

# Префиксы переменных окружения, которые выставляет раннер.
CI_PREFIXES = (
    "CI_", "SOURCECRAFT_", "SC_", "PIPELINE_",
    "WORKFLOW_", "JOB_", "TASK_", "CUBE_", "BUILD_", "RUNNER_",
)


def collect_ci_variables() -> dict[str, str]:
    """Собрать переменные окружения, выставленные раннером.

    Returns:
        Словарь "имя переменной -> значение", отсортированный по имени.
        Значения длиннее 120 символов обрезаются.
    """
    found = {}
    for name, value in os.environ.items():
        if name.startswith(CI_PREFIXES):
            found[name] = value if len(value) <= 120 else value[:120] + "…"
    return dict(sorted(found.items()))


def looks_like_container() -> bool:
    """Проверить, выполняется ли код внутри контейнера.

    Docker оставляет в корне файл `/.dockerenv`, а у процесса с PID 1 в
    контрольных группах видны имена `docker`, `containerd` или `kubepods`.
    На обычной машине нет ни того, ни другого.

    Returns:
        True, если найден хотя бы один признак контейнера.
    """
    if Path("/.dockerenv").exists():
        return True

    try:
        cgroup = Path("/proc/1/cgroup").read_text(encoding="utf-8")
    except OSError:
        return False

    return any(name in cgroup for name in ("docker", "containerd", "kubepods"))


def collect_evidence() -> dict[str, tuple[bool, str]]:
    """Собрать признаки, по которым определяется место выполнения.

    Returns:
        Словарь "название проверки -> (сошлась ли, что найдено)".
    """
    ci_variables = collect_ci_variables()
    colab_tag = os.environ.get("COLAB_RELEASE_TAG")
    in_container = looks_like_container()

    return {
        "Переменные окружения раннера": (
            bool(ci_variables),
            f"найдено {len(ci_variables)} шт."
            if ci_variables else "не найдены",
        ),
        "Операционная система Linux": (
            platform.system() == "Linux",
            f"`{platform.platform()}`",
        ),
        "Запуск в контейнере": (
            in_container,
            "есть /.dockerenv или запись в /proc/1/cgroup" if in_container
            else "признаков контейнера нет",
        ),
        "Не Google Colab": (
            colab_tag is None and not os.path.isdir("/content"),
            f"COLAB_RELEASE_TAG = `{colab_tag}`" if colab_tag
            else "COLAB_RELEASE_TAG не задана, каталога /content нет",
        ),
    }


def build_signature() -> str:
    """Собрать текст отметки.

    Returns:
        Markdown с результатами проверок и сведениями о запуске.
    """
    evidence = collect_evidence()
    ci_variables = collect_ci_variables()

    if all(passed for passed, _ in evidence.values()):
        heading = "## Отметка о выполнении: раннер SourceCraft CI"
        statement = (
            "Сошлись все четыре проверки, так что ячейки выполнил раннер в "
            "контейнере. На моей машине и в Colab такой набор признаков не "
            "собирается: там нет ни контейнера, ни переменных раннера."
        )
    else:
        failed = [name for name, (passed, _) in evidence.items() if not passed]
        heading = "## Отметка о выполнении: локальный запуск"
        statement = (
            "Сошлись не все проверки (см. таблицу ниже), значит ноутбук "
            "выполнен вне CI и отметка здесь справочная. Не хватило: "
            + "; ".join(failed) + ". Настоящую отметку раннера надо "
            "смотреть в артефактах пайплайна."
        )

    now = datetime.now(timezone.utc).isoformat(timespec="seconds")

    lines = [
        MARKER,
        "",
        heading,
        "",
        statement,
        "",
        "### Проверки",
        "",
        "| Проверка | Сошлась | Что найдено |",
        "|---|---|---|",
    ]
    for name, (passed, detail) in evidence.items():
        lines.append(f"| {name} | {'да' if passed else 'нет'} | {detail} |")

    lines += [
        "",
        "### Окружение",
        "",
        "| Параметр | Значение |",
        "|---|---|",
        f"| Время выполнения (UTC) | `{now}` |",
        f"| Имя хоста | `{platform.node()}` |",
        f"| Python | `{platform.python_version()}` |",
        f"| Путь к интерпретатору | `{sys.executable}` |",
        f"| Рабочий каталог | `{os.getcwd()}` |",
    ]

    if ci_variables:
        lines += [
            "",
            "### Переменные окружения раннера",
            "",
            "| Переменная | Значение |",
            "|---|---|",
        ]
        lines += [
            f"| `{name}` | `{value}` |" for name, value in ci_variables.items()
        ]

    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """Дописать отметку в последнюю ячейку ноутбука."""
    with open(NOTEBOOK_PATH, encoding="utf-8") as file:
        notebook = json.load(file)

    cells = notebook["cells"]
    signature = build_signature()

    last_cell = cells[-1] if cells else None

    if last_cell is not None and last_cell["cell_type"] == "markdown":
        text = "".join(last_cell["source"])
        # Убираем отметку от предыдущего запуска, если она есть.
        if MARKER in text:
            text = text.split(MARKER)[0].rstrip()
        merged = text + "\n\n" + signature
        last_cell["source"] = merged.splitlines(keepends=True)
    else:
        cells.append({
            "cell_type": "markdown",
            "metadata": {},
            "source": signature.splitlines(keepends=True),
        })

    with open(NOTEBOOK_PATH, "w", encoding="utf-8") as file:
        json.dump(notebook, file, ensure_ascii=False, indent=1)

    print(f"Отметка о выполнении добавлена в {NOTEBOOK_PATH}")


if __name__ == "__main__":
    main()
