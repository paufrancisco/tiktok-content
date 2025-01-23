public class fibonacci_sequence {
    public static void main(String[] args) {


        int series = 10;
    
        int firstNum = 0;
        int secNum = 1;

        System.out.println("The terms of sequence till "+series+"term");
        for (int i = 1; i <=series; i++) {
            
            System.out.print(firstNum+" ");
            int nxtNum = firstNum+secNum;
            firstNum = secNum;
            secNum = nxtNum;

        }
    
    }

}
