#Cortázar Tinajero Luis Enrique.

# Función para obtener el inverso modular de "a" módulo "m"
# Usamos un ciclo sencillo ya que m=26 es pequeño.
def mod_inverse(a, m):
    # Nos aseguramos de trabajar con a en módulo m
    a = a % m
    # Probamos todos los posibles valores entre 1 y m-1
    for x in range(1, m):
        # Si encontramos un x tal que (a * x) mod m sea 1, se encontró el inverso
        if (a * x) % m == 1:
            return x
    # Si no se encuentra ningún inverso, lanzamos un error (esto no sucede si a y m son coprimos)
    raise ValueError("El inverso modular no existe.")

# Función que convierte un texto en una lista de números
def text_to_numbers(text):
    # Convertimos el texto a mayúsculas y eliminamos espacios para trabajar solo con letras
    text = text.upper().replace(" ", "")
    # Convertimos cada letra a su valor numérico (ord('A') es 65; A→0, B→1, etc.)
    numbers = [ord(char) - 65 for char in text if char.isalpha()]
    return numbers

# Función que convierte una lista de números de vuelta a texto
def numbers_to_text(numbers):
    # Cada número lo convertimos en una letra sumándole 65 y usando chr()
    text = "".join(chr(num + 65) for num in numbers)
    return text

# Función para cifrar un mensaje usando el cifrado de Hill con una matriz clave dada
def hill_encrypt(message, key):
    # Convertimos el mensaje a una lista de números
    nums = text_to_numbers(message)
    # Determinamos el tamaño de bloque, que es la dimensión (n) de la matriz clave
    n = len(key)
    # Si el mensaje no es múltiplo de n, se agrega relleno con 'X' (23 correspondiente a X)
    if len(nums) % n != 0:
        padding = n - (len(nums) % n)  # número de caracteres de relleno necesarios
        nums.extend([23] * padding)     # 23 es el valor de 'X'

    cipher_numbers = []  # Lista donde almacenaremos los números cifrados

    # Procesamos el mensaje en bloques del tamaño de la matriz clave
    for i in range(0, len(nums), n):
        block = nums[i:i+n]  # Extraemos un bloque de n números
        cipher_block = []    # Lista para guardar el bloque cifrado resultante
        # Realizamos la multiplicación del bloque por la matriz clave
        for row in key:
            # Para cada fila de la matriz, calculamos el resultado de la multiplicación
            value = sum([row[j] * block[j] for j in range(n)]) % 26
            cipher_block.append(value)
        # Añadimos el bloque cifrado a la lista general
        cipher_numbers.extend(cipher_block)

    # Convertimos los números cifrados de vuelta a texto y lo retornamos
    cipher_text = numbers_to_text(cipher_numbers)
    return cipher_text

# Función para obtener la inversa modular de una matriz 2x2 bajo módulo m
def matrix_mod_inv(matrix, m):
    # Para una matriz [[a, b], [c, d]]:
    # Su determinante es: det = a*d - b*c (tomado módulo m)
    a, b = matrix[0]
    c, d = matrix[1]
    det = (a * d - b * c) % m
    # Se obtiene el inverso modular del determinante
    inv_det = mod_inverse(det, m)
    # Se calcula la matriz adjunta y se multiplica por el inverso del determinante
    inv_matrix = [
        [(d * inv_det) % m, (-b * inv_det) % m],
        [(-c * inv_det) % m, (a * inv_det) % m]
    ]
    return inv_matrix

# Función para descifrar un mensaje cifrado con el cifrado de Hill
def hill_decrypt(cipher_text, key):
    # Calculamos la matriz inversa de la clave
    inv_key = matrix_mod_inv(key, 26)
    # Convertimos el texto cifrado a una lista de números
    nums = text_to_numbers(cipher_text)
    decrypted_numbers = []  # Lista para almacenar el bloque descifrado
    n = len(key)          # Tamaño de bloque (dimensión de la matriz clave)

    # Procesamos el mensaje cifrado en bloques de tamaño n
    for i in range(0, len(nums), n):
        block = nums[i:i+n]  # Extraemos el bloque cifrado
        plain_block = []     # Lista para el bloque descifrado
        # Multiplicamos el bloque por la matriz inversa de la clave
        for row in inv_key:
            value = sum([row[j] * block[j] for j in range(n)]) % 26
            plain_block.append(value)
        # Añadimos el bloque descifrado a la lista general
        decrypted_numbers.extend(plain_block)

    # Convertimos los números descifrados de vuelta a texto
    plain_text = numbers_to_text(decrypted_numbers)
    return plain_text

# Bloque principal para probar la función de cifrado y descifrado
if __name__ == "__main__":
    # Definimos la matriz clave 2x2 (debe ser invertible en Z26)
    key = [
        [3, 3],
        [2, 5]
    ]

    # Mensaje original que se va a cifrar
    mensaje = "Aylin"
    print("Mensaje original:", mensaje)

    # Cifrado del mensaje usando el algoritmo de Hill
    mensaje_cifrado = hill_encrypt(mensaje, key)
    print("Mensaje cifrado: ", mensaje_cifrado)

    # Descifrado del mensaje cifrado utilizando la matriz inversa de la clave
    mensaje_descifrado = hill_decrypt(mensaje_cifrado, key)
    print("Mensaje descifrado:", mensaje_descifrado)

