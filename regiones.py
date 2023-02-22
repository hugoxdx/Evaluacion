from fastapi import APIRouter, HTTPException

from pydantic import BaseModel

router= APIRouter()

#DEFINIENDO REGIONES DE AFRICA


@router.get("/regiones/")
async def imprimir():
    return [{"id":"10", "Nombre":"Africa" },
            {"id":"20", "Nombre":"Antartica" },
            {"id":"30", "Nombre":"Asia" },
            {"id":"40", "Nombre":"Europe" },
            {"id":"50", "Nombre":"North America" },
            {"id":"60", "Nombre":"Oceania" },
            {"id":"70", "Nombre":"South America" }

    ]


class region (BaseModel):
    id:int
    Nombre:str


reg_list= [region(id=0,Nombre="Central Africa"),
            region(id=1,Nombre="Eastern Africa"),
            region(id=2,Nombre="Northern Africa"),
            region(id=3,Nombre="Southern Africa"),
            region(id=4,Nombre="Western Africa")

            ]

@router.get("/africa/")
async def imprimir():
    return (reg_list)
@router.get("/africa/{id}")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, reg_list)  #Función de orden superior
    try:
        return reg_list(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}

@router.get("/africa/")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, reg_list)  #Función de orden superior
    try:
        return reg_list(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}


@router.post("/africa/")
async def usersclass(user:region):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(reg_list):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            return {"error":"el usuario ya existe"}
    else:
        reg_list.append(user)
        return user
    
@router.put("/africa/")
async def usersclass(user:region):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(reg_list):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           reg_list[index] = user  #accedemos al indice de la lista que hemos encontrado y actualizamos con el nuevo usuario
           found=True
           
    if not found:
        return {"error":"No se ha actualizado el usuario"}
    else:
        return user
    
@router.delete("/africa/{id}")
async def usersclass(id:int):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(reg_list):
        if saved_user.id ==id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           del reg_list[index]  #Eliminamos al indice de la lista que hemos encontrado 
           found=True
           return "El registro se ha eliminado"
       
    if not found:
        return {"error":"No se ha eliminado el usuario"}






# -------- DEFINIENDO REGIONES DE ANTARTICA

class region2 (BaseModel):
    id:int
    Nombre:str

reg_list1= [region2(id=5,Nombre="Antartica")

            ]

@router.get("/antartica/")
async def imprimir():
    return (reg_list1)

@router.get("/antartica/{id}")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, reg_list1)  #Función de orden superior
    try:
        return reg_list1(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}

@router.get("/antartica/")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, reg_list1)  #Función de orden superior
    try:
        return reg_list1(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}


@router.post("/antartica/")
async def usersclass(user:region2):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(reg_list1):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            return {"error":"el usuario ya existe"}
    else:
        reg_list1.append(user)
        return user
    
@router.put("/antartica/")
async def usersclass(user:region2):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(reg_list1):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           reg_list1[index] = user  #accedemos al indice de la lista que hemos encontrado y actualizamos con el nuevo usuario
           found=True
           
    if not found:
        return {"error":"No se ha actualizado el usuario"}
    else:
        return user
    
@router.delete("/antartica/{id}")
async def usersclass(id:int):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(reg_list1):
        if saved_user.id ==id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           del reg_list1[index]  #Eliminamos al indice de la lista que hemos encontrado 
           found=True
           return "El registro se ha eliminado"
       
    if not found:
        return {"error":"No se ha eliminado el usuario"}





#  -------- DEFINIENDO REGINOES DE ASIA


class region3 (BaseModel):
    id:int
    Nombre:str

reg_list2= [ region3(id=0,Nombre="Eastern Asia"),
            region3(id=1,Nombre="Middle Asia"),
            region3(id=2,Nombre="Southeast Asia"),
            region3(id=3,Nombre="Southern and Central Asia")
]

@router.get("/asia/")
async def imprimir():
    return (reg_list2)


@router.get("/asia/{id}")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, reg_list2)  #Función de orden superior
    try:
        return reg_list2(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}

@router.get("/asia/")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, reg_list2)  #Función de orden superior
    try:
        return reg_list2(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}


@router.post("/asia/")
async def usersclass(user:region3):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(reg_list2):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            return {"error":"el usuario ya existe"}
    else:
        reg_list2.append(user)
        return user
    
@router.put("/asia/")
async def usersclass(user:region3):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(reg_list2):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           reg_list2[index] = user  #accedemos al indice de la lista que hemos encontrado y actualizamos con el nuevo usuario
           found=True
           
    if not found:
        return {"error":"No se ha actualizado el usuario"}
    else:
        return user
    
@router.delete("/asia/{id}")
async def usersclass(id:int):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(reg_list2):
        if saved_user.id ==id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           del reg_list2[index]  #Eliminamos al indice de la lista que hemos encontrado 
           found=True
           return "El registro se ha eliminado"
       
    if not found:
        return {"error":"No se ha eliminado el usuario"}







# ------------ DEFINIENDO REGIONES DE EUROPA

class region4 (BaseModel):
    id:int
    Nombre:str

reg_list3= [ region4(id=0,Nombre="Baltic Countries"),
            region4(id=1,Nombre="British Island"),
            region4(id=2,Nombre="Eastern Europe"),
            region4(id=3,Nombre="Nourdic Countries"),
            region4(id=4,Nombre="Southern Europe"),
            region4(id=5,Nombre="Western Europe"),
]

@router.get("/europe/")
async def imprimir():
    return (reg_list3)

@router.get("/europe/{id}")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, reg_list3)  #Función de orden superior
    try:
        return reg_list3(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}

@router.get("/europe/")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, reg_list3)  #Función de orden superior
    try:
        return reg_list3(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}


@router.post("/europe/")
async def usersclass(user:region4):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(reg_list3):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            return {"error":"el usuario ya existe"}
    else:
        reg_list3.append(user)
        return user
    
@router.put("/europe/")
async def usersclass(user:region4):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(reg_list3):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           reg_list3[index] = user  #accedemos al indice de la lista que hemos encontrado y actualizamos con el nuevo usuario
           found=True
           
    if not found:
        return {"error":"No se ha actualizado el usuario"}
    else:
        return user
    
@router.delete("/europe/{id}")
async def usersclass(id:int):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(reg_list3):
        if saved_user.id ==id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           del reg_list3[index]  #Eliminamos al indice de la lista que hemos encontrado 
           found=True
           return "El registro se ha eliminado"
       
    if not found:
        return {"error":"No se ha eliminado el usuario"}








# ---------  DEFINIENDO REGIONES DE NORTE AMERICA

class region5 (BaseModel):
    id:int
    Nombre:str

reg_list4= [region5(id=17,Nombre="Caribbean"),
            region5(id=18,Nombre="Central America"),
            region5(id=19,Nombre="North America"), 
]

@router.get("/northamerica/")
async def imprimir():
    return (reg_list4)


@router.get("/northamerica/{id}")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, reg_list4)  #Función de orden superior
    try:
        return reg_list4(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}

@router.get("/northamerica/")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, reg_list4)  #Función de orden superior
    try:
        return reg_list4(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}


@router.post("/northamerica/")
async def usersclass(user:region5):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(reg_list4):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            return {"error":"el usuario ya existe"}
    else:
        reg_list4.append(user)
        return user
    
@router.put("/northamerica/")
async def usersclass(user:region5):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(reg_list4):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           reg_list4[index] = user  #accedemos al indice de la lista que hemos encontrado y actualizamos con el nuevo usuario
           found=True
           
    if not found:
        return {"error":"No se ha actualizado el usuario"}
    else:
        return user
    
@router.delete("/northamerica/{id}")
async def usersclass(id:int):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(reg_list4):
        if saved_user.id ==id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           del reg_list4[index]  #Eliminamos al indice de la lista que hemos encontrado 
           found=True
           return "El registro se ha eliminado"
       
    if not found:
        return {"error":"No se ha eliminado el usuario"}








# --------DEFINIENDO REGIONES DE OCEANIA

class region6 (BaseModel):
    id:int
    Nombre:str
reg_list5= [region6(id=0,Nombre="Australia and New Zeland"),
            region6(id=1,Nombre="Melanesia"),
            region6(id=2,Nombre="Micronesia/caribbean"),
            region6(id=3,Nombre="Polinesya"),
]

@router.get("/oceania/")
async def imprimir():
    return (reg_list5)

@router.get("/oceania/{id}")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, reg_list5)  #Función de orden superior
    try:
        return reg_list5(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}

@router.get("/oceania/")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, reg_list5)  #Función de orden superior
    try:
        return reg_list5(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}


@router.post("/oceania/")
async def usersclass(user:region6):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(reg_list5):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            return {"error":"el usuario ya existe"}
    else:
        reg_list5.append(user)
        return user
    
@router.put("/oceania/")
async def usersclass(user:region5):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(reg_list5):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           reg_list5[index] = user  #accedemos al indice de la lista que hemos encontrado y actualizamos con el nuevo usuario
           found=True
           
    if not found:
        return {"error":"No se ha actualizado el usuario"}
    else:
        return user
    
@router.delete("/oceania/{id}")
async def usersclass(id:int):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(reg_list5):
        if saved_user.id ==id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           del reg_list5[index]  #Eliminamos al indice de la lista que hemos encontrado 
           found=True
           return "El registro se ha eliminado"
       
    if not found:
        return {"error":"No se ha eliminado el usuario"}
    








# ----------DEFINIENDO REGIONES DE SOUTH AMERICA

class region7 (BaseModel):
    id:int
    Nombre:str

reg_list6= [region7(id=24,Nombre="South America") 
]

@router.get("/southamerica/")
async def imprimir():
    return (reg_list6)




@router.get("/southamerica/{id}")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, reg_list6)  #Función de orden superior
    try:
        return reg_list6(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}

@router.get("/southamerica/")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, reg_list6)  #Función de orden superior
    try:
        return reg_list6(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}


@router.post("/southamerica/")
async def usersclass(user:region7):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(reg_list6):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            return {"error":"el usuario ya existe"}
    else:
        reg_list6.append(user)
        return user
    
@router.put("/southamerica/")
async def usersclass(user:region7):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(reg_list6):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           reg_list6[index] = user  #accedemos al indice de la lista que hemos encontrado y actualizamos con el nuevo usuario
           found=True
           
    if not found:
        return {"error":"No se ha actualizado el usuario"}
    else:
        return user
    
@router.delete("/southamerica/{id}")
async def usersclass(id:int):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(reg_list6):
        if saved_user.id ==id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           del reg_list6[index]  #Eliminamos al indice de la lista que hemos encontrado 
           found=True
           return "El registro se ha eliminado"
       
    if not found:
        return {"error":"No se ha eliminado el usuario"}