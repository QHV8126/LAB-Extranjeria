from extranjeria import *

# main 
if __name__ == "__main__":
    # Lectura de datos
    registros = lee_datos_extranjeria("data/extranjeriaSevilla.csv")
   
    print("TEST DE LA FUNCIÓN lee_datos_extranjeria:")
    print(f"Leídos {len(registros)} registros.")
    print("Mostrando los 3 primeros:")
    for registro in registros[:3]:
        print(registro)
    print()
    print("Mostrando los 3 últimos:")
    for registro in registros[-3:]:
        print(registro)

    print("\nTEST DE LA FUNCIÓN numero_nacionalidades_distintas:")
    print(f"El número de nacionalidades distintas es {numero_nacionalidades_distintas(registros)}")

    '''
   TEST DE LA FUNCIÓN secciones_distritos_con_extranjeros_nacionalidades:
    Hay 503 secciones de distritos con residentes cuya procedencia es ALEMANIA o ITALIA.
    Mostrando 3 secciones:
    '''
    print("\nTEST DE LA FUNCIÓN secciones_distritos_con_extranjeros_nacionalidades:")
    paises = {"ALEMANIA", "ITALIA"}
    distritos_secciones = secciones_distritos_con_extranjeros_nacionalidades(registros, paises)
    print(f"Hay {len(distritos_secciones)} secciones de distritos con residentes cuya procedencia es {paises}.")
    print("Mostrando 3 secciones:")
    print(distritos_secciones[:3])

    print("\nTEST DE LA FUNCIÓN total_extranjeros_por_pais:")
    total_por_pais = total_extranjeros_por_pais(registros)
    print("Mostrando el número de residentes para algunos países de procedencia:")
    for pais in ["ALEMANIA", "ITALIA", "MARRUECOS"]:
        print(f"{pais}: {total_por_pais[pais]}")
        
    print("\nTEST DE LA FUNCIÓN top_n_extranjeria:")
    top_n = top_n_extranjeria(registros, 5)
    print("Mostrando los 5 países de los que proceden más residentes:")
    print(top_n)

    print("\nTEST DE LA FUNCIÓN barrio_mas_multicultural:")
    print(f"El barrio más multicultural de sevilla es {barrio_mas_multicultural(registros)}")

    print("\nTEST DE LA FUNCIÓN barrio_con_mas_extranjeros:")
    print(f"El barrio con más residentes extranjeros es {barrio_con_mas_extranjeros(registros)}")
    print(f"El barrio con más hombres residentes extranjeros es {barrio_con_mas_extranjeros(registros, 'HOMBRES')}")
    print(f"El barrio con más mujeres residentes extranjeras es {barrio_con_mas_extranjeros(registros, 'MUJERES')}")

'''
    print("\nTEST DE LA FUNCIÓN pais_mas_representado_por_distrito:")
    distrito_pais = pais_mas_representado_por_distrito(registros)
    print("Los países con más residentes en cada distrito son los siguientes:")
    for distrito in sorted(distrito_pais):
        print(f"Distrito: {distrito:02} => {distrito_pais[distrito]}")





    

   '''