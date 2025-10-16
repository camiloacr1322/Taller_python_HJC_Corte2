Limpieza y exploración de datos
En el proceso de preparación de la base de datos, se llevaron a cabo varias etapas de limpieza y análisis exploratorio de los datos:

1.Eliminación de duplicados: Se identificó la variable Id_fic como clave única de registro. Durante la revisión, se encontraron 4,578 registros duplicados, los cuales fueron eliminados de la base de datos para asegurar la integridad de los análisis posteriores.

2.Exploración y tratamiento de valores faltantes: Antes de analizar los datos, se reemplazaron los valores 99999 por NA para facilitar la identificación de datos ausentes. Posteriormente, se realizó un análisis de los faltantes por variable:
	- La variable IdNivelEducativo presentó más del 95% de datos faltantes, por lo que se consideró no viable para análisis.
	- Otras variables presentaron porcentajes de faltantes menores al 40%.
	- La variable de interés principal, estrato socioeconómico, presentó 13.2% de casos faltantes.

3.Decisión sobre el manejo de faltantes: Considerando que el foco del estudio es el estrato socioeconómico, se decidió eliminar los casos faltantes en esta variable, trabajando únicamente con el 80% restante de la base de datos que contiene información completa en las variables de interés.
Con estas acciones, la base de datos quedó depurada, consistente y lista para los análisis descriptivos, pruebas de hipótesis y modelamiento posteriores, asegurando la calidad de los resultados.

