import copy

# Interfaz Documento
class Documento:
    def clonar(self):
        pass

    def editar_contenido(self, nuevo_contenido):
        pass

# Prototipo Concreto
class CurriculumVitae(Documento):
    def __init__(self, contenido):
        self.contenido = contenido

    def clonar(self):
        return copy.deepcopy(self)

    def editar_contenido(self, nuevo_contenido):
        self.contenido = nuevo_contenido

    def mostrar(self):
        print(f"Curriculum Vitae: {self.contenido}")

# Prototipo Concreto
class CartaPresentacion(Documento):
    def __init__(self, contenido):
        self.contenido = contenido

    def clonar(self):
        return copy.deepcopy(self)

    def editar_contenido(self, nuevo_contenido):
        self.contenido = nuevo_contenido

    def mostrar(self):
        print(f"Carta de Presentación: {self.contenido}")

# Cliente
class EditorDeDocumentos:
    def __init__(self):
        self.plantillas = {}

    def agregar_plantilla(self, nombre, documento):
        self.plantillas[nombre] = documento

    def crear_documento(self, nombre):
        plantilla = self.plantillas.get(nombre)
        if plantilla:
            return plantilla.clonar()
        else:
            print(f"No se encontró la plantilla {nombre}")
            return None

# Uso
editor = EditorDeDocumentos()
cv_plantilla = CurriculumVitae("Plantilla de CV básica")
carta_plantilla = CartaPresentacion("Plantilla de Carta de Presentación")

editor.agregar_plantilla("CV", cv_plantilla)
editor.agregar_plantilla("Carta", carta_plantilla)

nuevo_cv = editor.crear_documento("CV")
nuevo_cv.editar_contenido("Nuevo contenido para el CV de Juan Pérez")
nuevo_cv.mostrar()

nueva_carta = editor.crear_documento("Carta")
nueva_carta.editar_contenido("Nuevo contenido para la Carta de Presentación")
nueva_carta.mostrar()
