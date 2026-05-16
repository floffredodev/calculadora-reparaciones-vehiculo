# 🔧 Calculadora de Reparaciones de Vehículos
Herramienta de línea de comandos para calcular el costo total de reparaciones, incluyendo repuestos, mano de obra e IVA (12% Ecuador).
> Es básica
---

## 📋 ¿Qué hace este programa?

Dado el costo de los repuestos, las horas trabajadas y la tarifa por hora, la calculadora:

1. Calcula la mano de obra (`horas × tarifa`)
2. Obtiene el subtotal (`repuestos + mano de obra`)
3. Agrega el IVA del 12% (vigente en Ecuador)
4. Muestra el **total a pagar** con un resumen detallado
5. Pregunta si deseas calcular otra reparación o salir

```
Calculadora de reparaciones de vehículos
 
Costo total de repuestos ($): 150
Horas de mano de obra: 3
Tarifa por hora de mano de obra ($): 12
--------------------------------
Resumen de la reparación:
--------------------------------
Costo de repuestos: $150.00
Costo de mano de obra: $36.00
--------------------------------
Subtotal: $186.00
IVA (12%): $22.32
--------------------------------
Total a pagar: $208.32
--------------------------------

¿Calcular otra reparación? (s/n): 
```

---

## 🚀 Requisitos

- Python 3.x instalado en tu sistema

Verifica que lo tienes con:

```bash
python3 --version
```

---

## ▶️ Cómo ejecutarlo

```bash
# 1. Clona este repositorio
git clone https://github.com/floffredodev/calculadora-reparaciones-vehiculo.git

# 2. Entra a la carpeta
cd calculadora-reparaciones-vehiculo

# 3. Ejecuta el programa
py calculadora-reparaciones.py
```

---

## 🗂️ Estructura del proyecto

```
calculadora-reparaciones/
│
└── calculadora_reparaciones.py   # Programa principal
└── README.md                     # Este archivo
```

---

## 🧠 Conceptos de Python aplicados

Este proyecto para mí fue una introducción a la programación. Cubre:

| Concepto | Uso en el programa |
|---|---|
| `print()` / `input()` | Mostrar resultados y pedir datos al usuario |
| Variables y tipos de datos | `float` para precios y horas, `str` para texto |
| Operadores aritméticos | Cálculo de mano de obra, subtotal, IVA y total |
| `if / elif / else` | Validación de entradas negativas y menú de salida |
| `while` + `break` | Bucle principal y bucles de validación por campo |
| `try / except` | Manejo de errores cuando el usuario escribe letras |
| f-strings | Formato de números con 2 decimales en la salida |

---

## ✅ Validaciones incluidas

- El programa no acepta valores negativos en ningún campo
- Si el usuario escribe letras en vez de números, pide el dato de nuevo sin romperse
- La respuesta final acepta `s`/`S` y `n`/`N` sin distinción de mayúsculas

---

## 🇪🇨 Contexto fiscal

El IVA aplicado es del **12%**, conforme a la tarifa general del Servicio de Rentas Internas (SRI) de Ecuador vigente al momento del desarrollo.

---

## 👨‍💻 Autor

**Francis**

---

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Úsalo, modifícalo y compártelo libremente.
