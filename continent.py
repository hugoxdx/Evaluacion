
from fastapi import APIRouter, HTTPException

from pydantic import BaseModel

router= APIRouter()

class continente(BaseModel):
    id:int
    Nombre:str


continente_list= [continente(id=0,Nombre="Africa"),
            continente(id=1,Nombre="Antartica"),
            continente(id=2,Nombre="Asia"),
            continente(id=3,Nombre="Europe"),
            continente(id=4,Nombre="North America"),
            continente(id=5,Nombre="Oceania"),
            continente(id=6,Nombre="South America")

            ]

@router.get("/continent/")
async def imprimir():
    return (continente_list)
@router.get("/continent/")
async def imprimir():
    return (continente_list)

@router.get("/continent/{id}")
async def imprimir(id:int):
    users=filter (lambda user: user.id == id, continente_list)  #Función de orden superior
    try:
        return list(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}

@router.get("/continent/")
async def imprimir(id:int):
    users=filter (lambda user: user.id == id, continente_list)  #Función de orden superior
    try:
        return list(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}


@router.post("/continent/")
async def imprimir(user:continente):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(continente_list):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            return {"error":"el usuario ya existe"}
    else:
        continente_list.append(user)
        return user
    
@router.put("/continent/")
async def imprimir(user:continente):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(continente_list):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           continente_list[index] = user  #accedemos al indice de la lista que hemos encontrado y actualizamos con el nuevo usuario
           found=True
           
    if not found:
        return {"error":"No se ha actualizado el usuario"}
    else:
        return user
    
@router.delete("/continent/{id}")
async def imprimir(id:int):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(continente_list):
        if saved_user.id ==id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           del continente_list[index]  #Eliminamos al indice de la lista que hemos encontrado 
           found=True
           return "El registro se ha eliminado"
       
    if not found:
        return {"error":"No se ha eliminado el usuario"}
