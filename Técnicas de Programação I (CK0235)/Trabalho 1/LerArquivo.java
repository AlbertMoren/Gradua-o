import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Map;
import java.util.TreeMap;

public class LerArquivo {
    public Map<String, String> lerArquivo(String fileName){
        Map<String , String> cpfnome = new TreeMap<>();

        try {
            BufferedReader leitor = new BufferedReader(new FileReader(fileName));
            String line;
            while((line = leitor.readLine()) != null){
                String[] campos = line.split(";");
                String cpf = campos[0];
                String nome = campos[1];
                cpfnome.put(cpf, nome);
            }
            leitor.close();
        } catch (IOException e) {
            System.out.println("Erro ao ler o arquivo " + e.getMessage());
        }
        return cpfnome;
    } 
}
