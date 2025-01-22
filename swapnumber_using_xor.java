public class swapnumber_using_xor{
    public static void main(String[] args) {
        
        int number1 = 5;
        int number2 = 10;
 
        number1 = number1 ^ number2;
        number2 = number1 ^ number2;
        number1 = number1 ^ number2;

        System.out.println("Number 1: "+number1+"\nNumber 2: "+number2);

    }
}