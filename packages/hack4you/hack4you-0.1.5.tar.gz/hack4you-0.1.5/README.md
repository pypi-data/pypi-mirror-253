# Hack4U Academy Courses Library

Una biblioteca de Python para consultar cursos de la academia Hack4U.

## Cursos disponibles

- Introducción a Linux [15 horas]
- Personalización de Linux [3 horas]
- Introducción al Hacking [53 horas]
- Python ofensivo [35 horas]

## Instalación

Instala el paquete usando 'pip3':

```python3
pip3 install hack4u
```

## Uso básico

### Listar todos los cursos

```python
from hack4u import list_courses

list_courses()
```

### Obtener un curso por nombre

```python
from hack4u import get_course_by_name

course = get_course_by_name("Python ofensivo")
print(course)
```

### Calcular duración total de los cursos (horas)

```python
from hack4u import total_duration

duracion = total_duration()
print(f"Duración total {duracion} horas.")
```

















