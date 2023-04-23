public class Ponto {
    float x,y;

    Ponto(){
        x = 0;
        y = 0;
    }

    Ponto(Float x1,Float y1){
        x = x1;
        y = y1;
    }

    void setXY(float x1, float y1){
        x = x1;
        y = y1;
    }

    void mover(float dx, float dy){
        x = x + dx;
        y = y + dy;
    }
}
