## Pasos para ejecutar la aplicación:

1. **Clona el repositorio**:

   ```bash
   git clone https://github.com/tu_usuario/final_tickets.git
   cd final_tickets
   ```

2. **Configura la base de datos**:

   Abre el archivo `.env` en la raíz del proyecto y ajusta los parámetros de conexión a la base de datos según sea necesario.

3. **Ejecuta Docker Compose**:

   Para levantar los contenedores necesarios para la aplicación, ejecuta el siguiente comando:

   ```bash
   docker-compose up --build
   ```

   Este comando construirá y ejecutará los contenedores definidos en el archivo `docker-compose.yml`.
