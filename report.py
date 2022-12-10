def write_chunk(file_name, lines):
    """Сохраняет файл в виде csv файла 

        Args:
            file_name (str): Название файла
            fields (str): Поля csv файла
            lines (str): Вакансии через \n
    """
    print("Saving", file_name)
    with open('csv//vacancies_'+ file_name +'.csv', 'w', encoding="utf-8-sig") as f_out:
        f_out.writelines(lines)
        f_out.close()

def сsv_chuncker(file_name):
    csvs = {}
    with open(file_name, 'r', encoding="utf-8-sig") as File:
        names = File.readline()
        for string in File:
            year = string.split(",")[len(string.split(",")) - 1][0:4]
            if(year in csvs.keys()):
                csvs[year].append(string)
            else: 
                csvs[year] = list(names)

        if len(csvs) > 0:
            year = 2007
            for year in csvs:
                write_chunk(str(year), csvs[year])
                year += 1

file_name = input("Введите название файла: ")
сsv_chuncker(file_name)