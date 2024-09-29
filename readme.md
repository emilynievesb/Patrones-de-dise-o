# Implementación de Patrones de Diseño: Builder y Prototype

Este repositorio contiene dos implementaciones de patrones de diseño en Python: el **Patrón Builder** y el **Patrón Prototype**. Ambos patrones se han aplicado a casos de uso distintos con ejemplos sencillos para su comprensión.

## 1. Patrón Builder: Constructor de Currículums Vitae

### Descripción

El **Patrón Builder** se utiliza para construir objetos complejos paso a paso. En este caso, hemos aplicado el patrón para crear un **Constructor de Currículums Vitae (CV)**, donde el usuario puede agregar secciones como información personal, experiencia laboral, educación, entre otras, de manera flexible.

### Estructura del Código

-   **CV**: Es el objeto final (Currículum Vitae) que estamos construyendo, el cual contiene las diferentes secciones.
-   **CVBuilder**: Es la interfaz que define los métodos para añadir diferentes partes al CV.
-   **CVConcretoBuilder**: Es la implementación concreta del Builder, que construye el CV paso a paso.
-   **GeneradorCV (Director)**: El Director que gestiona el proceso de construcción del CV según las elecciones del usuario.

### Uso

1. El Director **GeneradorCV** controla cómo se construye el CV llamando a los métodos del **CVBuilder**.
2. El **CVBuilder** agrega cada sección al CV en el orden que el Director indique.
3. Finalmente, se obtiene el objeto `CV` completamente construido, listo para ser utilizado.

### Ejecución del Código

```python
# Creamos un builder para hacer un CV
builder = CVConcretoBuilder()

# El director construye un CV agregando las secciones
generador = GeneradorCV(builder)
generador.construir_cv("Juan Pérez", "Desarrollador en Empresa XYZ", "Ingeniero en Sistemas")

# Obtenemos y mostramos el CV completo
cv = builder.obtener_cv()
cv.mostrar()
```

## 2. Patrón Prototype: Editor de Documentos

### Descripción

El **Patrón Prototype** permite crear copias de objetos existentes (prototipos) en lugar de crear nuevos objetos desde cero. En este ejemplo, hemos implementado un **Editor de Documentos** que permite crear nuevas instancias de documentos como Currículums Vitae, cartas de presentación, etc., a partir de plantillas predefinidas.

### Estructura del Código

-   **Documento**: Es la interfaz que define los métodos comunes para los documentos, como `clonar` y `editarContenido`.
-   **CurriculumVitae y CartaPresentacion**: Son las implementaciones concretas de los prototipos (documentos).
-   **EditorDeDocumentos (Cliente)**: Es el cliente que maneja los prototipos y permite crear nuevos documentos clonándolos.

### Uso

1. El **EditorDeDocumentos** tiene un conjunto de plantillas (prototipos) que puede clonar.
2. Cuando el usuario selecciona una plantilla, se clona un nuevo documento basado en esa plantilla.
3. El usuario puede personalizar el contenido del documento clonado sin modificar la plantilla original.

### Ejecución del Código

```python
# Creamos un editor de documentos con plantillas
editor = EditorDeDocumentos()
cv_plantilla = CurriculumVitae("Plantilla de CV básica")
carta_plantilla = CartaPresentacion("Plantilla de Carta de Presentación")

# Agregamos las plantillas al editor
editor.agregar_plantilla("CV", cv_plantilla)
editor.agregar_plantilla("Carta", carta_plantilla)

# Clonamos y personalizamos los documentos
nuevo_cv = editor.crear_documento("CV")
nuevo_cv.editar_contenido("Nuevo contenido para el CV de Juan Pérez")
nuevo_cv.mostrar()

nueva_carta = editor.crear_documento("Carta")
nueva_carta.editar_contenido("Nuevo contenido para la Carta de Presentación")
nueva_carta.mostrar()
```

## Requisitos

-   Python 3.x
-   No se requieren dependencias externas.

## Ejecución

Para ejecutar las implementaciones:

1. Clona este repositorio.
2. Navega a la carpeta del proyecto.
3. Ejecuta los archivos Python para cada patrón de diseño, como:

```bash
python builder_cv.py
python prototype_documentos.py
```

## Referencias

-   [Documentación del Patrón Builder](https://refactoring.guru/design-patterns/builder)
-   [Documentación del Patrón Prototype](https://refactoring.guru/design-patterns/prototype)
