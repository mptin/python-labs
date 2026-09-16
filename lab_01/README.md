# Лабораторная работа 1. MkDocs и GitHub Pages

Файлы этой работы лежат не здесь, а в отдельном репозитории
[mptin/mptin.github.io](https://github.com/mptin/mptin.github.io).

Причина: ЛР 1 и ЛР 3 делают один и тот же репозиторий `mptin.github.io`.
ЛР 1 создаёт сайт, ЛР 3 настраивает его автоматический деплой. Держать копию
сайта ещё и здесь нельзя: это был бы второй, расходящийся с первым репозиторий.

## Где что

| Что | Ссылка |
|---|---|
| Опубликованный сайт | [mptin.github.io](https://mptin.github.io) |
| Отчёт по работе | [mptin.github.io/LR-1](https://mptin.github.io/LR-1) |
| Репозиторий сайта | [github.com/mptin/mptin.github.io](https://github.com/mptin/mptin.github.io) |
| Конфигурация MkDocs | [source/mkdocs.yml](https://github.com/mptin/mptin.github.io/blob/main/source/mkdocs.yml) |
| Исходники страниц | [source/docs/](https://github.com/mptin/mptin.github.io/tree/main/source/docs) |
| Собранный сайт | [docs/](https://github.com/mptin/mptin.github.io/tree/main/docs) |
| Обоснование выбора темы | [README репозитория сайта](https://github.com/mptin/mptin.github.io#почему-material) |

## Как собрать локально

```bash
git clone https://github.com/mptin/mptin.github.io.git
cd mptin.github.io
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

cd source
mkdocs serve                       # предпросмотр на http://127.0.0.1:8000
mkdocs build --strict -d ../docs   # сборка в /docs
```

## Публикация

По заданию ЛР 1 собранный каталог `docs/` коммитится вместе с исходниками, а в
настройках репозитория GitHub Pages включается на `/docs` ветки `main`.

В ЛР 3 этот же сайт переведён на автоматический деплой: источник в настройках
Pages переключён с ветки на `GitHub Actions`, сборку выполняет workflow
`.github/workflows/deploy-pages.yml`. Каталог `docs/` остаётся в репозитории —
из него публикуется сайт в SourceCraft Sites.

Подробности — в [отчёте по ЛР 1](https://mptin.github.io/LR-1) и
[отчёте по ЛР 3](https://mptin.github.io/LR-3).
