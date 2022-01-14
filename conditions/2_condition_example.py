import webbrowser  # импорт модуля webbrowser

website = input('Введите адрес сайта -> ')

if 'https://' in website:
    webbrowser.open(website)
    print('if')
elif 'www.' in website:
    website = 'https://' + website
    webbrowser.open(website)
    print('elif')
else:
    website = 'https://www.' + website
    webbrowser.open(website)
    print('else')

# in - есть ли последовательность в другой последовательности
