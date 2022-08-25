from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re

def change_phone_format(row, phone_index):
    if 'доб' in row[phone_index]:
      pattern = "(\+7\s?|8\s?)\(?(\d{3})\)?\s?\D?(\d{3})\D?(\d{2})\D?(\d{2})\s?\(?(доб.)\s?(\d*)\)?"
      return (re.sub(pattern, r'+7(\2)\3-\4-\5 \6(\7)', row[phone_index]))
    else:
      pattern = r"(\+7\s?|8\s?)\(?(\d{3})\)?\s?\D?(\d{3})\D?(\d{2})\D?(\d{2})"
      return (re.sub(pattern, r'+7(\2)\3-\4-\5', row[phone_index]))

def contact_list_update(contacts_list):
  for i in range(len(contacts_list)):
    row = contacts_list[i]
    row[phone_index] = change_phone_format(row, phone_index)
    # print(row)
    text = ' '.join(row[lastname_index:surname_index + 1])
    names_list = text.split()
    # print(names_list)
    row[0] = names_list[0]
    row[1] = names_list[1]
    if len(names_list) > 2:
      row[2] = names_list[2]
  return contacts_list

def clear_dublacates(contacts_list):
  for i in contacts_list:
    for j in contacts_list:
      if i[0] == j[0] and i[1] == j[1] and i != j:
        if i[2] == '':
          i[2] = j[2]
        if i[3] == '':
          i[3] = j[3]
        if i[4] == '':
          i[4] = j[4]
        if i[5] == '':
          i[5] = j[5]
        if i[6] == '':
          i[6] = j[6]
  updated_cl = []
  for line in contacts_list:
    if line not in updated_cl:
      updated_cl.append(line)
  return updated_cl


if __name__ == "__main__":

  with open("phonebook_raw.csv", encoding='UTF-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
  # pprint(contacts_list)
  # TODO 1: выполните пункты 1-3 ДЗ
  phone_index = contacts_list[0].index('phone')
  surname_index = contacts_list[0].index('surname')
  firstname_index = contacts_list[0].index('firstname')
  lastname_index = contacts_list[0].index('lastname')

  contact_list_update(contacts_list)

  udated_contact_list = clear_dublacates(contacts_list)

  print(udated_contact_list)

  # TODO 2: сохраните получившиеся данные в другой файл
  # код для записи файла в формате CSV
  with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(udated_contact_list)