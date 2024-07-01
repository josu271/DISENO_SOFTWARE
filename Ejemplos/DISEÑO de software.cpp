#include <iostream>
#include <string>

using namespace std;

int main() {
    int opcion;
    
    string nombre, apellido, correoElectronico, genero, contrasena, fechaNacimiento;
    string numeroTelefonico;
    do {
        cout << "\nMenu:\n";
        cout << "1. Ingresar nombre\n";
        cout << "2. Ingresar apellido\n";
        cout << "3. Ingresar correo electronico\n";
        cout << "4. Ingresar genero\n";
        cout << "5. Ingresar numero telefonico\n";
        cout << "6. Ingresar contrasena\n";
        cout << "7. Ingresar fecha de nacimiento\n";
        cout << "Seleccione una opcion: ";
        cin >> opcion ;

        switch (opcion)
		 {
	           case 1: 
	              cout << "ingrese su nombre: ";
	              cin >> nombre;
	              break;
	           case 2: 
	              cout << "ingrese su apellido: ";
	              cin >> apellido;
	              break;
	           case 3: 
	              cout << "ingrese su correo electronico: ";
	              cin >> correoElectronico ;
	              break;
	           case 4: 
	              do {
                    cout << "Ingrese su genero (masculino, femenino): ";
                    getline(cin, genero);
                    
                    if (!(genero == "masculino" || genero == "femenino")) {
                        cout << "Genero invalido. Por favor, intentalo de nuevo." << endl;
                       }
                    } while (!(genero == "masculino" || genero == "femenino"));
                    break;
	           case 5: 
	              cout << "ingrese su numero telefonico: ";
	              cin >> numeroTelefonico;
	              break;
	           case 6: 
	              cout << "ingrese su contraseña: ";
	              cin >> contrasena;
	              break;
	           case 7: 
	              cout << "ingrese su fecha de nacimiento (formato dd/mm/aaaa): ";
	              cin >> fechaNacimiento;
	              break;
	           default: 
	              cout << "Opcion invalida. Por favor,seleccione una opcion valida. " << endl;
	              break;
         }
    }while(opcion != 7);
    cout << "\nDatos del proveedor registrado:\n";
    cout << "Nombre: " << nombre << "\n";
    cout << "Apellido: " << apellido << "\n";
    cout << "Correo electronico: " << correoElectronico << "\n";
    cout << "Genero: " << genero << "\n";
    cout << "Numero telefonico: " << numeroTelefonico << "\n";
    cout << "Fecha de nacimiento: " << fechaNacimiento << "\n";

    return 0;
}
