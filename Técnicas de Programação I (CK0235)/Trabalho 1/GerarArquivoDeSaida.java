import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Map;

public class GerarArquivoDeSaida {
    public void escreverNoArquivo(Map<String , String> cpfnome, String fileName){
        try {
            BufferedWriter escrita = new BufferedWriter(new FileWriter(fileName));
            for(Map.Entry<String,String> entry: cpfnome.entrySet()){
                escrita.write(entry.getKey() + ";" + entry.getValue());
                escrita.newLine();
            }
            escrita.close();
        } catch (IOException e) {
            System.out.println("Erro ao escrever o arquivo" + e.getMessage());
        }
    }
}
