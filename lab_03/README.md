# Лабораторная работа 3. CI/CD для статического сайта

Файлы этой работы лежат не здесь, а в отдельном репозитории
[mptin/mptin.github.io](https://github.com/mptin/mptin.github.io).

Причина: по заданию нужно развернуть **тот же самый** сайт из ЛР 1 на двух
платформах, из одного локального репозитория с двумя удалёнными. Поэтому
конфигурации деплоя лежат внутри репозитория сайта.

## Четыре ссылки, которые сдаются по заданию

| Что | Ссылка |
|---|---|
| Сайт на GitHub Pages | [mptin.github.io](https://mptin.github.io) |
| Репозиторий на GitHub | [github.com/mptin/mptin.github.io](https://github.com/mptin/mptin.github.io) |
| Сайт на SourceCraft | [anthony-004.sourcecraft.site/portfolio](https://anthony-004.sourcecraft.site/portfolio) |
| Репозиторий на SourceCraft | [sourcecraft.dev/anthony-004/portfolio](https://sourcecraft.dev/anthony-004/portfolio) |

## Где что

| Что | Ссылка |
|---|---|
| Деплой на GitHub Pages | [.github/workflows/deploy-pages.yml](https://github.com/mptin/mptin.github.io/blob/main/.github/workflows/deploy-pages.yml) |
| Публикация в SourceCraft Sites | [.sourcecraft/sites.yaml](https://github.com/mptin/mptin.github.io/blob/main/.sourcecraft/sites.yaml) |
| Проверка сборки в SourceCraft CI | [.sourcecraft/ci.yaml](https://github.com/mptin/mptin.github.io/blob/main/.sourcecraft/ci.yaml) |
| Отчёт по работе | [mptin.github.io/LR-3](https://mptin.github.io/LR-3) |

## Два удалённых репозитория из одного локального

```bash
git remote add origin https://github.com/mptin/mptin.github.io.git
git remote add sourcecraft ssh://git@ssh.sourcecraft.dev/anthony-004/portfolio.git

git remote -v          # проверка: должны быть оба
git push origin main
git push sourcecraft main
```

## Настройки, которые включаются руками

На GitHub: Settings → Pages → Source переключить с `Deploy from a branch` на
`GitHub Actions`; репозиторий должен быть публичным.

На SourceCraft: публичная организация и публичный репозиторий, персональный
токен с правами Maintainer, включённый раздел Sites.

Подробнее — в [отчёте по работе](https://mptin.github.io/LR-3).
