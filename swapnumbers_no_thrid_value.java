


public class swapnumbers_no_thrid_value {
    public static void main(String[] args) {
        
        int number1 = 5;
        int number2 = 10;
 
        number1 = number1 + number2;
        number2 = number1 - number2;
        number1 = number1 - number2;

        System.out.println("This is number1: "+number1);
        System.out.println("Thsi is number2: "+number2);

    }
}
