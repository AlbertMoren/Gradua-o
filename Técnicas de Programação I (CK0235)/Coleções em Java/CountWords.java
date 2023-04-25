import java.util.*;

public class CountWords {
    private String frase;

    public CountWords(String frase){
        this.frase = frase;
    }
    
   public int Contapalavras(){
        String[] palavras = frase.split(" ");
        return palavras.length;     
   }

   public int ContapalavrasDiferentes(){
        String[] palavras = frase.split(" ");
        Set <String> set = new HashSet<>();
        for(int i = 0;i<palavras.length;i++){
            set.add(palavras[i]);
        }
        return set.size();
   }

   public void print(){
        System.out.println("Total de palavras = "+Contapalavras());
        System.out.println("Total de palavras diferentes = "+ ContapalavrasDiferentes());
   }
}
