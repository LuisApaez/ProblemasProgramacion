import java.util.*;

public class problema5 {
    // Metodo principal
    public static void main(String[] args) {
        int x = 9;
        raiz(x);
    }

    // Metodo para calcular la raiz
    public static void raiz(int x) {
        // Array auxiliar
        List<Integer> push = new ArrayList<Integer>();
        // Variable entera auxiliar
        int y;

        // Casos para x=0 o x=1 cuya raiz es 0 o 1 respectivamente respectivamente
        switch (x) {
            case 0:
                System.out.println(0);
                break;
            case 1:
                System.out.println(1);
                break;
            default:
                break;
        }
        if (x < 0) {
            System.out.println("Error");
        } else{
            // Calculamos los cuadrados antes de x * x
            for (int i = 2; i < x; i++) {
                y = i * i;
                // Solo nos quedamos con los cuadrados menores al valor de x
                if (y <= x) {
                    push.add(i);
                } else {
                    break;
                }
            }
            // Arrojamos el ultimo elemento del array
            System.out.println(push.get(push.size()-1));
        }
    }
}
