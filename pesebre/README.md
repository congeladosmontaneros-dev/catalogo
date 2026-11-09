# 🎄 Pesebre interactivo · Congelados Montañeros

Un pesebre en la pantalla donde las personas **hablan con los personajes**: dicen "Hola Virgen María" y responde María; "Hola San José", y responde José. También hablan el Ángel y el Pastorcito (el único que recomienda productos de la tienda).

Hay **dos formas de usarlo** (se pueden combinar):

| Forma | Quién escucha y habla | Pantalla |
|---|---|---|
| **A. Con el kit LAFVIN (ESP32 + IA Xiaozhi)** | El ESP32 | La página en **modo fondo**: `.../pesebre/?modo=fondo` |
| **B. Solo con el PC** | El PC con micrófono y parlante | La página normal: `.../pesebre/` |

Para la forma A sigue **`personaje-xiaozhi.md`**.

## La imagen del pesebre

La escena es una ilustración generada con IA. Para que no dependa de internet:
1. Abre la imagen en tu cuenta de OpenArt (proyecto por defecto) y descárgala.
2. Guárdala en esta carpeta con el nombre **`escena.jpg`** y súbela al repositorio.

Si `escena.jpg` no existe, la página usa la imagen directamente desde OpenArt. La versión gratis trae marca de agua; para quitarla hay que descargarla desde un plan pago o usar otra imagen. **Cualquier foto o dibujo horizontal (16:9) guardado como `escena.jpg` sirve**, incluso una foto del pesebre real de la tienda.

## Qué se necesita

| Equipo | Para qué |
|---|---|
| PC o portátil con **Google Chrome** o **Microsoft Edge** | Muestra el pesebre, escucha y habla |
| Pantalla USB-C conectada al PC | Muestra el pesebre en grande |
| Micrófono (el del portátil sirve; mejor uno USB o de diadema) | Escuchar a las personas |
| Parlante o bafle | Que el Ángel se escuche en la tienda |
| Internet | El reconocimiento de voz de Chrome y la IA lo necesitan |
| Kit LAFVIN (opcional) | Un segundo personaje que habla por su cuenta (ver `personaje-xiaozhi.md`) |

## Cómo ponerlo a funcionar (5 minutos)

1. En el PC, abre Chrome y entra a:
   **https://congeladosmontaneros-dev.github.io/catalogo/pesebre/**
2. Arrastra la ventana a la pantalla USB-C y presiona **F** para ponerla en pantalla completa.
3. Toca **"Toca y habla"** (o la barra espaciadora). La primera vez Chrome pide permiso para usar el micrófono: dale **Permitir**.
4. Habla. Responde el personaje que saludaste, con texto y con voz. Cada personaje tiene un tono de voz distinto.

Sin configurar nada funciona en **modo básico**, con respuestas ya escritas sobre la novena, villancicos, horarios y pedidos.

## Activar la IA (para que responda cualquier pregunta)

1. Crea una cuenta en **console.anthropic.com**, carga saldo y crea una **clave de API** solo para el pesebre.
2. En esa misma consola, pon un **límite de gasto mensual** (por ejemplo USD 20) para que nunca haya sorpresas.
3. En la página del pesebre presiona **C** (o el engranaje ⚙ abajo a la izquierda) y pega la clave.
4. Escribe la **promoción del día** si hay una: el Ángel la anuncia.
5. Prueba la voz con el botón 🔊 y elige la que suene más natural. Las voces de Microsoft en Edge suelen sonar mejor.

**Seguridad de la clave:** la clave queda guardada **solo en ese computador**, no en GitHub. No la compartas ni la escribas en ningún archivo del repositorio. Si el PC se pierde o alguien la ve, bórrala en console.anthropic.com y crea otra.

## Atajos de teclado

| Tecla | Acción |
|---|---|
| Espacio | Hablar / dejar de escuchar / interrumpir al Ángel |
| C | Configuración |
| F | Pantalla completa |
| R | Empezar una conversación nueva |

La conversación también se reinicia sola cuando pasan 90 segundos sin preguntas, porque se asume que llegó otra persona.

## Consejos para la tienda

- Pon el micrófono **cerca de la pantalla y lejos del parlante** para que no se escuche a sí mismo.
- Un letrero al lado: **"¡Pregúntale al Ángel del Pesebre! 🎤 Toca el botón dorado"**.
- Del 16 al 24 de diciembre el Ángel sabe qué día de la novena es.
- Graba a los niños hablando con el Ángel (con permiso de los papás) para Instagram y Facebook.
- Actualiza la promo del día cada mañana con la tecla **C**.

## Fase 2: luces con el ESP32 (opcional)

En la configuración hay un campo **"IP del ESP32"**. Si se llena, la página le avisa al ESP32 cuando el Ángel escucha o habla:

```
http://<IP-del-ESP32>/estado?e=escuchando   (o pensando, hablando, listo)
```

Con eso un ESP32 puede prender la estrella o una tira LED mientras el Ángel habla. Para esto la página se abre **desde el PC** (descargando `pesebre/index.html`), porque GitHub Pages (https) no deja hablar con equipos de la red local (http).

## Actualizar productos y precios

La lista de productos que conoce el Ángel está dentro de `index.html`, en la constante `CATALOGO`. Cuando cambien precios en el catálogo principal, hay que actualizarla también.
