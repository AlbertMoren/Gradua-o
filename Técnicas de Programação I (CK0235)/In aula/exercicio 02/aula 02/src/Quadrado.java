public class Quadrado{
   private Ponto origem;
   private double lado;

   public void setOrigem(double lado){
      origem = new Ponto(0,0);
      this.lado = lado;
   }

   public double permentro(){
      double permentro = 4 * this.lado;

      return permentro;
   }
}
