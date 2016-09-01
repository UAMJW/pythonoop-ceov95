class Estudiante:

	def __init__(self, nombre, apellido, cif, carrera, edad, sexo):
		self.nombre = nombre
		self.apellido = apellido
		self.cif = cif
		self.carrera = carrera
		self.edad = edad
		self.sexo = sexo

	def getNombre(self):
			return self.nombre
	def getApellido(self):
			return self.apellido
	def getCif(self):
			return self.cif
	def getCarrera(self):
			return self.carrera
	def getEdad(self):
			return self.edad
	def getSexo(self):
			return self.sexo

	def imprimirEstudiante(self):
		print("\nNombre: " + self.getNombre() + "\nApellido: " + self.getApellido() + "\nCIF: " + self.getCif() 
		+ "\nCarrera: " + self.getCarrera() + "\nEdad: " + str(self.getEdad()) + "\nSexo: "+ self.getSexo())

nombre = raw_input("Ingrese su nombre: ")
apellido = raw_input("Ingrese su apellido: ")	
cif = raw_input("Ingrese su CIF: ")
carrera = raw_input("Ingrese su carrera: ")
edad = raw_input("Ingrese su edad: ")
sexo = raw_input("Ingrese su sexo: ")
e = Estudiante(nombre,apellido,cif,carrera,edad,sexo)
e.imprimirEstudiante()