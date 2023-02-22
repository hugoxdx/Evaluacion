from fastapi import APIRouter, HTTPException

from pydantic import BaseModel

router= APIRouter()

#DEFINIENDO REGIONES DE AFRICA


class regiones(BaseModel):
    id:int
    Nombre:str


regiones_list= [regiones(id=0,Nombre="Central Africa"),
            regiones(id=1,Nombre="Eastern Africa"),
            regiones(id=2,Nombre="Northern Africa"),
            regiones(id=3,Nombre="Southern Africa"),
            regiones(id=4,Nombre="Western Africa"),
            regiones(id=5,Nombre="Antartica"),
            regiones(id=6,Nombre="Eastern Asia"),
            regiones(id=7,Nombre="Middle Asia"),
            regiones(id=8,Nombre="Southeast Asia"),
            regiones(id=9,Nombre="Southern and Central Asia"),
            regiones(id=10,Nombre="Baltic Countries"),
            regiones(id=11,Nombre="British Island"),
            regiones(id=12,Nombre="Eastern Europe"),
            regiones(id=13,Nombre="Nourdic Countries"),
            regiones(id=15,Nombre="Southern Europe"),
            regiones(id=16,Nombre="Western Europe"),
            regiones(id=17,Nombre="Caribbean"),
            regiones(id=18,Nombre="Central America"),
            regiones(id=19,Nombre="North America"),
            regiones(id=20,Nombre="Australia and New Zeland"),
            regiones(id=21,Nombre="Melanesia"),
            regiones(id=22,Nombre="Micronesia/caribbean"),
            regiones(id=23,Nombre="Polinesya"),
            regiones(id=24,Nombre="South America")

            ]

@router.get("/continent/region/")
async def imprimir():
    return (regiones_list)


#checar
@router.get("/continent/region/")
async def imprimir():
    return (regiones_list)
@router.get("/continent/region/")
async def imprimir():
    return (regiones_list)

@router.get("/continent/region/{id}")
async def imprimir(id:int):
    users=filter (lambda user: user.id == id, regiones_list)  #Función de orden superior
    try:
        return list(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}

@router.get("/continent/region/")
async def imprimir(id:int):
    users=filter (lambda user: user.id == id, regiones_list)  #Función de orden superior
    try:
        return list(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}


@router.post("/continent/region/")
async def imprimir(user:regiones):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(regiones_list):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            return {"error":"el usuario ya existe"}
    else:
        regiones_list.append(user)
        return user
    
@router.put("/continent/region/")
async def imprimir(user:regiones):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(regiones_list):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           regiones_list[index] = user  #accedemos al indice de la lista que hemos encontrado y actualizamos con el nuevo usuario
           found=True
           
    if not found:
        return {"error":"No se ha actualizado el usuario"}
    else:
        return user
    
@router.delete("/continent/region/{id}")
async def imprimir(id:int):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(regiones_list):
        if saved_user.id ==id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           del regiones_list[index]  #Eliminamos al indice de la lista que hemos encontrado 
           found=True
           return "El registro se ha eliminado"
       
    if not found:
        return {"error":"No se ha eliminado el usuario"}
