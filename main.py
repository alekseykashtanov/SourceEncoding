from discrete_source import DiscreteSource

try:
	source = DiscreteSource(open("source_description.json", "r"))
	out_file = open("out.txt", "w")

	print("Выберите режим:")
	print("1 - Вычисление энтропии источника")
	print("2 - Создание равномерного кода с заданной скоростью, мощностью")
	print("		и вероятностью ошибки декодирования")

	usr_input = input()
	while(usr_input != '1' and usr_input != '2')
		usr_input = input()

	if usr_input == '1':
		print("Энтропия: ", source.entropy())
	else:
		print("Введите желаемую скорость кодирования: ", end='')
		R = float(input())
		print("Введите границу ошибки декодирования: ", end='')
		eps = float(input())
		print("Введите мощность алфавита кодера: ", end='')
		q = int(input())
		print("Мощность кодового алфавита: ", source.gen_encoding(R, eps, q, out_file))
except KeyError:
	print("Вероятности символов заданы неверно! Проверьте файл и попробоуйте еще раз")
	return -1
except IOError:
	print("File opening/writing error")
	return -1


