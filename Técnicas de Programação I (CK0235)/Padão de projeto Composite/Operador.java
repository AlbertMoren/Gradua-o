//Composite
public class Operador extends Expressao{
    Expressao esq, dir;
    char tipoOp;

    @Override
    float operation() {
        float resultado;
        if(tipoOp == '+'){
            resultado = dir.operation() + esq.operation();
        }else{
            resultado = dir.operation() - esq.operation();
        }
        return resultado;
    }

    @Override
    void add(Expressao e) {
        
    }

    @Override
    void remove(Expressao e) {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'remove'");
    }

    @Override
    void getChild() {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'getChild'");
    }

    
}
