0x00. AirBnB clone - The console
This project is the first step towards building my first full web application: the AirBnB clone.

The project deals with the following components:
- Puts in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
- Creates a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- Creates all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
- Creates the first abstracted storage engine of the project: File storage.
- Create all unittests to validate all our classes and storage engine

