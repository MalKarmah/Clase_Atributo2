class Alumno:

    def inicializar(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota

    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Nota:",self.nota)

    def mostrar_resultado(self):
        if self.nota>=6:
            print("Aprobo")
        else:
            print("No Aprobo")

estudiante=Alumno()
estudiante.inicializar("Carlos",7)
estudiante.imprimir()
estudiante.mostrar_resultado()

