# Generador de Contraseñas Seguras

Este es un generador de contraseñas seguras en Python que permite personalizar la contraseña a crear, con opciones para incluir o excluir tipos de caracteres como números, símbolos, y mayúsculas. El generador asegura contraseñas robustas de acuerdo con las preferencias del usuario.

## Características

- **Longitud personalizada**: El usuario puede elegir la longitud de la contraseña, con un mínimo de 4 caracteres.
- **Tipos de caracteres**: El usuario puede decidir incluir:
  - Letras minúsculas
  - Letras mayúsculas
  - Números
  - Símbolos
- **Exclusión de caracteres**: Es posible excluir caracteres específicos de la contraseña.
- **Interacción sencilla**: El usuario responde a las preguntas en la terminal para generar la contraseña.

## Requisitos

Este código está escrito en Python 3. Para ejecutarlo, necesitas tener Python instalado en tu máquina. Además, se utilizan las siguientes bibliotecas estándar de Python:

- `random`
- `string`

Estas bibliotecas vienen preinstaladas con Python, por lo que no es necesario instalar dependencias adicionales.

## Uso

1. **Clonar o descargar el repositorio**:
   Si tienes Git instalado, puedes clonar el repositorio con el siguiente comando:
   
   ```bash
   git clone git@github.com:Daniel-Arbelo/password-generator.git

2. **Ejecutar el script**:
   Abre una terminal y navega al directorio donde se encuentra el archivo `generador_contrasenas.py`. Luego, ejecuta el siguiente comando para iniciar el generador:

   ```bash
   python generador_contrasenas.py

3. **Responde a las preguntas**:
   El programa te pedirá las siguientes opciones:
   - Longitud de la contraseña (mínimo 4 caracteres).
   - Si deseas incluir números, símbolos y mayúsculas.
   - Caracteres que quieres excluir de la contraseña.

4. **Contraseña generada**:
   Después de responder a las preguntas, el generador mostrará la contraseña segura que cumple con los requisitos establecidos.

## Ejemplo de ejecución

```bash
==============================
  Generador de Contraseñas Seguras
==============================

Longitud de la contraseña (mínimo 4): 12
¿Incluir números? (s/n): s
¿Incluir símbolos? (s/n): s
¿Incluir mayúsculas? (s/n): s
Ingrese caracteres a excluir (opcional): o0

Contraseña generada: R9*GhF#l2Pf
```
## Función de las partes del código

1. **`generar_contrasena`**:
   Esta función genera una contraseña aleatoria con base en las opciones proporcionadas por el usuario. Acepta parámetros como la longitud de la contraseña, si incluir números, símbolos y mayúsculas, y si se deben excluir ciertos caracteres.

2. **`main`**:
   La función principal interactúa con el usuario y solicita las configuraciones necesarias para generar la contraseña. Luego llama a la función `generar_contrasena` para crear la contraseña y mostrarla.

## Manejo de errores

Si el usuario ingresa una longitud de contraseña menor a 4 o responde con valores no válidos, el programa capturará el error y lo informará de manera amigable.

## Contribuciones

Si deseas mejorar este proyecto o agregar nuevas funcionalidades, puedes hacer un **fork** del repositorio y enviar un **pull request** con tus cambios.

## Licencia

Este proyecto está bajo la licencia **MIT**. Esto permite que cualquier persona pueda usar, modificar y distribuir el código de manera libre, siempre y cuando se incluya el aviso de la licencia original.
