def validar_cadena(cadena, longitud_minima=5, longitud_maxima=50):
    longitud = len(cadena)
    if longitud_minima <= longitud <= longitud_maxima:
        return True
    else:
        return False

def validar_telefono(telefono):
    if len(telefono) == 10 and telefono.isdigit():
        return True
    else:
        return False

def registro_usuario(id_usuario):
    while True:
        nombre = input("Ingrese su nombre: ")
        if validar_cadena(nombre):
            break
        print("El nombre debe contener entre 5 y 50 caracteres.")
        
    while True:
        apellido = input("Ingrese su apellido: ")
        if validar_cadena(apellido):
            break
        print("El apellido debe contener entre 5 y 50 caracteres.")
        
    while True:
        telefono = input("Ingrese su número de teléfono: ")
        if validar_telefono(telefono):
            break
        print("El número de teléfono debe contener 10 dígitos.")
        
    while True:
        correo = input("Ingrese su correo electrónico: ")
        if validar_cadena(correo):
            break
        print("El correo electrónico debe contener entre 5 y 50 caracteres.")
            
    return {"id": id_usuario, "nombre": nombre, "apellido": apellido, "telefono": telefono, "correo": correo}

def bienvenida(usuario):
    print("Hola " + usuario['nombre'] + " " + usuario['apellido'] + ", tu ID de usuario es " + str(usuario['id']) + " y en breve recibirás un correo a " + usuario['correo'])

def registrar_usuarios():
    usuarios = []
    num_usuarios = int(input("¿Cuántos usuarios desea registrar? "))
    for i in range(num_usuarios):
        usuario = registro_usuario(i+1)
        usuarios.append(usuario)
        bienvenida(usuario)
    return usuarios

usuarios_registrados = registrar_usuarios()
for usuario in usuarios_registrados:
    print(f'ID: {usuario["id"]}, Nombre: {usuario["nombre"]}, Apellido: {usuario["apellido"]}, Telefono: {usuario["telefono"]}, Correo: {usuario["correo"]}')