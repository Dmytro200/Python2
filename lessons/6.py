print("Вас приветствует конвертер смайликов в смайлики")

emoji = [':)', 'XD', ':(', '>:(', '>:)']
convert_emoji = ['☺', '😂', '😢', '😠', '😈' ]



text = input("Введите текст для конвертации:")

print(str(text))

text = text.replace('>:(', '😠')
text = text.replace('>:)', '😈')
text = text.replace(':)', '☺')
text = text.replace('XD', '😂')
text = text.replace(':(', '😢')

print(text)