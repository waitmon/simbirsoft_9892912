## Общая информация

Тестовое задание на позицию "QA Automation инженер"

Тестовый сайт: https://www.globalsqa.com/angularJs-protractor/BankingProject/#/customer

## Предусловия

1) Скачать последнюю версию Selenium Server (Grid):  https://www.selenium.dev/downloads/ (больше подробностей по установке - https://www.selenium.dev/documentation/grid/getting_started/)

2) Склонировать репозиторий и перейти в него в командной строке:
```
git@github.com:waitmon/simbirsoft_9892912
```
```
cd simbirsoft_9892912
```
3) Создать виртуальное окружение

## Запуск тестов
1) Установить зависимости: 
 ```
 pip3 install -r requirements
 ```
2) В терминале перейти в директорию со скачанным selenium grid и запустить в режиме standalone следующей командной:

```
java -jar selenium-server-standalone-4.23.0.jar standalone
```

3) Последовательный запуск тестов (3 браузера по очереди, с генерацией отчётов):

```
pytest -sv --alluredir allure-report
```
4) Параллельный запуск тестов (3 браузера сразу, с генерацией отчётов)

```
pytest -s -v -n=3 --alluredir allure-report 
```

5) Просмотр сгенерированных allure-отчётов:

```
allure serve allure-report
```
