import pandas as pd

# Ruta del archivo CSV intermedio
archivo_csv = 'ventas_por_factura_2024.csv'

try:
    # Leer el archivo CSV
    data = pd.read_csv(archivo_csv)
    
    # Filtrar por las facturas que empiece con 'C'
    data_filtrada = data[data['N° de factura'].str.startswith('C')]

    data_ordenada = data_filtrada.sort_values(by='N° de factura')
    
    # Exportar a Excel
    archivo_excel = 'ventas_por_factura_2024.xlsx'
    data_ordenada.to_excel(archivo_excel, index=False)
    
    print(f"Datos exportados exitosamente a {archivo_excel}")
except Exception as e:
    print(f"Error al transformar los datos: {e}")