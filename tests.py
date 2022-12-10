from unittest import TestCase
from main import Salary, Vacancy

class SalaryTests(TestCase):
    def test_salary_type(self):
        self.assertEqual(type(Salary("100","2000", "true", "RUR")).__name__, "Salary")

    def test_salary_to(self):
        self.assertEqual(Salary("100", "2000", "true", "RUR").salary_to, 2000)

    def test_salary_from(self):
        self.assertEqual(Salary(100.0, "2000", "true", "RUR").salary_from, 100)

    def test_salary_currency(self):
        self.assertEqual(Salary(100.0, "2000", "true", "RUR").salary_currency, 'RUR')

    def test_salary_to_string_RUR(self):
        self.assertEqual(Salary("100", "2000", "true", "RUR").to_string(), '100 - 2 000 (Рубли) (Без вычета налогов)')

    def test_salary_to_string_EUR(self):
        self.assertEqual(Salary(100.0, 2000000000, "false", "EUR").to_string(), '100 - 2 000 000 000 (Евро) (С вычетом налогов)')

class VacancyTest(TestCase):
    def test_vacancy_skills_many(self):
        self.assertEqual(Vacancy("x", "y", 'z\nz\nx', "noExperience", "true", "x", Salary("100", "2000", "true", "RUR"), "x",
                    "2007-12-03T17:40:09+0300").key_skills, ['z', 'z', 'x'])

    def test_vacancy_description(self):
        self.assertEqual(Vacancy("x", "<br><b>x</b>yz</br>", 'z', "noExperience", "true", "x", Salary("100", "2000", "true", "RUR"), "x",
                    "2007-12-03T17:40:09+0300").description, 'xyz')

    def test_vacancy_skills_one(self):
        self.assertEqual(Vacancy("x", "<br><b>x</b>yz</br>", 'z', "noExperience", "true", "x", Salary("100", "2000", "true", "RUR"), "x",
                    "2007-12-03T17:40:09+0300").key_skills, ['z'])

    def test_vacancy_date_to_string(self):
        self.assertEqual(Vacancy("x", "<br><b>x</b>yz</br>", 'z', "noExperience", "true", "x", Salary("100", "2000", "true", "RUR"), "x",
                                 "2007-12-03T17:40:09+0300").date_to_string(), '03.12.2007')
    def test_vacancy_date_get_year(self):
        self.assertEqual(Vacancy("x", "<br><b>x</b>yz</br>", 'z', "noExperience", "true", "x", Salary("100", "2000", "true", "RUR"), "x",
                                 "2007-12-03T17:40:09+0300").date_get_year(), 2007)

    def test_vacancy_premium_to_string_yes(self):
        self.assertEqual(Vacancy("x", "<br><b>x</b>yz</br>", 'z', "noExperience", "true", "x", Salary("100", "2000", "true", "RUR"), "x",
                                 "2007-12-03T17:40:09+0300").premium_to_string(), 'Да')
    def test_vacancy_premium_to_string_no(self):
        self.assertEqual(Vacancy("x", "<br><b>x</b>yz</br>", 'z', "noExperience", "False", "x", Salary("100", "2000", "true", "RUR"), "x",
                                 "2007-12-03T17:40:09+0300").premium_to_string(), 'Нет')

    def test_vacancy_description_to_string_bigger_100(self):
        self.assertEqual(Vacancy("x", 'x'*1000, 'z', "noExperience", "true", "x", Salary("100", "2000", "true", "RUR"), "x",
                                 "2007-12-03T17:40:09+0300").description_to_string(),
                                'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx...')

    def test_vacancy_description_to_string_less_100(self):
        self.assertEqual(Vacancy("x", 'xxxx', 'z', "noExperience", "true", "x", Salary("100", "2000", "true", "RUR"), "x",
                                 "2007-12-03T17:40:09+0300").description_to_string(), 'xxxx')

    def test_vacancy_experience_to_string_noExperience(self):
        self.assertEqual(Vacancy("x", "<br><b>x</b>yz</br>", 'z', "noExperience", "true", "x", Salary("100", "2000", "true", "RUR"), "x",
                                 "2007-12-03T17:40:09+0300").experience_to_string(), 'Нет опыта')

    def test_vacancy_experience_to_string_between1And3(self):
        self.assertEqual(Vacancy("x", "<br><b>x</b>yz</br>", 'z', "between1And3", "true", "x", Salary("100", "2000", "true", "RUR"), "x",
                                 "2007-12-03T17:40:09+0300").experience_to_string(), 'От 1 года до 3 лет')


    def test_vacancy_experience_to_string_between3And6(self):
        self.assertEqual(Vacancy("x", "<br><b>x</b>yz</br>", 'z', "between3And6", "true", "x", Salary("100", "2000", "true", "RUR"), "x",
                                 "2007-12-03T17:40:09+0300").experience_to_string(), 'От 3 до 6 лет')

    def test_vacancy_experience_to_list(self):
        self.assertEqual(Vacancy("x", "<br><b>x</b>yz</br>", 'z', "between3And6", "true", "x", Salary("100", "2000", "true", "RUR"), "x",
                                 "2007-12-03T17:40:09+0300").to_list(),
        ['x', 'xyz', 'z', 'От 3 до 6 лет', 'Да', 'x', '100 - 2 000 (Рубли) (Без вычета налогов)', 'x', '03.12.2007'])