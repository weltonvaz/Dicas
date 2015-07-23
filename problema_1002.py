def area_do_circulo(raio):
	PI = 3.14159
	area = PI * (raio ** 2)
	return area
raio = float(input())

print("A=%.4f" %area_do_circulo(raio))
	
