# Deteccion de ataques de fuerza
Deteccion de ataques de fuerza.

El detector de ataques de fuerza bruta en un sistema de inicio de sesión. La clase DetectorAtaquesFuerza utiliza un diccionario para rastrear intentos de inicio de sesión por dirección IP, con la capacidad de bloquear temporalmente una IP si excede un límite de intentos en un período. Además, se mantiene una lista negra para IPs bloqueadas. El método detectar_ataque verifica si la IP está bloqueada temporalmente, registra intentos y verifica contraseñas. En caso de éxito, elimina los registros de intentos exitosos; de lo contrario, detecta un ataque de fuerza bruta si se supera el límite de intentos. La simulación incluye 5 intentos fallidos seguidos de un intento exitoso con la contraseña correcta
