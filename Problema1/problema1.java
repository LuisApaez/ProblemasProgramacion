
// Solucion problema1

public class problema1 {
    // Metodo principal
    public static void main(String[] args) {
        System.out.println(romanInt("MCMXCIV"));
    }

    // Metodo solucion
    public static int romanInt(String s) {
	// Declaramos las variables a utilizar
    int v = 0;
    int resultado = 0;
    int previo = 0;
	// Leeremos el numero de derecha a izquierda
    for(int i=s.length()-1; i>=0; i--){
        switch (s.charAt(i)) {
            case 'I': v = 1; break;
            case 'V': v = 5; break;
            case 'X': v = 10; break;
            case 'L': v = 50; break;
            case 'C': v = 100; break;
            case 'D': v = 500; break;
            case 'M': v = 1000; break;
        }
		// Si el valor previo es cero, hacemos que tome el valor de v capturado en la iteracion
        if(previo == 0){
            resultado = resultado + v;
            previo = v;
		// Si el valor de previo es mayor al actual en iteracion, restaremos
        } else if(previo > v){
            resultado = resultado - v;
            previo = v;
		// En cualquier otro caso sumaremos
        } else {
            resultado = resultado + v;
            previo = v;
        }
		// El valor de v se actualiza en cada iteracion
    }
    return resultado;
    }
}


