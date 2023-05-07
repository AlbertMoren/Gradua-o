import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class LerArquivo {
    public Map<String, String> lerArquivo(String fileName){
        Map<String , String> cpfnome = new HashMap<>();

        try {
            BufferedReader reader = new BufferedReader(new FileReader(fileName));
            String line;
            while((line = reader.readLine()) != null){
                String[] campos = line.split(";");
                String cpf = campos[0];
                String nome = campos[1];
                cpfnome.put(cpf, nome);
            }
            reader.close();
        } catch (IOException e) {
            System.out.println("Erro ao ler o arquivo " + e.getMessage());
        }
        return cpfnome;
    } 
}
