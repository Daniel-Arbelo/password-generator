import random
import string

def generar_contrasena(longitud=12, incluir_numeros=True, incluir_simbolos=True, incluir_mayusculas=True, excluir_caracteres=""):
    """
    Genera una contraseña segura con las opciones especificadas.
    
    :param longitud: Longitud de la contraseña (mínimo 4)
    :param incluir_numeros: Si debe incluir números
    :param incluir_simbolos: Si debe incluir símbolos
    :param incluir_mayusculas: Si debe incluir letras mayúsculas
    :param excluir_caracteres: Caracteres a excluir de la contraseña
    :return: Contraseña generada
    """
    caracteres = string.ascii_lowercase  # Letras minúsculas
    
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation
    
    # Excluir caracteres específicos si el usuario lo desea
    caracteres = ''.join(c for c in caracteres if c not in excluir_caracteres)
    
    if not caracteres:
        raise ValueError("Debe incluir al menos un tipo de caracter.")
    
    return ''.join(random.choice(caracteres) for _ in range(longitud))

def main():
    """
    Función principal que maneja la interacción con el usuario.
    """
    print("\n==============================")
    print("  Generador de Contraseñas Seguras")
    print("==============================\n")
    
    try:
        longitud = int(input("Longitud de la contraseña (mínimo 4): "))
        if longitud < 4:
            raise ValueError("La longitud debe ser al menos 4 caracteres.")
        
        incluir_numeros = input("¿Incluir números? (s/n): ").strip().lower() == 's'
        incluir_simbolos = input("¿Incluir símbolos? (s/n): ").strip().lower() == 's'
        incluir_mayusculas = input("¿Incluir mayúsculas? (s/n): ").strip().lower() == 's'
        excluir_caracteres = input("Ingrese caracteres a excluir (opcional): ").strip()
        
        contrasena = generar_contrasena(longitud, incluir_numeros, incluir_simbolos, incluir_mayusculas, excluir_caracteres)
        print(f"\nContraseña generada: {contrasena}\n")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
