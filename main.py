import operator

class Main():

      def add(self):
            file = open('text.txt', 'a+', encoding='utf-8')
            size = file.readlines()
            if len(size) <= 2000:
                  tel = input("Введите номер телефона (4-х значный): ")
                  number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
                  for i in tel:
                        if i not in number:
                              print("Номер телефона введен некорректно. Телефон должен состоять только из цифр!!!")
                              break
                  if len(tel) != 4:
                        print("Номер телефона введен некорректно. Телефон должен состоять из 4-х цифр!!!")
                        # break
                  nomer = input("Введите номер помещения: ")
                  people = input("Введите фамилию сотрудника. Если сотрудников несколько, вводите фамилии через пробел: ")

                  file.write('\n')
                  file.write(tel)
                  file.write(' ')
                  file.write(nomer)
                  file.write(' ')
                  file.write(people)
                  file.close()
            else:
                  print("Невозможно добавить данные, так как в списке уже 2000 номеров")

      def update(self):
            file = open('text.txt', 'r', encoding='utf-8')
            arr = []
            while True:
                  line = file.readline()
                  if not line:
                        break
                  arr.append(line.split())
            file.close()

            vibor = input("Введите данные, которые хотите изменить (телефон = tel/ номер помещения = nom): ")
            if vibor == 'tel':
                  tel = input("Введите номер телефона, как он записан в справочнике: ")
                  new_tel = input("Введите номер нового телефона: ")
                  for i in range(len(arr)):
                        for j in range(len(arr[i])):
                              if arr[i][j] == tel:
                                    arr[i][j] = new_tel
                                    break
                  file = open('text.txt', 'w', encoding='utf-8')
                  file.write("")
                  file.close()
                  for i in range(len(arr)):
                        line = " ".join(arr[i])
                        file = open('text.txt', 'a+', encoding='utf-8')
                        file.write(line)
                        file.write('\n')

            if vibor == 'nom':
                  nom = input("Введите номер помещения, как он записан в справочнике: ")
                  new_nom = input("Введите новый номер помещения: ")
                  for i in range(len(arr)):
                        for j in range(len(arr[i])):
                              if arr[i][j] == nom:
                                    arr[i][j] = new_nom
                                    break
                  file = open('text.txt', 'w', encoding='utf-8')
                  file.write("")
                  file.close()
                  for i in range(len(arr)):
                        line = " ".join(arr[i])
                        file = open('text.txt', 'a+', encoding='utf-8')
                        file.write(line)
                        file.write('\n')

      def sort(self):
            file = open('text.txt', 'r', encoding='utf-8')
            arr = []
            while True:
                  line = file.readline()
                  if not line:
                        break
                  arr.append(line.split())
            file.close()
            new_arr = []
            for i in range(len(arr)):
                  for j in range(len(arr[i])):
                        if j == 1:
                              new_arr.append(int(arr[i][j]))
            res = merge_sort(new_arr)
            print(res)

            new_mas = []
            for i in range(len(arr)):
                  nomer = str(res[i])
                  for k in range(len(new_arr)):
                        if arr[k][1] == nomer:
                              new_mas.append(arr[k])

            file = open('text.txt', 'w', encoding='utf-8')
            file.write("")
            file.close()
            for i in range(len(new_mas)):
                  line = " ".join(new_mas[i])
                  file = open('text.txt', 'a+', encoding='utf-8')
                  file.write(line)
                  file.write('\n')


def merge_sort(L, compare=operator.lt):
    if len(L) < 2:
        return L[:]
    else:
        middle = int(len(L) / 2)
        left = merge_sort(L[:middle], compare)
        right = merge_sort(L[middle:], compare)
        return merge(left, right, compare)

def merge(left, right, compare):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


flag = True
while flag:
      print("---------------------------------------------------------------------------\n"
            "Выберите номер дейстивя, которое хотите совершить!\n"
            "1. Посмотреть текущий телефонный список.\n"
            "2. Добавить данные в телефонный справочник.\n"
            "3. Редактировать имеющиеся данные.\n"
            "4. Создать чистый справочник.\n"
            "5. Отсортировать данные справочника по номеру помещения.\n"
            "6. По номеру помещения найти номер телефона.\n"
            "0. Закончить работу с телефонным справочником.\n"
            "---------------------------------------------------------------------------")
      choice = int(input("Введите номер действия, которое хотите совершить: "))
      print("")

      main = Main()


      if choice == 0:
            flag = False
            break
      elif choice == 1:
            file = open('text.txt', 'r', encoding='utf-8')
            print(file.read())
            file.close()

      elif choice == 2:
            main.add()

      elif choice == 3:
            main.update()

      elif choice == 4:
            file = open('text.txt', 'w', encoding='utf-8')
            file.write("")
            file.close()
            print("Телефонный справочник пуст.")

      elif choice == 5:
            main.sort()
            print("Сортировка выполнена!!!")

      elif choice == 6:
            pom = input("Введите номер помещения: ")
            file = open('text.txt', 'r', encoding='utf-8')
            arr = []
            while True:
                  line = file.readline()
                  if not line:
                        break
                  arr.append(line.split())
            file.close()

            for i in range(len(arr)):
                        if arr[i][1] == pom:
                              telephon = arr[i][0]
            print("Вы искали номер телефона: ", telephon)

      else:
            print("Вы ввели несуществующий номер действия, попробуйте еще раз!")

      print("")


print("Вы закончили работу с файлом")

