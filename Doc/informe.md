## Limpieza y exploración de datos
En el proceso de preparación de la base de datos, se llevaron a cabo varias etapas de limpieza y análisis exploratorio de los datos:

1. Eliminación de duplicados: Se identificó la variable Id_fic como clave única de registro. Durante la revisión, se encontraron 4,578 registros duplicados, los cuales fueron eliminados de la base de datos para asegurar la integridad de los análisis posteriores.

2. Exploración y tratamiento de valores faltantes: Antes de analizar los datos, se reemplazaron los valores 99999 por NA para facilitar la identificación de datos ausentes. Posteriormente, se realizó un análisis de los faltantes por variable:
	- La variable IdNivelEducativo presentó más del 95% de datos faltantes, por lo que se consideró no viable para análisis.
	- Otras variables presentaron porcentajes de faltantes menores al 40%.
	- La variable de interés principal, estrato socioeconómico, presentó 13.2% de casos faltantes.

3. Decisión sobre el manejo de faltantes: Considerando que el foco del estudio es el estrato socioeconómico, se decidió eliminar los casos faltantes en esta variable, trabajando únicamente con el 80% restante de la base de datos que contiene información completa en las variables de interés.
Con estas acciones, la base de datos quedó depurada, consistente y lista para los análisis descriptivos, pruebas de hipótesis y modelamiento posteriores, asegurando la calidad de los resultados.

## Análisis exploratorio y descriptivo

Una vez depurada la base de datos, se realizó un análisis exploratorio y descriptivo para comprender la distribución de las variables de interés y su relación con el estrato socioeconómico. Los principales hallazgos fueron los siguientes:

1. Distribución de estratos socioeconómicos: Los estratos con mayor frecuencia en la base de datos son 2, 3 y 1, siendo el estrato 2 el predominante con 29,520 observaciones, lo que representa 65.6% de la base. Los otros estratos suman solo 26 observaciones en total, siendo el estrato 6 el más preocupante, con únicamente 2 registros. Esto indica una distribución muy desigual de los estratos en la muestra.

2. Relación entre estrato y curso de vida: Se elaboró una gráfica de frecuencia cruzando estrato socioeconómico y curso de vida. El análisis muestra que la mayoría de las observaciones corresponden a niños en su infancia que viven en estratos 2 y 3, reflejando la concentración de la muestra en estos grupos.

3. Relación entre estrato y nivel educativo: Se realizó una gráfica cruzando estrato socioeconómico y nivel educativo. Sin embargo, esta visualización no aporta información descriptiva relevante, debido a que la mayoría de los datos de nivel educativo son NA, limitando la interpretación de esta variable.

### Conclusión:

El análisis exploratorio evidencia que los datos presentan una alta concentración en ciertos estratos (principalmente 2 y 3) y que algunas variables, como el nivel educativo, tienen demasiados valores faltantes, lo que limita su utilidad descriptiva. Los hallazgos obtenidos permitirán orientar los análisis posteriores hacia variables más completas y representativas


## Análisis de diferencias de medias de edad por estrato socioeconómico

El objetivo de este análisis fue determinar si existen diferencias significativas entre las medias de edad de los distintos estratos socioeconómicos. Para ello, se siguió un procedimiento estadístico riguroso, considerando los supuestos necesarios para aplicar pruebas paramétricas.

### 1. Evaluación de supuestos

- Normalidad: Inicialmente se utilizó la prueba de Shapiro-Wilk para cada grupo. Dado que la base de datos es grande, esta prueba puede ser sensible y detectar desviaciones mínimas de la normalidad. Los resultados indicaron que los estratos 4 y 5 cumplen el supuesto de normalidad, y el estrato 6 no pudo evaluarse debido a que solo contiene dos observaciones.
Posteriormente, se aplicó la prueba de Kolmogorov–Smirnov para confirmar estos resultados, obteniéndose el mismo patrón: los grupos mencionados cumplen el supuesto de normalidad.

- Homocedasticidad:
Se aplicó la prueba de Levene para verificar igualdad de varianzas entre los estratos. Los resultados indicaron que se cumple la homocedasticidad, Esto indica que solo un supuesto se cumple y los supuestos paramétricos para ANOVA no se satisfacen completamente.


### 2. Análisis de diferencias entre medias

- ANOVA: A pesar de que los supuestos no se cumplen, se realizó un ANOVA de un factor como referencia. La prueba mostró diferencias significativas entre las medias de edad de los estratos. Sin embargo, debido al incumplimiento de los supuestos, estos resultados deben considerarse con cautela.

- Prueba no paramétrica (Kruskal-Wallis): Dado que los supuestos paramétricos no se cumplían, se aplicó la prueba de Kruskal-Wallis, la cual es apropiada para muestras que no cumplen normalidad ni homocedasticidad. Los resultados confirmaron que existen diferencias significativas entre las medias de edad por estrato.


### 3. Identificación de los estratos con diferencias significativas

Para determinar qué estratos presentan diferencias, se realizó una prueba post hoc de Dunn. El análisis indicó que los estratos 1 y 3 son los grupos que muestran una diferencia significativa en la media de edad.

#### Conclusión:

El análisis evidencia que existen diferencias significativas en la edad promedio entre los estratos socioeconómicos, particularmente entre los estratos 1 y 3. Los resultados resaltan la importancia de considerar pruebas no paramétricas cuando los supuestos de normalidad no se cumplen.

## Asociación entre estrato socioeconómico y localidad

Con el objetivo de explorar la relación entre el estrato socioeconómico y la localidad, se realizaron los siguientes análisis:

### 1. Prueba de independencia (Chi-cuadrado)

Se aplicó la prueba de independencia Chi-cuadrado, cuyos resultados indicaron que la localidad y el estrato socioeconómico están asociadas, es decir, no son variables independientes en la muestra.

### 2. Análisis de correspondencia simple

Dado que se identificó asociación, se llevó a cabo un análisis de correspondencia simple para profundizar en la relación entre ambas variables:

- Las dos primeras dimensiones explican 99.7% de la varianza, lo que indica que capturan prácticamente toda la información de la asociación.
- Los análisis de contribuciones y cosenos cuadrados confirman que estas dos dimensiones son suficientes para interpretar la relación entre estrato y localidad.


### 3. Resultados gráficos e interpretativos
La representación gráfica del análisis de correspondencia permitió identificar asociaciones concretas entre estratos y localidades:
- Estrato bajo 2 : asociado principalmente con Santa Fe, Los Mártires, Chapinero, San Cristóbal, Kennedy, Tunjuelito y Bosa.
- Estrato 1: asociado con Ciudad Bolívar y Usme.
- Estrato 5: no se asocia de manera clara con ninguna localidad.
- Estrato 3: asociado con Fontibón y Puente Aranda.
- Estrato 4: asociado con Teusaquillo, Antonio Nariño y Barrios Unidos.
- Estrato 6: asociado con Usaquén y Engativá.

## Análisis de Clústeres

### 1. Objetivo del análisis

Identificar perfiles sociales diferenciados dentro de la población de niños, niñas y adolescentes (NNA) registrada en intervenciones sociales, agrupando observaciones según variables demográficas y contextuales (sexo, curso de vida, ocupación y localidad) mediante análisis de clústeres.  
El propósito es descubrir patrones naturales sin utilizar una variable dependiente, caracterizar subpoblaciones según sus condiciones sociales y aportar insumos para la segmentación y la planificación de intervenciones.

### 2. Metodología aplicada

Para la construcción de los clústeres se utilizó el algoritmo K-Means, aplicado sobre un conjunto de variables categóricas previamente seleccionadas: SEXO, CURSO DE VIDA, ETNIA, OCUPACIÓN y Localidad_fic.  
Dado que el método K-Means requiere variables numéricas, se realizó un proceso de codificación tipo One-Hot Encoding, transformando cada categoría en variables binarias que permiten calcular distancias entre observaciones.

La selección del número óptimo de clústeres (k) se realizó a partir de los criterios de la curva del codo (Elbow Method) y el coeficiente de silueta (Silhouette Score).  
Con base en estos indicadores, se determinó que el valor k = 6 ofrecía la mejor combinación entre cohesión interna y separación entre grupos.

Cada clúster se analizó posteriormente mediante tablas de frecuencias relativas (% por clúster) y cruces con variables sociodemográficas para identificar las características predominantes de cada grupo.  
Este enfoque permitió obtener perfiles descriptivos sin incluir el estrato socioeconómico como variable dependiente, garantizando un análisis exploratorio independiente de la clasificación oficial.

### 3. Resultados generales

El modelo con k = 6 permitió identificar seis grupos naturales dentro de la población de NNA.  

La siguiente tabla resume las características generales de cada grupo:

| Clúster | Sexo dominante | Etapa del curso de vida | Tamaño (n) |
|----------|----------------|--------------------------|------------|
| 0 | Mujer | Primera infancia | 113 |
| 1 | Hombre | Adolescencia | 186 |
| 2 | Hombre | Infancia | 197 |
| 3 | Mujer | Adolescencia | 209 |
| 4 | Mujer | Infancia | 157 |
| 5 | Hombre | Primera infancia | 122 |

De las variables de ocupación y localidad se observan patrones similares en todos los grupos, aunque con diferencias relevantes entre etapas y género:

- **Clúster 0 – niñas en primera infancia:** 47 % sin ocupación (niñas pequeñas) y 36 % estudiantes. Alta concentración en las localidades de Kennedy, Bosa y Engativá.  
- **Clúster 5 – niños en primera infancia:** patrón similar al anterior, pero masculino, con mayor presencia en Ciudad Bolívar y Suba.  
- **Clúster 2 y 4 – infancia:** niños y niñas en edad escolar, casi todos estudiantes (89 % y 84 % respectivamente), distribuidos principalmente en Kennedy, Bosa y Suba.  
- **Clúster 1 y 3 – adolescencia:** adolescentes hombres y mujeres, en su mayoría estudiantes (83 % y 85 % respectivamente), pero con una ligera presencia de trabajo informal (alrededor del 12 %).  

### 4. Relación con el estrato socioeconómico

Para evaluar la coherencia social de los grupos formados, se realizó un cruce entre los seis clústeres y el estrato socioeconómico reportado en la base de datos.  
Los resultados muestran una correspondencia parcial, donde los grupos con mayor vulnerabilidad social se asocian con los estratos más bajos, y aquellos con mayor participación educativa corresponden a niveles socioeconómicos intermedios.

| Estrato | Clúster 0 | Clúster 1 | Clúster 2 | Clúster 3 | Clúster 4 | Clúster 5 |
|----------|------------|------------|------------|------------|------------|------------|
| 1. Bajo-bajo | 28.3 % | 6.7 % | 15.0 % | 16.7 % | 8.3 % | 25.0 % |
| 2. Bajo | 11.1 % | 20.0 % | 18.7 % | 21.5 % | 16.9 % | 11.8 % |
| 3. Medio-bajo | 8.6 % | 18.8 % | 24.7 % | 21.6 % | 15.3 % | 11.0 % |

El análisis de la tabla evidencia que los **clústeres 0 y 5**, conformados por niños y niñas en primera infancia, concentran las mayores proporciones del **estrato 1 (bajo-bajo)**, reflejando contextos de mayor vulnerabilidad social.  
En contraste, los **clústeres 1, 2, 3 y 4**, integrados por población infantil y adolescente en edad escolar, se asocian principalmente con los **estratos 2 y 3**, correspondientes a niveles socioeconómicos intermedios.



