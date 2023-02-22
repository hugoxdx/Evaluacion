from fastapi import APIRouter, HTTPException

from pydantic import BaseModel

router= APIRouter()


@router.get("/regiones/")
async def imprimir():
    return [{"id":"10", "Nombre":"central america" },
            {"id":"20", "Nombre":"eastern america" },
            {"id":"30", "Nombre":"northamerica" },
            {"id":"40", "Nombre":"western africa" },
            {"id":"50", "Nombre":"antartica" },
            {"id":"60", "Nombre":"Oceania" },
            {"id":"70", "Nombre":"eastern asia" }

    ]




#----------------------------DEFINIENDO lqw ciudades de central africa
class ciudad (BaseModel):
    id:int
    Nombre:str


ciu_list= [ciudad(id=0,Nombre="ANGOLA"),
           ciudad(id=1,Nombre="CENTRAL AFRICAN REPUBLIC"),
           ciudad(id=2,Nombre="CAMEROON"),
           ciudad(id=3,Nombre="CONGO"),
           ciudad(id=4,Nombre="GABON"),
           ciudad(id=5,Nombre="EQUATORIAL"),
           ciudad(id=6,Nombre="SAO TOME AND PRINCIPE"),
           ciudad(id=7,Nombre="CHAD"),
           ciudad(id=8,Nombre="CONGO THE DEMOCRATIC REPUBLIC OF THE")
  ]

@router.get("/centralafrica/")
async def imprimir():
    return (ciu_list)

@router.get("/centralafrica/{id}")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, ciu_list)  #Función de orden superior
    try:
        return ciu_list(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}

@router.get("/centralafrica/")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, ciu_list)  #Función de orden superior
    try:
        return ciu_list(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}


@router.post("/centralafrica/")
async def usersclass(user:ciudad):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            return {"error":"el usuario ya existe"}
    else:
        ciu_list.append(user)
        return user
    
@router.put("/centralafrica/")
async def usersclass(user:ciudad):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           ciu_list[index] = user  #accedemos al indice de la lista que hemos encontrado y actualizamos con el nuevo usuario
           found=True
           
    if not found:
        return {"error":"No se ha actualizado el usuario"}
    else:
        return user
    
@router.delete("/centralafrica/{id}")
async def usersclass(id:int):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list):
        if saved_user.id ==id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           del ciu_list[index]  #Eliminamos al indice de la lista que hemos encontrado 
           found=True
           return "El registro se ha eliminado"
       
    if not found:
        return {"error":"No se ha eliminado el usuario"}






#---------------------------------DEFINIENDO lqw ciudades de eastern africa
class ciudad1 (BaseModel):
    id:int
    Nombre:str


ciu_list1= [ciudad1(id=0,Nombre="BURUNDI"),
           ciudad1(id=1,Nombre="COMOROS"),
           ciudad1(id=2,Nombre="DIJIBOUTI"),
           ciudad1(id=3,Nombre="ERITREA"),
           ciudad1(id=4,Nombre="ETHIOPIA"),
           ciudad1(id=5,Nombre="BRISTISH INDIAN OCEAN TERRITORY"),
           ciudad1(id=6,Nombre="KENYA"),
           ciudad1(id=7,Nombre="MADAGASCAR"),
           ciudad1(id=8,Nombre="MOZAMBIQUE"),
           ciudad1(id=9,Nombre="MAURITIUS"),
           ciudad1(id=10,Nombre="MALAWI"),
           ciudad1(id=11,Nombre="MAYOTTE"),
           ciudad1(id=12,Nombre="REUNION"),
           ciudad1(id=13,Nombre="RWANDA"),
           ciudad1(id=14,Nombre="SOMALIA"),
           ciudad1(id=15,Nombre="SEYCHELLES"),
           ciudad1(id=16,Nombre="TANZANIA"),
           ciudad1(id=17,Nombre="UGANDA"),
           ciudad1(id=18,Nombre="ZAMBIA"),
           ciudad1(id=19,Nombre="ZIMBABWE")
  ]

@router.get("/easternafrica/")
async def imprimir():
    return (ciu_list1)

@router.get("/easternafrica/{id}")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, ciu_list1)  #Función de orden superior
    try:
        return ciu_list1(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}

@router.get("/easternafrica/")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, ciu_list1)  #Función de orden superior
    try:
        return ciu_list1(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}


@router.post("/easternafrica/")
async def usersclass(user:ciudad1):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list1):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            return {"error":"el usuario ya existe"}
    else:
        ciu_list1.append(user)
        return user
    
@router.put("/easternafrica/")
async def usersclass(user:ciudad1):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list1):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           ciu_list1[index] = user  #accedemos al indice de la lista que hemos encontrado y actualizamos con el nuevo usuario
           found=True
           
    if not found:
        return {"error":"No se ha actualizado el usuario"}
    else:
        return user
    
@router.delete("/easternafrica/{id}")
async def usersclass(id:int):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list1):
        if saved_user.id ==id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           del ciu_list1[index]  #Eliminamos al indice de la lista que hemos encontrado 
           found=True
           return "El registro se ha eliminado"
       
    if not found:
        return {"error":"No se ha eliminado el usuario"}







#-----------------------------------DEFINIENDO lqw ciudades de northern africa
class ciudad2 (BaseModel):
    id:int
    Nombre:str


ciu_list2= [ciudad2(id=0,Nombre="ARGELIA"),
           ciudad2(id=1,Nombre="EGYPT"),
           ciudad2(id=2,Nombre="WESTERN SAHARA"),
           ciudad2(id=3,Nombre="LIBYAN ARAB JAMAHIRIYA"),
           ciudad2(id=4,Nombre="MOROCCO"),
           ciudad2(id=5,Nombre="SUDAN"),
           ciudad2(id=6,Nombre="TUNISIA")
  ]

@router.get("/northernafrica/")
async def imprimir():
    return (ciu_list2)

@router.get("/northernafrica/{id}")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, ciu_list2)  #Función de orden superior
    try:
        return ciu_list2(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}

@router.get("/northernafrica/")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, ciu_list2)  #Función de orden superior
    try:
        return ciu_list2(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}


@router.post("/northernafrica/")
async def usersclass(user:ciudad2):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list2):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            return {"error":"el usuario ya existe"}
    else:
        ciu_list2.append(user)
        return user
    
@router.put("/northernafrica/")
async def usersclass(user:ciudad2):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list2):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           ciu_list2[index] = user  #accedemos al indice de la lista que hemos encontrado y actualizamos con el nuevo usuario
           found=True
           
    if not found:
        return {"error":"No se ha actualizado el usuario"}
    else:
        return user
    
@router.delete("/northernafrica/{id}")
async def usersclass(id:int):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list2):
        if saved_user.id ==id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           del ciu_list2[index]  #Eliminamos al indice de la lista que hemos encontrado 
           found=True
           return "El registro se ha eliminado"
       
    if not found:
        return {"error":"No se ha eliminado el usuario"}









#-------------------------------DEFINIENDO lqw ciudades de southern africa
class ciudad3 (BaseModel):
    id:int
    Nombre:str


ciu_list3= [ciudad3(id=0,Nombre="BOTSWANA"),
           ciudad3(id=1,Nombre="LESOTHO"),
           ciudad3(id=2,Nombre="NAMIBIA"),
           ciudad3(id=3,Nombre="SWANZILAND"),
           ciudad3(id=4,Nombre="SOUTH AFRICA")
  ]

@router.get("/southernafrica/")
async def imprimir():
    return (ciu_list3)
@router.get("/southernafrica/{id}")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, ciu_list3)  #Función de orden superior
    try:
        return ciu_list3(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}

@router.get("/southernafrica/")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, ciu_list3)  #Función de orden superior
    try:
        return ciu_list3(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}


@router.post("/southernafrica/")
async def usersclass(user:ciudad3):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list3):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            return {"error":"el usuario ya existe"}
    else:
        ciu_list3.append(user)
        return user
    
@router.put("/southernafrica/")
async def usersclass(user:ciudad3):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list3):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           ciu_list3[index] = user  #accedemos al indice de la lista que hemos encontrado y actualizamos con el nuevo usuario
           found=True
           
    if not found:
        return {"error":"No se ha actualizado el usuario"}
    else:
        return user
    
@router.delete("/southernafrica/{id}")
async def usersclass(id:int):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list3):
        if saved_user.id ==id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           del ciu_list[index]  #Eliminamos al indice de la lista que hemos encontrado 
           found=True
           return "El registro se ha eliminado"
       
    if not found:
        return {"error":"No se ha eliminado el usuario"}








#-------------------------------DEFINIENDO lqw ciudades de western africa
class ciudad4 (BaseModel):
    id:int
    Nombre:str


ciu_list4= [ciudad4(id=0,Nombre="BENIN"),
           ciudad4(id=1,Nombre="BURKINA FASO"),
           ciudad4(id=2,Nombre="COTE DLVOIRE"),
           ciudad4(id=3,Nombre="CAPE VERDE"),
           ciudad4(id=4,Nombre="GHANA"),
           ciudad4(id=5,Nombre="GUINEA"),
           ciudad4(id=6,Nombre="GAMBIA"),
           ciudad4(id=7,Nombre="GUINEA BISSAUL"),
           ciudad4(id=8,Nombre="LIBERIA"),
           ciudad4(id=9,Nombre="MALI"),
           ciudad4(id=10,Nombre="MAURITANIA"),
           ciudad4(id=11,Nombre="NIGER"),
           ciudad4(id=12,Nombre="NIGERIA"),
           ciudad4(id=13,Nombre="SENEGAL"),
           ciudad4(id=14,Nombre="SAINT HELENA"),
           ciudad4(id=15,Nombre="SIERRA HELENA"),
           ciudad4(id=16,Nombre="TOGO")
  ]

@router.get("/westernafrica/")
async def imprimir():
    return (ciu_list4)

@router.get("/westernafrica/{id}")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, ciu_list4)  #Función de orden superior
    try:
        return ciu_list4(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}

@router.get("/westernafrica/")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, ciu_list4)  #Función de orden superior
    try:
        return ciu_list4(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}


@router.post("/westernafrica/")
async def usersclass(user:ciudad4):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list4):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            return {"error":"el usuario ya existe"}
    else:
        ciu_list4.append(user)
        return user
    
@router.put("/westernafrica/")
async def usersclass(user:ciudad4):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list4):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           ciu_list4[index] = user  #accedemos al indice de la lista que hemos encontrado y actualizamos con el nuevo usuario
           found=True
           
    if not found:
        return {"error":"No se ha actualizado el usuario"}
    else:
        return user
    
@router.delete("/westernafrica/{id}")
async def usersclass(id:int):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list4):
        if saved_user.id ==id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           del ciu_list4[index]  #Eliminamos al indice de la lista que hemos encontrado 
           found=True
           return "El registro se ha eliminado"
       
    if not found:
        return {"error":"No se ha eliminado el usuario"}










#-------------------------------------DEFINIENDO las ciudades de antartica
class ciudad5 (BaseModel):
    id:int
    Nombre:str


ciu_list5= [ciudad5(id=0,Nombre="ANTARTICA"),
           ciudad5(id=1,Nombre="FRENCH SOUTHERN TERRITORIES"),
           ciudad5(id=2,Nombre="BOUVET ISLAND"),
           ciudad5(id=3,Nombre="HEARD ISLAND AND MCDONALD ISLAND"),
           ciudad5(id=4,Nombre="SOUTH GEORGIA THE SOUTH SANDWICH ISLANDS")
  ]

@router.get("/antartica/")
async def imprimir():
    return (ciu_list5)
@router.get("/antartica/{id}")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, ciu_list5)  #Función de orden superior
    try:
        return ciu_list5(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}

@router.get("/antartica/")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, ciu_list5)  #Función de orden superior
    try:
        return ciu_list5(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}


@router.post("/antartica/")
async def usersclass(user:ciudad5):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list5):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            return {"error":"el usuario ya existe"}
    else:
        ciu_list5.append(user)
        return user
    
@router.put("/antartica/")
async def usersclass(user:ciudad5):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list5):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           ciu_list5[index] = user  #accedemos al indice de la lista que hemos encontrado y actualizamos con el nuevo usuario
           found=True
           
    if not found:
        return {"error":"No se ha actualizado el usuario"}
    else:
        return user
    
@router.delete("/antartica/{id}")
async def usersclass(id:int):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list5):
        if saved_user.id ==id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           del ciu_list5[index]  #Eliminamos al indice de la lista que hemos encontrado 
           found=True
           return "El registro se ha eliminado"
       
    if not found:
        return {"error":"No se ha eliminado el usuario"}









#------------------------DEFINIENDO lqw ciudades de eastern asia
class ciudad6 (BaseModel):
    id:int
    Nombre:str


ciu_list6= [ciudad6(id=0,Nombre="CHINA"),
           ciudad6(id=1,Nombre="HONG KONG"),
           ciudad6(id=2,Nombre="JAPAN"),
           ciudad6(id=3,Nombre="SOUTH KOREA"),
           ciudad6(id=4,Nombre="MACAO"),
           ciudad6(id=5,Nombre="MONGOLIA"),
           ciudad6(id=6,Nombre="NORTH KOREA"),
           ciudad6(id=7,Nombre="TAIWAN")
  ]

@router.get("/easternasia/")
async def imprimir():
    return (ciu_list6)
@router.get("/easternasia/{id}")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, ciu_list6)  #Función de orden superior
    try:
        return ciu_list6(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}

@router.get("/easternasia/")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, ciu_list6)  #Función de orden superior
    try:
        return ciu_list6(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}


@router.post("/easternasia/")
async def usersclass(user:ciudad6):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list6):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            return {"error":"el usuario ya existe"}
    else:
        ciu_list6.append(user)
        return user
    
@router.put("/easternasia/")
async def usersclass(user:ciudad6):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list6):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           ciu_list6[index] = user  #accedemos al indice de la lista que hemos encontrado y actualizamos con el nuevo usuario
           found=True
           
    if not found:
        return {"error":"No se ha actualizado el usuario"}
    else:
        return user
    
@router.delete("/easternasia/{id}")
async def usersclass(id:int):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list6):
        if saved_user.id ==id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           del ciu_list[index]  #Eliminamos al indice de la lista que hemos encontrado 
           found=True
           return "El registro se ha eliminado"
       
    if not found:
        return {"error":"No se ha eliminado el usuario"}









#----------------------------------------DEFINIENDO lqw ciudades de Middle East
class ciudad7 (BaseModel):
    id:int
    Nombre:str


ciu_list7= [ciudad7(id=0,Nombre="UNITED ARAB EMIRATES"),
           ciudad7(id=1,Nombre="ARMENIA"),
           ciudad7(id=2,Nombre="ARZEBAIJAN"),
           ciudad7(id=3,Nombre="BAHRAIN"),
           ciudad7(id=4,Nombre="CYPRUS"),
           ciudad7(id=5,Nombre="GEORGIA"),
           ciudad7(id=6,Nombre="IRAQ"),
           ciudad7(id=7,Nombre="ISRAEL"),
           ciudad7(id=8,Nombre="JORDAN"),
           ciudad7(id=9,Nombre="KUWAIT"),
           ciudad7(id=10,Nombre="LEBANON"),
           ciudad7(id=11,Nombre="OMAN"),
           ciudad7(id=12,Nombre="PALESTINE"),
           ciudad7(id=13,Nombre="QATAR"),
           ciudad7(id=14,Nombre="SAUDI ARABIA"),
           ciudad7(id=15,Nombre="SYRIA"),
           ciudad7(id=16,Nombre="TURKEY"),
           ciudad7(id=17,Nombre="YEMEN")
  ]

@router.get("/middleeast/")
async def imprimir():
    return (ciu_list7)
@router.get("/middleeast/{id}")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, ciu_list7)  #Función de orden superior
    try:
        return ciu_list7(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}

@router.get("/middleeast/")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, ciu_list7)  #Función de orden superior
    try:
        return ciu_list7(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}


@router.post("/middleeast/")
async def usersclass(user:ciudad7):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list7):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            return {"error":"el usuario ya existe"}
    else:
        ciu_list7.append(user)
        return user
    
@router.put("/middleeast/")
async def usersclass(user:ciudad7):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list7):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           ciu_list7[index] = user  #accedemos al indice de la lista que hemos encontrado y actualizamos con el nuevo usuario
           found=True
           
    if not found:
        return {"error":"No se ha actualizado el usuario"}
    else:
        return user
    
@router.delete("/middleeast/{id}")
async def usersclass(id:int):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list7):
        if saved_user.id ==id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           del ciu_list7[index]  #Eliminamos al indice de la lista que hemos encontrado 
           found=True
           return "El registro se ha eliminado"
       
    if not found:
        return {"error":"No se ha eliminado el usuario"}






#---------------------DEFINIENDO lqw ciudades de Southeast Asia
class ciudad8 (BaseModel):
    id:int
    Nombre:str


ciu_list8= [ciudad8(id=0,Nombre="BRUNEI"),
           ciudad8(id=1,Nombre="INDONESIA"),
           ciudad8(id=2,Nombre="CAMBODIA"),
           ciudad8(id=3,Nombre="LAOS"),
           ciudad8(id=4,Nombre="MYANMAR"),
           ciudad8(id=5,Nombre="MALASYA"),
           ciudad8(id=6,Nombre="PHILIPPINES"),
           ciudad8(id=7,Nombre="SINGAPORE"),
           ciudad8(id=8,Nombre="THAILAND"),
           ciudad8(id=9,Nombre="EAST ASIA"),
           ciudad8(id=10,Nombre="VIETNAM")
  ]

@router.get("/southeastasia/")
async def imprimir():
    return (ciu_list8)
@router.get("/southeastasia/{id}")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, ciu_list8)  #Función de orden superior
    try:
        return ciu_list8(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}

@router.get("/southeastasia/")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, ciu_list8)  #Función de orden superior
    try:
        return ciu_list8(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}


@router.post("/southeastasia/")
async def usersclass(user:ciudad8):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list8):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            return {"error":"el usuario ya existe"}
    else:
        ciu_list8.append(user)
        return user
    
@router.put("/southeastasia/")
async def usersclass(user:ciudad8):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list8):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           ciu_list8[index] = user  #accedemos al indice de la lista que hemos encontrado y actualizamos con el nuevo usuario
           found=True
           
    if not found:
        return {"error":"No se ha actualizado el usuario"}
    else:
        return user
    
@router.delete("/southeastasia/{id}")
async def usersclass(id:int):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list8):
        if saved_user.id ==id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           del ciu_list8[index]  #Eliminamos al indice de la lista que hemos encontrado 
           found=True
           return "El registro se ha eliminado"
       
    if not found:
        return {"error":"No se ha eliminado el usuario"}








#----------------------------------DEFINIENDO lqw ciudades de Southern and Central Asia
class ciudad9 (BaseModel):
    id:int
    Nombre:str


ciu_list9= [ciudad9(id=0,Nombre="AFGHANISTAN"),
           ciudad9(id=1,Nombre="BANGLADESH"),
           ciudad9(id=2,Nombre="BHUTAN"),
           ciudad9(id=3,Nombre="INDIA"),
           ciudad9(id=4,Nombre="IRAN"),
           ciudad9(id=5,Nombre="KAZAKSTAN"),
           ciudad9(id=6,Nombre="KYRGYZSTAN"),
           ciudad9(id=7,Nombre="SRI LANKA"),
           ciudad9(id=8,Nombre="MALDIVES"),
           ciudad9(id=9,Nombre="NEPAL"),
           ciudad9(id=10,Nombre="PAKISTAN"),
           ciudad9(id=11,Nombre="TAJIKISTAN"),
           ciudad9(id=12,Nombre="TURKMENISTAN"),
           ciudad9(id=13,Nombre="UZBEKSITAN")
  ]

@router.get("/southernandcentralasia/")
async def imprimir():
    return (ciu_list9)
@router.get("/southernandcentralasia/{id}")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, ciu_list9)  #Función de orden superior
    try:
        return ciu_list9(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}

@router.get("/southernandcentralasia/")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, ciu_list9)  #Función de orden superior
    try:
        return ciu_list9(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}


@router.post("/southernandcentralasia/")
async def usersclass(user:ciudad9):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list9):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            return {"error":"el usuario ya existe"}
    else:
        ciu_list9.append(user)
        return user
    
@router.put("/southernandcentralasia/")
async def usersclass(user:ciudad9):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list9):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           ciu_list9[index] = user  #accedemos al indice de la lista que hemos encontrado y actualizamos con el nuevo usuario
           found=True
           
    if not found:
        return {"error":"No se ha actualizado el usuario"}
    else:
        return user
    
@router.delete("/southernandcentralasia/{id}")
async def usersclass(id:int):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list9):
        if saved_user.id ==id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           del ciu_list9[index]  #Eliminamos al indice de la lista que hemos encontrado 
           found=True
           return "El registro se ha eliminado"
       
    if not found:
        return {"error":"No se ha eliminado el usuario"}









#----------------------------DEFINIENDO lqw ciudades de Baltic Countries
class ciudad10 (BaseModel):
    id:int
    Nombre:str


ciu_list10= [ciudad(id=0,Nombre="ESTONIA"),
           ciudad(id=1,Nombre="LITHUANIA"),
           ciudad(id=2,Nombre="LATVIA")
  ]

@router.get("/balticcountries/")
async def imprimir():
    return (ciu_list10)
@router.get("/balticcountries/{id}")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, ciu_list10)  #Función de orden superior
    try:
        return ciu_list10(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}

@router.get("/balticcountries/")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, ciu_list10)  #Función de orden superior
    try:
        return ciu_list10(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}


@router.post("/balticcountries/")
async def usersclass(user:ciudad10):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list10):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            return {"error":"el usuario ya existe"}
    else:
        ciu_list10.append(user)
        return user
    
@router.put("/balticcountries/")
async def usersclass(user:ciudad10):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list10):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           ciu_list10[index] = user  #accedemos al indice de la lista que hemos encontrado y actualizamos con el nuevo usuario
           found=True
           
    if not found:
        return {"error":"No se ha actualizado el usuario"}
    else:
        return user
    
@router.delete("/balticcountries/{id}")
async def usersclass(id:int):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list10):
        if saved_user.id ==id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           del ciu_list10[index]  #Eliminamos al indice de la lista que hemos encontrado 
           found=True
           return "El registro se ha eliminado"
       
    if not found:
        return {"error":"No se ha eliminado el usuario"}







#------------------------DEFINIENDO lqw ciudades de British Islands
class ciudad11 (BaseModel):
    id:int
    Nombre:str


ciu_list11= [ciudad11(id=0,Nombre="UNITED KINGDOM"),
           ciudad11(id=1,Nombre="IRELAND")
  ]

@router.get("/britishislands/")
async def imprimir():
    return (ciu_list11)

@router.get("/britishislands/{id}")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, ciu_list11)  #Función de orden superior
    try:
        return ciu_list11(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}

@router.get("/britishislands/")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, ciu_list11)  #Función de orden superior
    try:
        return ciu_list11(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}


@router.post("/britishislands/")
async def usersclass(user:ciudad11):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list11):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            return {"error":"el usuario ya existe"}
    else:
        ciu_list11.append(user)
        return user
    
@router.put("/britishislands/")
async def usersclass(user:ciudad11):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list11):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           ciu_list11[index] = user  #accedemos al indice de la lista que hemos encontrado y actualizamos con el nuevo usuario
           found=True
           
    if not found:
        return {"error":"No se ha actualizado el usuario"}
    else:
        return user
    
@router.delete("/britishislands/{id}")
async def usersclass(id:int):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list11):
        if saved_user.id ==id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           del ciu_list11[index]  #Eliminamos al indice de la lista que hemos encontrado 
           found=True
           return "El registro se ha eliminado"
       
    if not found:
        return {"error":"No se ha eliminado el usuario"}










#-----------------------------DEFINIENDO lqw ciudades de Eastern Europe
class ciudad12 (BaseModel):
    id:int
    Nombre:str


ciu_list12= [ciudad12(id=0,Nombre="BULGARIA"),
           ciudad12(id=1,Nombre="BELARUS"),
           ciudad12(id=2,Nombre="CZECH REPUBLIC"),
           ciudad12(id=3,Nombre="HUNGARY"),
           ciudad12(id=4,Nombre="MOLDOVA"),
           ciudad12(id=5,Nombre="POLAND"),
           ciudad12(id=6,Nombre="ROMANIA"),
           ciudad12(id=7,Nombre="RUSSIAN FEDERATION"),
           ciudad12(id=8,Nombre="SLOVAKIA")
  ]

@router.get("/easterneurope/")
async def imprimir():
    return (ciu_list12)

@router.get("/easterneurope/{id}")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, ciu_list12)  #Función de orden superior
    try:
        return ciu_list12(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}

@router.get("/easterneurope/")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, ciu_list12)  #Función de orden superior
    try:
        return ciu_list12(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}


@router.post("/easterneurope/")
async def usersclass(user:ciudad12):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list12):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            return {"error":"el usuario ya existe"}
    else:
        ciu_list12.append(user)
        return user
    
@router.put("/easterneurope/")
async def usersclass(user:ciudad12):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list12):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           ciu_list12[index] = user  #accedemos al indice de la lista que hemos encontrado y actualizamos con el nuevo usuario
           found=True
           
    if not found:
        return {"error":"No se ha actualizado el usuario"}
    else:
        return user
    
@router.delete("/easterneurope/{id}")
async def usersclass(id:int):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list12):
        if saved_user.id ==id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           del ciu_list12[index]  #Eliminamos al indice de la lista que hemos encontrado 
           found=True
           return "El registro se ha eliminado"
       
    if not found:
        return {"error":"No se ha eliminado el usuario"}





#-----------------------------DEFINIENDO lqw ciudades de Nordic Countries
class ciudad13 (BaseModel):
    id:int
    Nombre:str


ciu_list13= [ciudad13(id=0,Nombre="DENMARK"),
           ciudad13(id=1,Nombre="FINLAND"),
           ciudad13(id=2,Nombre="FAROE ISLANDS"),
           ciudad13(id=3,Nombre="ICELAND"),
           ciudad13(id=4,Nombre="NORWAY"),
           ciudad13(id=5,Nombre="SVALBARD AND JAN MAYEN"),
           ciudad13(id=6,Nombre="SWEDEN")
  ]

@router.get("/nordiccountries/")
async def imprimir():
    return (ciu_list13)

@router.get("/nordiccountries/{id}")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, ciu_list13)  #Función de orden superior
    try:
        return ciu_list13(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}

@router.get("/nordiccountries/")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, ciu_list13)  #Función de orden superior
    try:
        return ciu_list13(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}


@router.post("/nordiccountries/")
async def usersclass(user:ciudad13):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list13):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            return {"error":"el usuario ya existe"}
    else:
        ciu_list13.append(user)
        return user
    
@router.put("/nordiccountries/")
async def usersclass(user:ciudad13):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list13):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           ciu_list13[index] = user  #accedemos al indice de la lista que hemos encontrado y actualizamos con el nuevo usuario
           found=True
           
    if not found:
        return {"error":"No se ha actualizado el usuario"}
    else:
        return user
    
@router.delete("/nordiccountries/{id}")
async def usersclass(id:int):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list13):
        if saved_user.id ==id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           del ciu_list13[index]  #Eliminamos al indice de la lista que hemos encontrado 
           found=True
           return "El registro se ha eliminado"
       
    if not found:
        return {"error":"No se ha eliminado el usuario"}






#----------------------------DEFINIENDO lqw ciudades de Southern Europe
class ciudad14 (BaseModel):
    id:int
    Nombre:str


ciu_list14= [ciudad14(id=0,Nombre="ALBANIA"),
           ciudad14(id=1,Nombre="ANDORRA"),
           ciudad14(id=2,Nombre="BOSNIA AND HERZEGONIA"),
           ciudad14(id=3,Nombre="SPAIN"),
           ciudad14(id=4,Nombre="GILBRALTAR"),
           ciudad14(id=5,Nombre="GREECE"),
           ciudad14(id=6,Nombre="CROATIA"),
           ciudad14(id=7,Nombre="ITALY"),
           ciudad14(id=8,Nombre="MACEDONIA"),
           ciudad14(id=9,Nombre="MALTA"),
           ciudad14(id=10,Nombre="PORTUGAL"),
           ciudad14(id=11,Nombre="SAN MARINO"),
           ciudad14(id=12,Nombre="SLOVENIA"),
           ciudad14(id=13,Nombre="HOLY SEE VATICAN CITY"),
           ciudad14(id=14,Nombre="YUGOSLAVIA")
  ]

@router.get("/southerneurope/")
async def imprimir():
    return (ciu_list14)

@router.get("/southerneurope/{id}")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, ciu_list14)  #Función de orden superior
    try:
        return ciu_list14(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}

@router.get("/southerneurope/")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, ciu_list14)  #Función de orden superior
    try:
        return ciu_list14(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}


@router.post("/southerneurope/")
async def usersclass(user:ciudad14):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list14):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            return {"error":"el usuario ya existe"}
    else:
        ciu_list14.append(user)
        return user
    
@router.put("/southerneurope/")
async def usersclass(user:ciudad14):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list14):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           ciu_list14[index] = user  #accedemos al indice de la lista que hemos encontrado y actualizamos con el nuevo usuario
           found=True
           
    if not found:
        return {"error":"No se ha actualizado el usuario"}
    else:
        return user
    
@router.delete("/southerneurope/{id}")
async def usersclass(id:int):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list14):
        if saved_user.id ==id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           del ciu_list14[index]  #Eliminamos al indice de la lista que hemos encontrado 
           found=True
           return "El registro se ha eliminado"
       
    if not found:
        return {"error":"No se ha eliminado el usuario"}










#-----------------------------DEFINIENDO lqw ciudades de Western Europe
class ciudad15 (BaseModel):
    id:int
    Nombre:str


ciu_list15= [ciudad15(id=0,Nombre="AUSTRIA"),
           ciudad15(id=1,Nombre="BELGIUM"),
           ciudad15(id=2,Nombre="SWITZERLAND"),
           ciudad15(id=3,Nombre="GERMANY"),
           ciudad15(id=4,Nombre="FRANCE"),
           ciudad15(id=5,Nombre="LIECHTENSTEIN"),
           ciudad15(id=6,Nombre="LUXEMBURGO"),
           ciudad15(id=7,Nombre="MONACO"),
           ciudad15(id=8,Nombre="NERTHERLANDS")
  ]

@router.get("/westerneurope/")
async def imprimir():
    return (ciu_list15)
@router.get("/westerneurope/{id}")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, ciu_list15)  #Función de orden superior
    try:
        return ciu_list15(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}

@router.get("/westerneurope/")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, ciu_list15)  #Función de orden superior
    try:
        return ciu_list15(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}


@router.post("/westerneurope/")
async def usersclass(user:ciudad15):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list15):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            return {"error":"el usuario ya existe"}
    else:
        ciu_list15.append(user)
        return user
    
@router.put("/westerneurope/")
async def usersclass(user:ciudad15):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list15):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           ciu_list15[index] = user  #accedemos al indice de la lista que hemos encontrado y actualizamos con el nuevo usuario
           found=True
           
    if not found:
        return {"error":"No se ha actualizado el usuario"}
    else:
        return user
    
@router.delete("/westerneurope/{id}")
async def usersclass(id:int):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list15):
        if saved_user.id ==id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           del ciu_list15[index]  #Eliminamos al indice de la lista que hemos encontrado 
           found=True
           return "El registro se ha eliminado"
       
    if not found:
        return {"error":"No se ha eliminado el usuario"}









#---------------------------------DEFINIENDO lqw ciudades de CARIBBEAN
class ciudad16 (BaseModel):
    id:int
    Nombre:str


ciu_list16= [ciudad16(id=0,Nombre="ARUBA"),
           ciudad16(id=1,Nombre="ANGUILLA"),
           ciudad16(id=2,Nombre="NETHERLANDS ANTILLES"),
           ciudad16(id=3,Nombre="ANTIGUA AND BARDUBA"),
           ciudad16(id=4,Nombre="BAHAMAS"),
           ciudad16(id=5,Nombre="BARBADOS"),
           ciudad16(id=6,Nombre="CUBA"),
           ciudad16(id=7,Nombre="CAYMAN ISLANDS"),
           ciudad16(id=8,Nombre="DOMINICA"),
           ciudad16(id=9,Nombre="DOMINICAN REPUBLIC"),
           ciudad16(id=10,Nombre="GUADELOUPE"),
           ciudad16(id=11,Nombre="GRENADA"),
           ciudad16(id=12,Nombre="HAITI"),
           ciudad16(id=13,Nombre="JAMAICA"),
           ciudad16(id=14,Nombre="SAINT  KITTS AND NEVIS"),
           ciudad16(id=15,Nombre="SAINT LUCIA"),
           ciudad16(id=16,Nombre="MONTSERAT"),
           ciudad16(id=17,Nombre="MARTINIQUE"),
           ciudad16(id=18,Nombre="PUERTO RICO"),
           ciudad16(id=19,Nombre="TURKS AND CAICOS ISLANDS"),
           ciudad16(id=20,Nombre="TRINIDAD AND TOBAGO"),
           ciudad16(id=21,Nombre="SAINT VINCENT AND THE GRENADINES"),
           ciudad16(id=22,Nombre="VIRGIN ISLAND BRITISH"),
           ciudad16(id=23,Nombre="VIRGIN ISLANDS US")
  ]

@router.get("/caribbean/")
async def imprimir():
    return (ciu_list16)

@router.get("/caribbean/{id}")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, ciu_list16)  #Función de orden superior
    try:
        return ciu_list16(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}

@router.get("/caribbean/")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, ciu_list16)  #Función de orden superior
    try:
        return ciu_list16(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}


@router.post("/caribbean/")
async def usersclass(user:ciudad16):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list16):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            return {"error":"el usuario ya existe"}
    else:
        ciu_list16.append(user)
        return user
    
@router.put("/caribbean/")
async def usersclass(user:ciudad16):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list16):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           ciu_list16[index] = user  #accedemos al indice de la lista que hemos encontrado y actualizamos con el nuevo usuario
           found=True
           
    if not found:
        return {"error":"No se ha actualizado el usuario"}
    else:
        return user
    
@router.delete("/caribbean/{id}")
async def usersclass(id:int):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list16):
        if saved_user.id ==id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           del ciu_list16[index]  #Eliminamos al indice de la lista que hemos encontrado 
           found=True
           return "El registro se ha eliminado"
       
    if not found:
        return {"error":"No se ha eliminado el usuario"}












#-------------DEFINIENDO lqw ciudades de CENTRAL AMERICA
class ciudad17 (BaseModel):
    id:int
    Nombre:str


ciu_list17= [ciudad17(id=0,Nombre="BELIZE"),
           ciudad17(id=1,Nombre="COSTA RICA"),
           ciudad17(id=2,Nombre="GUATEMALA"),
           ciudad17(id=3,Nombre="HONDURAS"),
           ciudad17(id=4,Nombre="MEXICO"),
           ciudad17(id=5,Nombre="NICARAGUA"),
           ciudad17(id=6,Nombre="PANAMA"),
           ciudad17(id=7,Nombre="EL SALVADOR")
  ]

@router.get("/centralafrica/")
async def imprimir():
    return (ciu_list17)

@router.get("/centralafrica/{id}")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, ciu_list17)  #Función de orden superior
    try:
        return ciu_list17(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}

@router.get("/centralafrica/")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, ciu_list17)  #Función de orden superior
    try:
        return ciu_list17(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}


@router.post("/centralafrica/")
async def usersclass(user:ciudad17):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list17):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            return {"error":"el usuario ya existe"}
    else:
        ciu_list17.append(user)
        return user
    
@router.put("/centralafrica/")
async def usersclass(user:ciudad17):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list17):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           ciu_list17[index] = user  #accedemos al indice de la lista que hemos encontrado y actualizamos con el nuevo usuario
           found=True
           
    if not found:
        return {"error":"No se ha actualizado el usuario"}
    else:
        return user
    
@router.delete("/centralafrica/{id}")
async def usersclass(id:int):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list17):
        if saved_user.id ==id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           del ciu_list17[index]  #Eliminamos al indice de la lista que hemos encontrado 
           found=True
           return "El registro se ha eliminado"
       
    if not found:
        return {"error":"No se ha eliminado el usuario"}





#-------------------------DEFINIENDO lqw ciudades de NORTH AMERICA
class ciudad18 (BaseModel):
    id:int
    Nombre:str


ciu_list18= [ciudad18(id=0,Nombre="BERMUDA"),
           ciudad18(id=1,Nombre="CANADA"),
           ciudad18(id=2,Nombre="GREENLAND"),
           ciudad18(id=3,Nombre="SAINT PIERRE AND MIQUELON"),
           ciudad18(id=4,Nombre="UNITED STATES")
  ]

@router.get("/northamerica/")
async def imprimir():
    return (ciu_list18)

@router.get("/northamerica/{id}")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, ciu_list18)  #Función de orden superior
    try:
        return ciu_list18(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}

@router.get("/northamerica/")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, ciu_list18)  #Función de orden superior
    try:
        return ciu_list18(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}


@router.post("/northamerica/")
async def usersclass(user:ciudad18):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list18):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            return {"error":"el usuario ya existe"}
    else:
        ciu_list18.append(user)
        return user
    
@router.put("/northamerica/")
async def usersclass(user:ciudad18):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list18):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           ciu_list18[index] = user  #accedemos al indice de la lista que hemos encontrado y actualizamos con el nuevo usuario
           found=True
           
    if not found:
        return {"error":"No se ha actualizado el usuario"}
    else:
        return user
    
@router.delete("/northamerica/{id}")
async def usersclass(id:int):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list18):
        if saved_user.id ==id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           del ciu_list18[index]  #Eliminamos al indice de la lista que hemos encontrado 
           found=True
           return "El registro se ha eliminado"
       
    if not found:
        return {"error":"No se ha eliminado el usuario"}






#-------------------------DEFINIENDO lqw ciudades de Australia and New Zealand
class ciudad19 (BaseModel):
    id:int
    Nombre:str


ciu_list19= [ciudad19(id=0,Nombre="AUSTRALIA"),
           ciudad19(id=1,Nombre="COCOS"),
           ciudad19(id=2,Nombre="CHRISTMAS ISLAND"),
           ciudad19(id=3,Nombre="NORFOLK ISLAND"),
           ciudad19(id=4,Nombre="NEW ZELAND")
  ]

@router.get("/australiaandnewzealand/")
async def imprimir():
    return (ciu_list19)
@router.get("/australiaandnewzealand/{id}")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, ciu_list19)  #Función de orden superior
    try:
        return ciu_list19(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}

@router.get("/australiaandnewzealand/")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, ciu_list19)  #Función de orden superior
    try:
        return ciu_list19(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}


@router.post("/australiaandnewzealand/")
async def usersclass(user:ciudad19):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list19):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            return {"error":"el usuario ya existe"}
    else:
        ciu_list19.append(user)
        return user
    
@router.put("/australiaandnewzealand/")
async def usersclass(user:ciudad19):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list19):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           ciu_list19[index] = user  #accedemos al indice de la lista que hemos encontrado y actualizamos con el nuevo usuario
           found=True
           
    if not found:
        return {"error":"No se ha actualizado el usuario"}
    else:
        return user
    
@router.delete("/australiaandnewzealand/{id}")
async def usersclass(id:int):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list19):
        if saved_user.id ==id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           del ciu_list19[index]  #Eliminamos al indice de la lista que hemos encontrado 
           found=True
           return "El registro se ha eliminado"
       
    if not found:
        return {"error":"No se ha eliminado el usuario"}







#--------------------------DEFINIENDO lqw ciudades de MELANESIA
class ciudad20 (BaseModel):
    id:int
    Nombre:str


ciu_list20= [ciudad20(id=0,Nombre="FIJI ISLANDS"),
           ciudad20(id=1,Nombre="NEW CALEDONIA"),
           ciudad20(id=2,Nombre="PAPUA NEW GUINEA"),
           ciudad20(id=3,Nombre="SOLOMON ISLANDS"),
           ciudad20(id=4,Nombre="VANUATU")
  ]

@router.get("/melanesia/")
async def imprimir():
    return (ciu_list20)
@router.get("/melanesia/{id}")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, ciu_list20)  #Función de orden superior
    try:
        return ciu_list20(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}

@router.get("/melanesia/")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, ciu_list20)  #Función de orden superior
    try:
        return ciu_list20(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}


@router.post("/melanesia/")
async def usersclass(user:ciudad):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list20):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            return {"error":"el usuario ya existe"}
    else:
        ciu_list20.append(user)
        return user
    
@router.put("/melanesia/")
async def usersclass(user:ciudad20):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list20):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           ciu_list20[index] = user  #accedemos al indice de la lista que hemos encontrado y actualizamos con el nuevo usuario
           found=True
           
    if not found:
        return {"error":"No se ha actualizado el usuario"}
    else:
        return user
    
@router.delete("/melanesia/{id}")
async def usersclass(id:int):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list20):
        if saved_user.id ==id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           del ciu_list20[index]  #Eliminamos al indice de la lista que hemos encontrado 
           found=True
           return "El registro se ha eliminado"
       
    if not found:
        return {"error":"No se ha eliminado el usuario"}





#---------------------------------DEFINIENDO lqw ciudades de MICRONESIA
class ciudad21 (BaseModel):
    id:int
    Nombre:str


ciu_list21= [ciudad21(id=0,Nombre="MICRONESIA FEDERATED STATES OF"),
           ciudad21(id=1,Nombre="GUAM"),
           ciudad21(id=2,Nombre="KIRIBATI"),
           ciudad21(id=3,Nombre="MARSHALL ISLANDS"),
           ciudad21(id=4,Nombre="NORTHERN MARIANA ISLANDS"),
           ciudad21(id=5,Nombre="NAURU"),
           ciudad21(id=6,Nombre="PALAU")
  ]

@router.get("/micronesia/")
async def imprimir():
    return (ciu_list21)

@router.get("/micronesia/{id}")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, ciu_list21)  #Función de orden superior
    try:
        return ciu_list21(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}

@router.get("/micronesia/")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, ciu_list21)  #Función de orden superior
    try:
        return ciu_list21(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}


@router.post("/micronesia/")
async def usersclass(user:ciudad21):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list21):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            return {"error":"el usuario ya existe"}
    else:
        ciu_list.append(user)
        return user
    
@router.put("/micronesia/")
async def usersclass(user:ciudad21):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list21):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           ciu_list21[index] = user  #accedemos al indice de la lista que hemos encontrado y actualizamos con el nuevo usuario
           found=True
           
    if not found:
        return {"error":"No se ha actualizado el usuario"}
    else:
        return user
    
@router.delete("/micronesia/{id}")
async def usersclass(id:int):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list21):
        if saved_user.id ==id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           del ciu_list21[index]  #Eliminamos al indice de la lista que hemos encontrado 
           found=True
           return "El registro se ha eliminado"
       
    if not found:
        return {"error":"No se ha eliminado el usuario"}






#-------------------------DEFINIENDO lqw ciudades de POLINESIA
class ciudad22 (BaseModel):
    id:int
    Nombre:str


ciu_list22= [ciudad22(id=0,Nombre="AMERICAN SAMOA"),
           ciudad22(id=1,Nombre="COOK ISLANDS"),
           ciudad22(id=2,Nombre="NIUE"),
           ciudad22(id=3,Nombre="PITCAIRN"),
           ciudad22(id=4,Nombre="FRANCH POLYNESIA"),
           ciudad22(id=5,Nombre="TOKELAU"),
           ciudad22(id=6,Nombre="TONGA"),
           ciudad22(id=7,Nombre="TUVALU"),
           ciudad22(id=8,Nombre="WALLIS AND FUTUNA"),
           ciudad22(id=9,Nombre="SAMOA")
           
       ]

@router.get("/polynesia/")
async def imprimir():
    return (ciu_list22)

@router.get("/polynesia/{id}")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, ciu_list22)  #Función de orden superior
    try:
        return ciu_list22(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}

@router.get("/polynesia/")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, ciu_list22)  #Función de orden superior
    try:
        return ciu_list22(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}


@router.post("/polynesia/")
async def usersclass(user:ciudad22):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list22):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            return {"error":"el usuario ya existe"}
    else:
        ciu_list.append(user)
        return user
    
@router.put("/polynesia/")
async def usersclass(user:ciudad22):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list22):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           ciu_list22[index] = user  #accedemos al indice de la lista que hemos encontrado y actualizamos con el nuevo usuario
           found=True
           
    if not found:
        return {"error":"No se ha actualizado el usuario"}
    else:
        return user
    
@router.delete("/polynesia/{id}")
async def usersclass(id:int):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list22):
        if saved_user.id ==id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           del ciu_list22[index]  #Eliminamos al indice de la lista que hemos encontrado 
           found=True
           return "El registro se ha eliminado"
       
    if not found:
        return {"error":"No se ha eliminado el usuario"}








#-----------------------------DEFINIENDO lqw ciudades de SOUTH AMERICA


class ciudad23 (BaseModel):
    id:int
    Nombre:str


ciu_list23= [ciudad23(id=0,Nombre="ARGENTINA"),
           ciudad23(id=1,Nombre="BOLIVIA"),
           ciudad23(id=2,Nombre="BRAZIL"),
           ciudad23(id=3,Nombre="CHILE"),
           ciudad23(id=4,Nombre="COLOMBIA"),
           ciudad23(id=5,Nombre="ECUADOR"),
           ciudad23(id=6,Nombre="FALKLAND ISLANDS"),
           ciudad23(id=7,Nombre="FRENCH GUIANA"),
           ciudad23(id=8,Nombre="GUYANA"),
           ciudad23(id=9,Nombre="PERU"),
           ciudad23(id=10,Nombre="PARAGUAY"),
           ciudad23(id=11,Nombre="SURINAME"),
           ciudad23(id=12,Nombre="URUGUAY"),
           ciudad23(id=13,Nombre="VENEZUELA")
           
       ]

@router.get("/southamerica/")
async def imprimir():
    return (ciu_list23)


@router.get("/southamerica/{id}")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, ciu_list23)  #Función de orden superior
    try:
        return ciu_list23(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}

@router.get("/southamerica/")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, ciu_list23)  #Función de orden superior
    try:
        return ciu_list23(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}


@router.post("/southamerica/")
async def usersclass(user:ciudad23):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list23):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            return {"error":"el usuario ya existe"}
    else:
        ciu_list23.append(user)
        return user
    
@router.put("/southamerica/")
async def usersclass(user:ciudad23):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list23):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           ciu_list23[index] = user  #accedemos al indice de la lista que hemos encontrado y actualizamos con el nuevo usuario
           found=True
           
    if not found:
        return {"error":"No se ha actualizado el usuario"}
    else:
        return user
    
@router.delete("/southamerica/{id}")
async def usersclass(id:int):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(ciu_list23):
        if saved_user.id ==id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           del ciu_list23[index]  #Eliminamos al indice de la lista que hemos encontrado 
           found=True
           return "El registro se ha eliminado"
       
    if not found:
        return {"error":"No se ha eliminado el usuario"}