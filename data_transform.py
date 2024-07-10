import pandas as pd

# Ruta del archivo CSV intermedio
archivo_csv = 'ventas_por_factura_2024.csv'

try:
    # Leer el archivo CSV
    data = pd.read_csv(archivo_csv)
    
    # Ordenar los datos por nombre
    data_ordenada = data.sort_values(by='Fecha de factura')
    
    # Exportar a Excel
    archivo_excel = 'ventas_por_factura_2024.xlsx'
    data_ordenada.to_excel(archivo_excel, index=False)
    
    print(f"Datos exportados exitosamente a {archivo_excel}")
except Exception as e:
    print(f"Error al transformar los datos: {e}")