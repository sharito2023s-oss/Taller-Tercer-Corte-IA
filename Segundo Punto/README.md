# 📦 Clasificador de Spam usando el Teorema de Bayes

## 📖 Descripción del Proyecto

Este proyecto implementa un clasificador sencillo de spam utilizando el
**Teorema de Bayes**.\
El algoritmo decide si un correo es *spam* basándose en la presencia de
la palabra **"gratis"**, entrenándose con probabilidades obtenidas de
datos históricos.

## 🧠 Teoría: Teorema de Bayes

El Teorema de Bayes permite actualizar probabilidades cuando aparece
nueva evidencia.

### Fórmula

P(A\|B) = \[P(B\|A) \* P(A)\] / P(B)

### Donde:

-   P(A\|B): Probabilidad posterior\
-   P(B\|A): Verosimilitud\
-   P(A): Probabilidad previa\
-   P(B): Probabilidad total

## 📌 Aplicación al Problema de Spam

A = S (correo es spam)\
B = G (correo contiene "gratis")

P(S\|G) = \[P(G\|S) \* P(S)\] / P(G)

## 📊 Datos del Problema

-   P(S) = 0.30\
-   P(G\|S) = 0.80\
-   P(G\|¬S) = 0.10

## 🧮 Desarrollo Matemático

1.  P(¬S) = 1 - 0.30 = 0.70\
2.  P(G) = 0.80(0.30) + 0.10(0.70) = 0.31\
3.  P(S\|G) = (0.80 \* 0.30) / 0.31 = 0.7742

✔ Resultado: **77.42% de probabilidad de que sea spam si contiene
"gratis"**.

## 💻 Implementación en Python

``` python
P_S = 0.30  
P_G_dado_S = 0.80  
P_G_dado_no_S = 0.10  

P_no_S = 1 - P_S
P_G = P_G_dado_S * P_S + P_G_dado_no_S * P_no_S

P_S_dado_G = (P_G_dado_S * P_S) / P_G

print(f"Probabilidad de spam dado 'gratis': {P_S_dado_G:.4f} ({P_S_dado_G*100:.2f}%)")
```

## 🔍 Interpretación

La palabra "gratis" incrementa la probabilidad de spam del 30% a 77.42%.

## 🚀 Aplicaciones

-   Clasificadores Naive Bayes\
-   Filtros de correo\
-   Análisis probabilístico

## 🎯 Conclusión

El Teorema de Bayes permite construir clasificadores simples y efectivos
basados en evidencia.
