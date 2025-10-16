# Registros administrativos de intervenciones sociales “niños, niñas y adolescentes”

## Business understanding

### 1.	Determinar Objetivos del Negocio

La base corresponde a registros administrativos de intervenciones sociales dirigidas a niños, niñas y adolescentes (NNA). Su objetivo principal es la prevención y atención del trabajo infantil, así como el acompañamiento psicosocial tanto a los menores como a sus familias. En ella se registran datos sobre cuándo y dónde se realizó la intervención, además del perfil profesional que brindó la atención (psicólogo, trabajador social, nutricionista, entre otros).

Este registro permite llevar un seguimiento individual de cada caso, con el fin de verificar si la intervención logró que el menor dejara de trabajar o si fue necesario implementar otro tipo de medidas de protección


#### Objetivo General del negocio

Analizar los cambios ocurridos según los diferentes estratos socioeconómicos, a partir de variables previamente seleccionadas con base en criterios demográficos.

#### Objetivos especificos 

- Caracterizar y realizar un análisis descriptivo de las variables seleccionadas, comparando sus comportamientos entre los diferentes estratos socioeconómicos.

- Aplicar pruebas de hipótesis para determinadas variables, con el fin de identificar diferencias significativas entre los estratos socioeconómicos y otras variables cualitativas, tomando como referencia la media de la edad.

- Desarrollar un modelo analítico enfocado en un solo estrato socioeconómico, que permita profundizar en su comportamiento particular.

#### Criterios de Éxito del Negocio

Calidad del análisis y consistencia de los resultados: Los análisis deben mostrar relaciones coherentes entre las variables y el estrato socioeconómico, con resultados estadísticamente significativos y consistentes con la información disponible en la base de datos

Capacidad explicativa del modelo: El modelo desarrollado debe permitir identificar patrones claros o asociaciones relevantes que ayuden a comprender cómo varían las características de la población según el estrato socioeconómico.

Validez y completitud de los datos: El proceso de depuración y análisis debe asegurar que el porcentaje de datos faltantes o inconsistentes no afecte la validez de las conclusiones.


## 2. Evaluar la Situación

### Requerimientos, Suposiciones y Restricciones
Origen de la base de datos
La información proviene de registros administrativos de intervenciones realizadas a niños, niñas y adolescentes (NNA). La base consolidada integra variables demográficas, educativas, laborales y socioeconómicas, estructuradas para permitir análisis descriptivos y comparativos por estrato socioeconómico.

#### Suposiciones
- Se asume que los registros corresponden a intervenciones reales y verificadas.
- Las variables incluidas reflejan adecuadamente las condiciones demográficas y sociales del NNA al momento del registro.
- Se considera que la codificación de categorías (sexo, etnia, ocupación, nivel educativo, etc.) es homogénea entre diferentes fuentes o periodos.

#### Restricciones: 
- Presencia de valores faltantes o inconsistencias en algunos campos, lo que puede limitar el tamaño efectivo de la muestra.
- Cobertura geográfica y temporal acotada a los registros disponibles, sin posibilidad de generalización a toda la población.
- Limitaciones en la actualización de datos, lo cual puede afectar la precisión de ciertas variables.


### Terminología

- NNA: Niños, Niñas y Adolescentes. Hace referencia a la población objeto de los registros.
- ESTRATO SOCIOECONÓMICO: Clasificación oficial que agrupa los hogares según sus condiciones de vivienda e ingresos.
- ZONA / LOCALIDAD / UPZ / BARRIO: Variables territoriales que identifican la ubicación geográfica del NNA o su hogar.
- VÍNCULO CON EL JEFE DE HOGAR: Relación del NNA con la persona cabeza de hogar (hijo, nieto, otro pariente, etc.).
- IdNivelEducativo: Nivel educativo alcanzado por el NNA al momento del registro (por ejemplo: primaria, secundaria, sin escolaridad).
- OCUPACIÓN: Actividad laboral principal que realiza el NNA en caso de encontrarse vinculado a una ocupación.
- POBLACIÓN DIFERENCIAL Y DE INCLUSIÓN: Clasificación que identifica si el NNA pertenece a un grupo poblacional con enfoque diferencial (personas con discapacidad, víctimas del conflicto, migrantes, población LGBTIQ+, entre otros).
- ETNIA: Grupo étnico al que pertenece el NNA, si aplica (indígena, afrodescendiente, ROM, etc.).
- CURSO DE VIDA: Categoría etaria que ubica al NNA dentro de una etapa del desarrollo (infancia, adolescencia, juventud).
- ESTADO CIVIL: Condición civil reportada en el registro (soltero, casado, unión libre, etc.), en caso de aplicar.
- SEXO: Variable demográfica que identifica el sexo biológico del NNA (femenino o masculino).
- NACIONALIDAD: País de origen o nacionalidad declarada del NNA.
- Id_fic: Identificador único de la ficha o registro individual de intervención asignado a cada NNA.

## 3. Determinar Objetivos de Minería de Datos

### Objetivos de Minería de Datos
- **Descriptivo:** Identificar y caracterizar patrones estadísticos entre los diferentes estratos socioeconómicos, considerando variables demográficas.  
- **Comparativo:**  Evaluar diferencias significativas entre grupos mediante pruebas de hipótesis y análisis de correspondencia simple. 
- **Diagnóstico:** etectar posibles asociaciones entre  las variables de interes.  
- **Analítico:** Desarrollar un modelo o perfil específico para un estrato socioeconómico seleccionado, que permita profundizar en su estructura y comportamient.  

### Criterios de Éxito en Minería de Datos
- Obtener resultados estadísticamente significativos (p < 0.05) en las pruebas aplicadas..  
- Lograr representaciones gráficas y tablas que faciliten la interpretación de los patrones detectados entre estratos. 
- Asegurar que los hallazgos permitan una descripción clara, precisa y sustentada del comportamiento de las variables frente al estrato socioeconómico

## 4. Elaborar Plan de Proyecto
Plan del Proyecto
- Comprensión del negocio (ya planteada).
- Comprensión de los datos: exploración inicial, calidad de datos, detección de inconsistencias.
- Preparación de los datos: limpieza, integración, transformación de variables.
- Modelado: selección de técnicas estadísticas (regresión, clasificación, supervivencia).
- Evaluación: validar resultados frente a criterios de éxito.
- Despliegue: generar reportes, dashboards y recomendaciones para tomadores de decisión.

Evaluación inicial de Herramientas y Técnica

Herramientas estadísticas: Python (pandas, scikit-learn, statsmodels), R.
Visualización: Power BI, Tableau, Matplotlib.

Modelos posibles:
 - Regresión logística (factores asociados a desvinculación).
 - Análisis de supervivencia (tiempos de seguimiento).
 - Árboles de decisión o Random Forest (clasificación de riesgo).

