#include <iostream>
#include <string>
#include <sstream>
using namespace std;

int main() {
    int tipoTarjeta;
    string tipoTarjetaStr;
    string nombreCompleto;
    string apellidos;
    string fechaNacimiento;
    string correoElectronico;
    string numeroTarjeta;
    string cvv;
    string fechaVencimiento;

    cout << "Seleccione el tipo de tarjeta:" << endl;
    cout << "1. Visa" << endl;
    cout << "2. Mastercard" << endl;
    cin >> tipoTarjeta;
    cin.ignore();  // Ignorar el car�cter de nueva l�nea residual en el buffer

    switch (tipoTarjeta) {
        case 1:
            tipoTarjetaStr = "Visa";
            break;
        case 2:
            tipoTarjetaStr = "Mastercard";
            break;
        default:
            tipoTarjetaStr = "Tipo de tarjeta desconocido";
            break;
    }

    cout << "Nombre Completo: ";
    getline(cin, nombreCompleto);
    cout << "Apellidos: ";
    getline(cin, apellidos);
    cout << "Fecha de nacimiento (dd/mm/aaaa): ";
    getline(cin, fechaNacimiento);
    cout << "Correo Electr�nico: ";
    getline(cin, correoElectronico);

    bool numeroTarjetaValido = false;
    do {
        cout << "Numero de Tarjeta: ";
        getline(cin, numeroTarjeta);
        stringstream ss(numeroTarjeta);
        float testFloat;
        if (ss >> testFloat) {
            numeroTarjetaValido = true;
        } else {
            cout << "El n�mero de tarjeta debe ser un n�mero v�lido. Por favor, int�ntelo de nuevo." << endl;
        }
    } while (!numeroTarjetaValido);

    bool cvvValido = false;
    do {
        cout << "CVV: ";
        getline(cin, cvv);
        stringstream ss(cvv);
        int testInt;
        if (ss >> testInt) {
            cvvValido = true;
        } else {
            cout << "El CVV debe ser un n�mero v�lido. Por favor, int�ntelo de nuevo." << endl;
        }
    } while (!cvvValido);

    cout << "Tipo de tarjeta: " << tipoTarjetaStr << endl;
    cout << "DATOS TARJETA:" << endl;
    cout << "Nombre Completo: " << nombreCompleto << endl;
    cout << "Apellidos: " << apellidos << endl;
    cout << "Fecha de nacimiento: " << fechaNacimiento << endl;
    cout << "Correo Electr�nico: " << correoElectronico << endl;
    cout << "Numero de Tarjeta: " << numeroTarjeta << endl;
    cout << "CVV: " << cvv << endl;

    return 0;
}

