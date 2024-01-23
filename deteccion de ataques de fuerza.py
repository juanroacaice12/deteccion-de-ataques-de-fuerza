import time #importamos el modulo de time para las marcas de tiempo 

class DetectorAtaquesFuerza:    #una clase para contener la logica de los ataques de fuerza 
    def __init__(self):
        self.intentos = {}
        self.limite_intentos = 5    #las variables que se utilizarán para rastrear los intentos de inicio de sesión y las características del sistema de detección.
        self.bloqueo_temporal = 60  
        self.lista_negra = set()

    def registrar_intento(self, ip, usuario):
        now = time.time()
        if ip in self.intentos:
            self.intentos[ip].append(now)    # registra cada intento de inicio de sesión junto con la marca de tiempo en el diccionario 
        else:
            self.intentos[ip] = [now]

    def verificar_bloqueo_temporal(self, ip):   #verifica si la IP está en la lista negra o si ha superado el límite de intentos en un período de tiempo reciente.
        if ip in self.lista_negra:
            return True
        if ip in self.intentos:
            intentos_recientes = [t for t in self.intentos[ip] if time.time() - t < self.bloqueo_temporal]
            if len(intentos_recientes) >= self.limite_intentos:
                self.lista_negra.add(ip)
                return True
        return False

    def verificar_intento_exitoso(self, ip):
        if ip in self.intentos:    #elimina los registros de intentos exitosos para una IP específica
            del self.intentos[ip]

    def detectar_ataque(self, ip, usuario, contrasena):
        if self.verificar_bloqueo_temporal(ip): 
            print(f"¡Ataque detectado! IP {ip} bloqueada temporalmente.")  
            return False
        else:
            self.registrar_intento(ip, usuario)

            contrasena_correcta = "javier13"      #verifica si la IP está bloqueada temporalmente. Si no lo está, registra el intento y verifica la contraseña
            if contrasena == contrasena_correcta:
                self.verificar_intento_exitoso(ip)
                print("Inicio de sesión exitoso.")
                return True
            else:
                if len(self.intentos[ip]) >= self.limite_intentos:
                    print("¡Ataque de fuerza bruta detectado!")
                else:
                    print("Contraseña incorrecta.")
                return False


#Creamos una instancia del detector y simulamos 5 intentos fallidos con la contraseña incorrecta, seguidos por un intento exitoso con la contraseña correcta
detector = DetectorAtaquesFuerza()

ip_usuario = "192.168.1.1"
nombre_usuario = "usuario123"

for _ in range(5):                                   
    contrasena_ingresada = input("Ingresa tu contraseña: ")
    detector.detectar_ataque(ip_usuario, nombre_usuario, contrasena_ingresada)

contrasena_ingresada = input("Ingresa tu contraseña: ")
detector.detectar_ataque(ip_usuario, nombre_usuario, contrasena_ingresada)

