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
Para manejar la seguridad de la API y los datos sensibles, se almacena la API KEY en una variable de entorno directamente en el computador, y el sistema al ejecutar el archivo, se setea y toman la información almacenada de la API que esta almacenada globalmente en el equipo. 

# APLICACIONES EN CONTEXTO DE MARKETING
En este contexto, se puede tomar como ejemplo, la publicidad por redes sociales, para consultarle a la API por medio del prompt el siguiente ejemplo:

- Publicidad en poblaciones femeninas entre los 20-30 años

![alt text](image.png)

```python
PS C:\Users\USER\Desktop\OPENAI PYTHON> python index.py
Hola, soy ChatGPT, ¿En que te puedo ayudar? :) : ¿Que recetas quieren ver las mujeres entre 20-30 años en redes sociales?
CHAT GPT:  Las mujeres entre 20-30 años suelen buscar recetas que sean prácticas, saludables y a menudo inspiradas en tendencias actuales. Algunas de las recetas que podrían interesarles son:

1. **Platos saludables y rápidos**: Ensaladas nutritivas con ingredientes frescos, buddha bowls, o wraps de vegetales.

2. **Recetas de desayuno energizante**: Tostadas de aguacate con toppings creativos, batidos verdes, y bowls de açai.

3. **Cocina internacional**: Recetas de tacos al estilo de comida callejera, sushi fácil de preparar en casa, o curry tailandés.

4. **Postres saludables**: Brownies de batata, galletas de avena y plátano, o helado de frutas casero sin azúcar añadido.

5. **Alternativas vegetarianas o veganas**: Hamburguesas de legumbres, lasañas de berenjena, o "nuggets" de coliflor.

6. **Comidas para meal prep**: Recomendaciones para preparar comidas en cantidad y establecer menús saludables para la semana.

7. **Recetas con ingredientes de temporada**: Platillos que destacan ingredientes frescos y de temporada, como calabaza en otoño o espárragos en primavera.

8. **Platos inspirados en tendencias de alimentación consciente**: Recetas que incorporan alimentos funcionales como el matcha, cúrcuma o aceites esenciales.

9. **Cocina sostenible**: Recetas que aprovechan al máximo los ingredientes y minimizan el desperdicio de alimentos.

10. **Recetas de "comida reconfortante" con un giro saludable**: Versiones ligeras de pizza, pasta o sopa.

Las redes sociales son una plataforma potente para descubrir y compartir contenido inspirador, y las recetas que son visualmente atractivas o fáciles de personalizar suelen tener un gran atractivo.

```
