from discrete_source import DiscreteSource

try:
	while True:
		in_file = open("source_description.json", "r")
		source = DiscreteSource(in_file)
		out_file = open("out.txt", "w")
		print("Выберите режим:")
		print("1 - Вычисление энтропии источника")
		print("2 - Создание равномерного кода с заданной скоростью, мощностью")
		print("		и вероятностью ошибки декодирования")

		usr_input = input()
		while usr_input != '1' and usr_input != '2':
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
			source.gen_encoding(R, eps, q)
		in_file.close()
		out_file.close()
except KeyError:
	print("Вероятности символов заданы неверно! Проверьте файл и попробоуйте еще раз")
except IOError:
	print("File opening/writing error")


