//Component
public abstract class Expressao{
    abstract float operation();
    abstract void add(Expressao esq, Expressao dir);
    abstract void remove(Expressao e);
    abstract void getChild();
}