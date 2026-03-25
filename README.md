# ⚔️ Terminal Souls

Simulador de combate por turnos en consola desarrollado en Python. En este juego, controlas a un Héroe que debe enfrentarse a un Enemigo utilizando diferentes acciones estratégicas hasta que uno de los dos quede sin vida.

---

## 📌 Características

* Sistema de combate por turnos
* Daño aleatorio en cada ataque
* Sistema de curación con pociones limitadas
* Habilidad especial con probabilidad de fallo
* Validación de acciones del usuario
* Mensajes claros en consola

---

## 🧠 Mecánicas del Juego

### 🧍 Héroe

* **HP inicial:** 100
* **Pociones:** 3

### 👹 Enemigo

* **HP inicial:** 120

---

## 🎮 Acciones del Jugador

1. **Atacar**

   * Daño entre 10 y 25

2. **Curar**

   * Recupera 20 HP
   * Consume 1 poción

3. **Habilidad Especial**

   * Daño entre 30 y 50
   * 50% de probabilidad de fallar

---

## ⚔️ Turno del Enemigo

* Ataca automáticamente después del turno del jugador
* Daño entre 15 y 20

---

## 🔄 Flujo del Juego

1. Se muestra el estado actual (HP del héroe y enemigo)
2. El jugador elige una acción
3. Se ejecuta la acción
4. El enemigo ataca
5. Se verifica si alguien ha muerto
6. El ciclo continúa hasta que uno pierda

---

## 🛠️ Requisitos

* Python 3.x

---

## ▶️ Cómo ejecutar

1. Clona o descarga este repositorio
2. Abre una terminal en la carpeta del proyecto
3. Ejecuta el archivo:

```bash
python python3 main.py
```

---

## 💡 Ejemplo de uso

```
⚔️ ¡Bienvenido a Terminal Souls! ⚔️

--- ESTADO ACTUAL ---
Héroe: 100 HP
Enemigo: 120 HP

Elige una acción:
1. Atacar
2. Curar
3. Habilidad Especial
Opción: 1

¡Atacaste e hiciste 18 de daño!
El enemigo te atacó e hizo 17 de daño.
```

---

## 📚 Funciones principales

* `generar_daño(min, max)` → Genera daño aleatorio
* `mostrar_estado()` → Muestra la vida actual
* `turno_jugador()` → Maneja la acción del jugador
* `turno_enemigo()` → Ejecuta el ataque enemigo
* `verificar_ganador()` → Determina si el juego termina

---

## 🚀 Posibles mejoras

* Barra de vida visual `[#####-----]`
* Sistema de golpes críticos
* Elección de nombre del jugador
* Diferentes tipos de enemigos
* Sistema de niveles

---

## 👨‍💻 Autor

Andres Garay

---

