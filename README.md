# Para nuestra api utilizaremos la combinación de Consistencia (C) y Disponibilidad (A).

Motivos:
Consistencia (C):
Integridad de Datos: Garantiza que toda la información de los tickets sea precisa y esté actualizada en todo momento, evitando conflictos como reservas duplicadas.
Operaciones Fiables: Asegura que las acciones de csrear, actualizar y eliminar tickets sean realizadas de manera correcta y completa.

Disponibilidad (A):
Acceso Continuo: La API está siempre disponible para que los usuarios realicen operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sin interrupciones.
Experiencia de Usuario: Proporciona una interacción fluida y confiable, esencial para mantener la satisfacción y confianza de los usuarios.