# INSTALACIÓN DE LIBRERIA DE OPENAI
A través del comando pip se hace la instalación de la librería de OPEN AI
```bash
pip install openai
```

# ENTRADA DE USUARIO
Se utilizo la funcion input para obtener el prompt de entrada del usuario y asignarlo a una variable

```python
prompt = input("Hola, soy ChatGPT, ¿En que te puedo ayudar? :) : ")
```

# SOLICITUD ENVIADA AL CLIENTE

Se utiliza la siguiente función para brindar la solicitud a la API con el prompt de entrada

```python
completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "user", "content": prompt}
    ]
)
```
# MANEJO DE RESPUESTA
Se obtiene la respuesta de parte del cliente por medio del siguiente metodo y mediante esa línea se obtene la respuetsa en consola.
```python
print("CHAT GPT: ", completion.choices[0].message.content)
```
```python
PS C:\Users\USER\Desktop\OPENAI PYTHON> python index.py
Hola, soy ChatGPT, ¿En que te puedo ayudar? :) : Dame 3 sabores de pizza
CHAT GPT:  Claro, aquí tienes tres sabores populares de pizza:

1. **Pizza Margherita**: Con salsa de tomate, mozzarella fresca y hojas de albahaca.
2. **Pizza Pepperoni**: Con salsa de tomate, mozzarella y rodajas de pepperoni.
3. **Pizza Hawaiana**: Con salsa de tomate, mozzarella, jamón y trozos de piña.

¡Espero que encuentres alguno de estos a tu gusto!
```
# SEGURIDAD PARA MANEJAR API Y DATOS SENSIBLES
Para manejar la seguridad de la API y los datos sensibles 