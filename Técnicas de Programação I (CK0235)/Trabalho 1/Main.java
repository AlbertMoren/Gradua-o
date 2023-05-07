import java.util.Map;

public class Main {

    public static void main(String[] args) {
        String arquivo1 = "file1.txt";
        String arquivo2 = "file2.txt";
        String arquivoDeSaida = "marge.txt";

        LerArquivo arquivo = new LerArquivo();
        Map <String, String> cpfnome =  arquivo.lerArquivo(arquivo1);
        cpfnome.putAll(arquivo.lerArquivo(arquivo2));

        GerarArquivoDeSaida arquivoSaida = new GerarArquivoDeSaida();
        arquivoSaida.escreverNoArquivo(cpfnome, arquivoDeSaida);

        System.out.println("Merge concluido com sucesso");

    }
}