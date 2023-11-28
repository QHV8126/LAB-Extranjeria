import csv
from collections import namedtuple,defaultdict

RegistroExtranjeria = namedtuple('RegistroExtranjeria', 
    'distrito,seccion,barrio,pais,hombres,mujeres')

def lee_datos_extranjeria(ruta_fichero):
    with open(ruta_fichero, encoding = 'utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        res = [RegistroExtranjeria(int(distrito.strip()),int(seccion.strip()),
            barrio.strip(),pais.strip(),int(hombres.strip()),int(mujeres.strip())) 
            for distrito,seccion,barrio,pais,hombres,mujeres in lector]
    return res

def numero_nacionalidades_distintas(registros):
    res = {pais for _,_,_,pais,_,_ in registros}
    return len(res)

def secciones_distritos_con_extranjeros_nacionalidades(registros, paises):
    res = [(distrito,seccion) for distrito,seccion,_,pais,_,_ in registros
         if pais in paises]
    return sorted(res)

def total_extranjeros_por_pais(registros):
    res = defaultdict(int)
    for distrito,seccion,barrio,pais,hombres,mujeres in registros:
        res[pais] += hombres + mujeres 
    return dict(res)

def top_n_extranjeria(registros, n=3):
    datos = total_extranjeros_por_pais(registros)
    res = list()
    for pais,numero_extranjeros in datos.items():
        res.append((pais,numero_extranjeros))
    return sorted(res, key = lambda x:x[1], reverse=True)[:n]

def barrio_mas_multicultural(registros):
    res = defaultdict(set)
    for _,_,barrio,pais,_,_ in registros:
        res[barrio].update(pais)
    res = sorted(res, key = lambda x:len(x[1]))
    return res[0]

def barrio_con_mas_extranjeros(registros, tipo=None):
    res = defaultdict(int)
    for _,_,barrio,_,hombres,mujeres in registros:
        if tipo == None:
            res[barrio] += hombres + mujeres
        if tipo == 'HOMBRES':
            res[barrio] += hombres
        if tipo == 'MUJERES':
            res[barrio] += mujeres
    res = sorted(res, key = lambda x:len(x[1]))
    return res[0]

def pais_mas_representado_por_distrito(registros):
    res = defaultdict(str)
    for distrito,seccion,barrio,pais,hombres,mujeres in registros:
        res[distrito] = pais_con_mas_extranjeros_residentes
    dicc = defaultdict(int)
    distrito_pais = list()
    for distrito_filtro in {distrito for distrito,_,_,_,_,_ in registros}:
        for distrito,seccion,barrio,pais,hombres,mujeres in registros:
            dicc[pais] += hombres+mujeres
        dicc = sorted(dicc, key=lambda x:x[1])
        distrito_paisa.append((distrito_filtro, ))