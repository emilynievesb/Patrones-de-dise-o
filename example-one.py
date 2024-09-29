# Producto
class CV:
    def __init__(self):
        self.secciones = []

    def agregar_seccion(self, seccion):
        self.secciones.append(seccion)

    def mostrar(self):
        for seccion in self.secciones:
            print(seccion)

# Builder
class CVBuilder:
    def agregar_informacion_personal(self, info):
        pass

    def agregar_experiencia_laboral(self, experiencia):
        pass

    def agregar_educacion(self, educacion):
        pass

# Builder Concreto
class CVConcretoBuilder(CVBuilder):
    def __init__(self):
        self.cv = CV()

    def agregar_informacion_personal(self, info):
        self.cv.agregar_seccion(f"Información Personal: {info}")

    def agregar_experiencia_laboral(self, experiencia):
        self.cv.agregar_seccion(f"Experiencia Laboral: {experiencia}")

    def agregar_educacion(self, educacion):
        self.cv.agregar_seccion(f"Educación: {educacion}")

    def obtener_cv(self):
        return self.cv

# Director
class GeneradorCV:
    def __init__(self, builder):
        self.builder = builder

    def construir_cv(self, info_personal, experiencia, educacion):
        self.builder.agregar_informacion_personal(info_personal)
        self.builder.agregar_experiencia_laboral(experiencia)
        self.builder.agregar_educacion(educacion)

# Uso
builder = CVConcretoBuilder()
generador = GeneradorCV(builder)
generador.construir_cv("Juan Pérez", "Desarrollador en Empresa XYZ", "Ingeniero en Sistemas")
cv = builder.obtener_cv()
cv.mostrar()
