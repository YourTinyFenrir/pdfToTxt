import PyPDF2  # Для работы с ПДФ файлами
from sys import argv  # Для передачи параметров при запуске скрипта
import os  # Для работы с каталогами
import fnmatch  # Отбор файлов с определенным расширением (pdf)

script, arg1, arg2 = argv  # Параметры запуска

path = str(arg1)  # Путь до проверяемой папки
pageNum = int(arg2)  # Номер считываемой страницы

pattern = "*.pdf"
for root, dirs, files in os.walk(path):
    for filename in files:
        if fnmatch.fnmatch(filename, pattern):  # Отбираем файлы по паттерну (с расширением .pdf)

            pdfFileObj = open(path + "\\" + filename, 'rb')  # Создаем PDF объект
            shortFilename = filename[:-4]  # Оставляем только название, без расширения

            # Создаем файл с таким же названием, но расширением .txt
            txtFile = open(path + "\\" + shortFilename + ".txt", "w+", encoding="utf-8")

            # Считываем PDF объект
            pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

            # Если номер попадает в диапазон от 0 до числа страниц в документе, то читываем только заданную страницу
            if 0 < pageNum <= pdfReader.numPages:
                pageObj = pdfReader.getPage(pageNum-1)
                txtFile.writelines(pageObj.extractText())
            # Если пользователь ввел -1, считываем все страницы документа
            elif pageNum == -1:
                for num in range(0, pdfReader.numPages):
                    pageObj = pdfReader.getPage(num)
                    txtFile.writelines(pageObj.extractText())
            # Если вышли за диапазон, вывод соответствующее соообщение
            else:
                print(filename + " - Range out error")

            # Закрываем файлы
            txtFile.close()
            pdfFileObj.close()