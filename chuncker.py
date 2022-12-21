def write_chunk(file_name, lines, header):
    """Сохраняет файл в виде csv файла 
        Args:
            file_name (str): Название файла
            fields (str): Поля csv файла
            lines (str): Вакансии через \n
    """
    print("Saving", file_name)
    with open('csv//vacancies_'+ file_name +'.csv', 'w', encoding="utf-8-sig") as f_out:
        f_out.write(header)
        f_out.writelines(lines)
        f_out.close()

def сsv_chuncker(file_name):
    dictionary = {}
    with open(file_name, 'r', encoding="utf-8-sig") as f:
        header = f.readline()
        for x in f:
            listLine = x.split(",")
            year = listLine[-1].split('-')[0]
            if (year in dictionary.keys()):
                dictionary[year].append(x)
            else:
                dictionary[year] = [x]

        for data in dictionary:
            write_chunk(data, dictionary[data], header)