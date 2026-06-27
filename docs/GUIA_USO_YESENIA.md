# Guia de uso: SDG Localidades

## Para que sirve

SDG Localidades genera el informe mensual de PQRS por localidad
automaticamente. En lugar de hacer el proceso manual de 2 horas,
solo debes arrastrar los archivos y hacer clic.

## Que necesitas

- Los 7 archivos Excel del mes (los mismos de siempre)
- Windows 10 o 11
- Acceso a la carpeta donde estan los archivos

## Paso a paso

### Paso 1: Abrir el sistema

1. Abre la carpeta `sdg-localidades`
2. Haz doble clic en `INICIAR.bat`
3. Se abrira una ventana negra (consola) y luego tu navegador
4. Espera a que aparezca la pagina azul con el titulo "SDG Localidades"
5. **No cierres la ventana negra** mientras uses el sistema

### Paso 2: Cargar los archivos

En la pagina web veras una zona punteada que dice
"Arrastra los archivos fuente aqui"

1. Abre la carpeta donde tienes los 7 archivos Excel del mes
2. Seleccionalos todos y ARRASTRALOS a la zona punteada
   (o haz clic en "Seleccionar archivos" y buscalos)
3. Cada archivo aparecera listado con una etiqueta de color:
   - AZUL: BD PQRS Bogotá
   - VERDE: SAC Atencion
   - MORADO: Resumen SIDE
   - NARANJA: Productividad CR
   - ROSADO: Productividad PH
   - TURQUESA: Encuestas
4. Si falta algun archivo, aparecera una advertencia amarilla
5. Verifica que esten los 7 antes de continuar

### Paso 3: Procesar el informe

1. Una vez cargados los archivos, el boton azul
   "PROCESAR INFORME" se activara
2. Haz clic en el boton
3. Veras el progreso en vivo:
   - Una barra de progreso que se llena
   - Una lista de fases que se van marcando
   - Mensajes de detalle de cada paso
4. El proceso toma de 2 a 3 minutos

### Paso 4: Descargar el Excel

1. Cuando termine, aparecera un mensaje verde:
   "Informe Generado!"
2. Haz clic en "DESCARGAR INFORME EXCEL"
3. El archivo se llamara:
   `INFORME PQRS LOCALIDADES [MES] [AÑO].xlsx`
4. Guardalo donde prefieras

### Paso 5: Cerrar el sistema

1. Cierra la pestana del navegador
2. En la ventana negra, presiona Ctrl+C
3. Confirma con "S" si pregunta
4. Listo

## Archivos que genera el sistema

El Excel contiene 39 hojas. Las mas importantes son:

| Hoja | Que contiene |
|------|--------------|
| PORTADA | Titulo, fecha, contenido del informe |
| RESUMEN CIFRAS | Datos consolidados de todas las fuentes por localidad |
| INF WEB | PQRS recibidas por canal web |
| DIAS GESTION | Dias promedio de gestion, pendientes, porcentajes |
| SIDE GESTION | Documentos extraviados: stock, registrados, entregados |
| INF Localidades PPT | Tablas Q1-Q6 para PowerPoint |
| VALIDACION | Verificacion de que los datos son correctos |

## Solucion de problemas

### "No se pudo conectar con el servidor"
- Cierra la ventana negra y abre INICIAR.bat de nuevo
- Revisa que no tengas otro programa usando el puerto 5000

### "Error al procesar archivo"
- Verifica que los archivos sean los del mes correcto
- Confirma que los archivos no esten danados (abrelos en Excel)
- Intenta de nuevo con "Nuevo informe"

### El proceso se queda en 0%
- Cierra todo y vuelve a iniciar
- Si persiste, avisame para revisar

### No recuerdo que archivos necesito
Los 7 archivos son:
1. BD PQRS BOGOTA TE ESCUCHA [MES] [AÑO].xlsx
2. 05. SAC_atencion - [MES] [AÑO].xlsx
3. Resumen SIDE [MES] [AÑO].xlsx
4. MAYO[ANO]_PRODUCTIVIDAD_CR.xlsx
5. MAYO[ANO]_PRODUCTIVIDAD_PH.xlsx
6. REPORTE PRODUCTIVIDAD ENCUESTAS [MES] [AÑO].xlsx
7. BASE DATOS PPT LOCALIDADES [MES] [AÑO].xlsx
