#Solución Taller SOLID Race Lab

Ingeniería de Software II — Universidad Nacional de Colombia (2026-2)
Santiago Cardenas Rodriguez

Este repositorio contiene la solución completa al taller práctico sobre los Principios SOLID, donde cada principio se aplica y valida mediante una simulación de carrera visual en consola.

###Para ejecutar todos los test
```bash
pytest -v
```

###Para correr las pruebas de un ejercicio individual
```bash
pytest tests/test_ex1_srp.py -v
```

##Resumen de Soluciones y Preguntas de Discusión

1. SRP — Single Responsibility Principle (Principio de Responsabilidad Única)

Solución aplicada: Se removieron del método Car.move() las responsabilidades de impresión en consola y escritura en disco. Se creó la clase RaceLogger, encargada exclusivamente de registrar el historial por tick y guardarlo en un archivo (race_log.txt).

Preguntas de discusión:

¿Por qué es mejor que Car no sepa nada sobre logging o impresión?

Porque Car ahora tiene una única razón para cambiar: modificar el estado interno o la lógica de movimiento del vehículo. Si se cambia el formato de renderizado o el almacenamiento de datos, no es necesario tocar la clase Car.

¿Qué se rompería primero si el profesor pide guardar los resultados en JSON?

Si Car manejara el logging, habría que modificar el método move() de Car (y de cualquier otra clase de vehículo futura). Con el diseño refactorizado, solo se modifica el método save() de RaceLogger, dejando intactos todos los vehículos.

2. OCP — Open/Closed Principle (Principio Abierto/Cerrado)

Solución aplicada: Se añadieron las clases Motorcycle (movimiento rápido pero variable mediante random.choice) y Bicycle (movimiento que disminuye gradualmente por fatiga sin bajar de 1). Se logró mediante herencia de Vehicle sin modificar las clases base Vehicle, Car, Truck o Track.

Preguntas de discusión:

Si quisieras editar Vehicle o Track para completar este ejercicio, ¿qué diría de tu diseño?

Indicaría un diseño rígido y mal abstraído (violación de OCP). Un diseño bien orientado a objetos permite extender el comportamiento del sistema simplemente agregando nuevas subclases polimórficas sin necesidad de alterar el código existente ya probado y funcional.

3. LSP — Liskov Substitution Principle (Principio de Sustitución de Liskov)

Solución aplicada: Se rediseñó UnreliableCar para que la "falta de confiabilidad" no rompa el contrato de Vehicle. Ahora, si el auto falla (30% de probabilidad), simplemente se queda varado en el turno (return, avanza 0m) en lugar de lanzar excepciones o reducir su posición.

Preguntas de discusión:

¿Qué habrías tenido que agregar a Track si NO hubieras arreglado UnreliableCar?

Se habrían tenido que añadir bloques try/except para prevenir que la carrera se detenga por excepciones, y condicionales defensivos para corregir o validar que la posición de un vehículo nunca disminuya.

¿Por qué es mejor arreglar la subclase?

Porque la clase base y el cliente (Track) deben poder confiar en el contrato de la abstracción. Arreglar la subclase garantiza que sea 100% sustituible sin ensuciar el motor de la carrera con lógica condicional especial.

4. ISP — Interface Segregation Principle (Principio de Segregación de Interfaces)

Solución aplicada: Se dividió la interfaz pesada VehicleActions en cuatro interfaces independientes con un único método abstracto: Movable, Refuelable, Flyable y Pedalable. GasCar implementa Movable + Refuelable, Bicycle implementa Movable + Pedalable, y la nueva clase Drone implementa Movable + Flyable.

Preguntas de discusión:

¿Qué interfaz(es) necesitaría un futuro Submarine o Airplane?

Airplane: Implementaría Movable, Flyable y Refuelable.

Submarine: Implementaría Movable, Refuelable y posiblemente una nueva interfaz pequeña como Submersible.

¿Agregar una de estas clases requiere tocar alguna clase de vehículo existente?

No. Al tener interfaces segregadas, cada clase nueva solo implementa los comportamientos que necesita sin afectar a las demás clases del sistema.

5. DIP — Dependency Inversion Principle (Principio de Inversión de Dependencias)

Solución aplicada: Se refactorizó la clase Race para recibir la lista de competidores (racers) e instancias de Track mediante inyección de dependencias en su constructor __init__. Se agregó la clase RocketSled y se ejecutaron dos listas de competidores distintas en main() sin modificar el código de Race.

Preguntas de discusión:

¿Cómo facilita la inyección de dependencias las pruebas unitarias de Race sin una animación real en terminal?

Permite inyectar en las pruebas una lista de competidores simulados junto con una pista configurada sin animación (Track(animate=False, tick_seconds=0)). Esto hace que las pruebas ejecuten la lógica del negocio instantáneamente, sin depender de salidas en la consola ni demoras de tiempo real.

Reflexión Final (Wrap-up)

Ejemplo de violación en proyectos previos: En proyectos académicos anteriores (como sistemas de gestión o e-commerce), era común tener controladores o modelos que realizaban consultas a la base de datos, procesaban la lógica de negocio, enviaban correos electrónicos y daban formato a la respuesta HTTP dentro de una sola función (violación masiva de SRP e ISP).

Cambio propuesto: Separar el envío de correos en un servicio de notificaciones independiente e inyectar dicho servicio mediante interfaces (DIP), lo que facilitaría hacer pruebas unitarias aisladas sin enviar correos reales durante los tests.
