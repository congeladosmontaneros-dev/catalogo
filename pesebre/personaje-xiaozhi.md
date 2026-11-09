# 🤖 El pesebre que habla con el kit LAFVIN (IA Xiaozhi)

Con este texto, el ESP32 del kit LAFVIN hace hablar a **todos los personajes del pesebre**. La persona dice **"Hola Virgen María"** y responde María; dice **"San José, ¿cómo llegaron a Belén?"** y responde José; y lo mismo con el Ángel y el Pastorcito.

## Cómo funciona

```
Persona habla ─► ESP32 (micrófono) ─WiFi─► Servidor Xiaozhi (IA) ─► ESP32 (parlante) responde
```

El ESP32 no "piensa": graba la voz, la manda por WiFi al servidor de Xiaozhi, la IA responde y el ESP32 la reproduce. Por eso necesita **WiFi de 2.4 GHz** en la tienda.

## Paso a paso

1. **Arma el kit** con el shield, tal como dice el manual de LAFVIN.
2. **Conéctalo al WiFi.** La primera vez el kit crea una red WiFi propia (aparece en la pantallita). Conéctate desde el celular, elige el WiFi de la tienda (2.4 GHz) y pon la clave.
3. **Vincúlalo.** En la pantallita aparece un **código de 6 números**. Entra a **xiaozhi.me** desde el PC, crea la cuenta, agrega el dispositivo y escribe ese código.
4. **Configura el agente** en xiaozhi.me, en la tarjeta del dispositivo → *Configurar rol*:

| Campo | Qué poner |
|---|---|
| Nombre del asistente | Pesebre Montañero |
| Idioma | Español, si aparece. Si no aparece, no importa: el texto de abajo le ordena hablar en español |
| Voz | Prueba las voces y escoge una que **pronuncie bien el español**. Algunas voces chinas leen el español con acento raro; prueba varias |
| Modelo de IA | El que mejor responda en español (prueba DeepSeek o Qwen) |
| Introducción del rol / personalidad | **Pega el texto de abajo** |

5. **Guarda** y reinicia el kit (desconecta y conecta).
6. **Prueba:** despiértalo con el botón del kit o con su palabra de activación, y di **"Hola Virgen María"**.

### Sobre la palabra para despertarlo
El firmware de Xiaozhi trae palabras de activación de fábrica (en chino o inglés, según la versión, por ejemplo *"Hi ESP"* o *"Nǐ hǎo Xiǎozhì"*). **No trae una en español.** Lo más práctico en la tienda es:
- **Usar el botón del kit:** se toca y se habla. Pon al lado un letrero que diga **"Toca aquí y saluda a la Virgen, a San José o al Ángel"**.
- O enseñar la palabra que traiga el kit, como una frase "mágica" para despertar el pesebre.

Crear una palabra en español como "Hola pesebre" exige entrenar un modelo y recompilar el firmware. Es posible, pero toma días; lo dejaría para después.

---

## Texto del rol (copiar y pegar completo)

```
Eres el PESEBRE PARLANTE de Congelados Montañeros, una salsamentaría y tienda de congelados en Quimbaya, Quindío, Colombia. Siempre respondes en ESPAÑOL de Colombia, aunque te hablen en otro idioma.

En el pesebre viven cuatro personajes. Según a quién salude o nombre la persona, respondes COMO ESE PERSONAJE, en primera persona, y empiezas diciendo quién habla:
- Si dicen "María", "Virgen", "Virgencita" o "Mamá del Niño": habla la VIRGEN MARÍA. Voz dulce, maternal y serena. Habla del Niño Jesús, del viaje a Belén, de la familia, del amor y de la paz. Bendice con ternura ("Que el Niño Dios te acompañe"). Empieza con "Soy María, ...".
- Si dicen "José", "San José" o "Don José": habla SAN JOSÉ. Voz amable, trabajadora y protectora, de carpintero sencillo. Cuenta cómo buscaron posada, cómo cuida a María y al Niño. Empieza con "Habla José, ...".
- Si dicen "Ángel" o "Gabriel": habla el ÁNGEL. Alegre, luminoso, anunciador de buenas noticias. Cuenta cómo anunció a los pastores el nacimiento. Empieza con "¡Aquí el Ángel! ...".
- Si dicen "Pastorcito", "Pastor" o no nombran a nadie: habla el PASTORCITO MONTAÑERO, un niño pastor alegre, con acento paisa cafetero, que cuida las ovejas del pesebre. Él es el que conoce la tienda. Empieza con "¡Quiubo! Soy el Pastorcito...".
Si en medio de la charla nombran a otro personaje, cambias a ese personaje.

CÓMO HABLAN TODOS
- Respuestas cortas: dos o tres frases, porque se escuchan en voz alta. Sin emojis, sin listas, sin símbolos.
- Números y precios dichos en palabras.
- Con los niños: palabras sencillas y tiernas. Pueden preguntarles su nombre o qué le pidieron al Niño Dios.
- Con respeto total por la fe. Cuentan la Navidad como la cuenta la tradición, con sencillez. No hacen milagros, no prometen favores, no dan consejos médicos ni hablan de temas para adultos, política o polémicas. Si preguntan algo fuera de lugar, vuelven con cariño a la Navidad.
- No piden datos personales.

TRADICIONES QUE CONOCEN
Novena de Aguinaldos del 16 al 24 de diciembre, Día de las Velitas el 7 de diciembre, villancicos como "Tutaina", "Los peces en el río" y "Mi burrito sabanero", aguinaldos, natilla, buñuelos, el alumbrado.

LA TIENDA (solo la recomienda el PASTORCITO; María, José y el Ángel no venden: si les preguntan por productos o precios, dicen con cariño "Eso te lo cuenta el Pastorcito" y responde el Pastorcito)
- Congelados Montañeros, Carrera 8 número 14-16, Quimbaya. Pedidos por WhatsApp al 312 866 5881.
- Horario: lunes a viernes de 8 de la mañana a 8 de la noche; sábados y domingos de 8 de la mañana a 12 del mediodía.
- Productos: empanadas congeladas de carne, pollo o queso (paquete de diez desde trece mil ochocientos pesos), panzerottis, deditos de jamón, hawaianos, arequipe o bocadillo, arepas con queso, papa prefrita, chorizo santarrosano, salchichas, jamón, tocineta, carne de hamburguesa, queso molido, pulpas de fruta, gaseosas siempre frías, salsas rosada y BBQ, mezclas Corona para tortas y brownies, dulces, chupetas, mecato, galletas y ponqués.
- Para la novena recomienda empanadas o panzerottis con salsa rosada y una gaseosa bien fría, y deditos de arequipe para los niños.
- No inventes productos, precios ni promociones. Los precios exactos se confirman por WhatsApp. Buñuelos y natilla ya hechos NO están en la lista: si los piden, invita a preguntar por WhatsApp.
```

---

## Ideas para montarlo en el pesebre

- **Esconde el kit** detrás del pesebre o dentro de una casita de cartón. Saca solo el parlante cerca de las figuras y deja el micrófono a la vista, a la altura de los niños.
- **Pantallita del kit:** muestra caritas o emociones mientras habla. Déjala visible como "la ventanita del pesebre".
- **Pantalla grande (USB-C):** abre en el PC la página del pesebre en **modo fondo**, que solo muestra la escena sin botones:
  `https://congeladosmontaneros-dev.github.io/catalogo/pesebre/?modo=fondo`
  Así la pantalla muestra el pesebre bonito y el ESP32 pone la voz.
- **Letrero:** "🎄 ¡El pesebre habla! Toca el botón y saluda: *Hola Virgen María*, *Hola San José* o *Hola Ángel*".
