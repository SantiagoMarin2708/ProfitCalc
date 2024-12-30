import streamlit as st

def calcular_ganancias(precio_venta, costo_producto, cantidad_vendida):
    return (precio_venta - costo_producto) * cantidad_vendida

st.title("Calculadora de Ganancias")
st.write("Santiago Marin Carrillo")
st.write("Esta aplicación te ayuda a calcular las ganancias de un producto.")

precio_venta = st.number_input("Precio de venta por unidad ($):", min_value=0.0, step=0.01)
costo_producto = st.number_input("Costo de producto por unidad ($):", min_value=0.0, step=0.01)
cantidad_vendida = st.number_input("Cantidad vendida (unidades):", min_value=0, step=1)

if st.button("Calcular ganancias"):
    if precio_venta < costo_producto:
        st.warning("El precio de venta es menor que el costo de producto. Estás teniendo pérdidas.")
    ganancias = calcular_ganancias(precio_venta, costo_producto, cantidad_vendida)
    st.success(f"Las ganancias son: ${ganancias:,.2f}")