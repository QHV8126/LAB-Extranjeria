import csv
from collections import namedtuple,defaultdict
from typing import List,Tuple,Dict,Optional

RegistroExtranjeria = namedtuple('RegistroExtranjeria', 
    'distrito,seccion,barrio,pais,hombres,mujeres')

def lee_datos_extranjeria(ruta_fichero:str)->List[RegistroExtranjeria]:
    with open(ruta_fichero, encoding = 'utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        res = [RegistroExtranjeria(distrito,seccion,
            barrio,pais,int(hombres),int(mujeres)) 
            for distrito,seccion,barrio,pais,hombres,mujeres in lector]
    return res

def numero_nacionalidades_distintas(registros:List[RegistroExtranjeria])->int:
    res = {pais for _,_,_,pais,_,_ in registros}
    return len(res)

def secciones_distritos_con_extranjeros_nacionalidades(
    registros:List[RegistroExtranjeria], paises:Tuple[str])->List[Tuple[str,str]]:
    res = (None,None)
    res = {(distrito,seccion) for distrito,seccion,_,pais,_,_ in registros
         if pais in paises and (distrito,seccion) not in res}
    return sorted(list(res))

def total_extranjeros_por_pais(registros:List[RegistroExtranjeria])->Dict[str,int]:
    res = defaultdict(int)
    for distrito,seccion,barrio,pais,hombres,mujeres in registros:
        res[pais] += hombres + mujeres 
    return dict(res)

def top_n_extranjeria(
    registros:List[RegistroExtranjeria], n:Optional[int]=3)->List[Tuple[str,int]]:
    datos = total_extranjeros_por_pais(registros)
    res = list()
    for pais,numero_extranjeros in datos.items():
        res.append((pais,numero_extranjeros))
    return sorted(res, key = lambda x:x[1], reverse=True)[:n]

def barrio_mas_multicultural(registros:List[RegistroExtranjeria])->str:
    res = defaultdict(set)
    for _,_,barrio,pais,_,_ in registros:
        res[barrio].add(pais)
    res = sorted(res.items(), key=lambda x: len(x[1]), reverse=True)
    return res[0][0]

def barrio_con_mas_extranjeros(
    registros:List[RegistroExtranjeria], tipo:Optional[str]=None)->str:
    res = defaultdict(int)
    for _,_,barrio,_,hombres,mujeres in registros:
        if tipo == None:
            res[barrio] += hombres + mujeres
        if tipo == 'HOMBRES':
            res[barrio] += hombres
        if tipo == 'MUJERES':
            res[barrio] += mujeres
    res = sorted(res.items(), key=lambda x: x[1], reverse=True)
    return res[0][0]

def pais_mas_representado_por_distrito(registros:List[RegistroExtranjeria])->Dict[str,str]:
    distrito_pais = list()
    for distrito_filtro in {distrito for distrito,_,_,_,_,_ in registros}:
        dicc = defaultdict(int)
        for distrito,_,_,pais,hombres,mujeres in registros:
            if distrito == distrito_filtro:
                dicc[pais] += hombres+mujeres
        dicc = sorted(dicc.items(), key=lambda x:x[1], reverse=True)
        distrito_pais.append((distrito_filtro, dicc[0][0]))
    return {distrito:pais for distrito,pais in distrito_pais}