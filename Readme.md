
# Пока только прототип
## Сейчас  пасрсит(но можно спарсить все что угодно):
- имя
- цену
- откуда отправляеться(просто было легко спарсить, поэтому это здесь)
- модели
- цвета
- фото(это просто ссылки, но если надо, то можно будет и скачать)\
---
## Не имеиться:
- норм комментариев(вроде исправил)
- норм архитектуры(есть шанс, что ее никогда не будет)
- норм название переменных
---
### для запуска нужно устоновить selenium(`pip install selenium`), запустить main и вставить url
### мб ещё надо будет устоновить геко драйве, но вроде я это пофиксил, но если нет, то скачать нужный файл от [сюда](https://github.com/mozilla/geckodriver/releases) и перенести в корневой католог(хотя он тут один :( )
### и вставить сюда вместо `"win_geckodriver.exe"` название файла
```python
elif sys.platform == "win32":
    geckodriver = os.getcwd() + os.sep + "win_geckodriver.exe"
```
### А ещё я не умею писать Readme :(