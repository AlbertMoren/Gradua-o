import java.util.*;
public class MapExample {
    public static void main(String[] args) {
        Map mapa = new HashMap<>();
        mapa.put("um", "Primeiro valor");
        mapa.put("Dois", "Segundo valor");
        mapa.put("Três", "Terceiro valor");
        System.out.println("Valor recuperados: " + mapa.get("dois"));
        Set chaves = mapa.keySet();
        Collection valores = mapa.values();
        System.out.println(chaves);
        System.out.println(valores);
    }
}
