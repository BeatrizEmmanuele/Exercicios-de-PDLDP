public class vetor2{
    public static void main(String[] args){
        Scanner scaner = new Scanner(System.in);

        int[] numbers = new int[6];
        int sumEven = 0;
        int countOdd = 0;

        System.out.println("Digite 6 números inteiros: " );

        for ( int i = 0; i< 6; i++){
            numbers[i] = scanner.nextInt();
        }


        System.out.println("Números pares digitados: " );
        for( int num : numbers){
            if(num % 2 == 0){
                System.out.println(num + " ");
                sumEven += num; 
                
            }
        }


        System.out.println("Soma dos números pares: " + sumEven);

        System.out.println("Números ímpares digitados: ");
        for (int num : numbers){
            if(num % 2 != 0){
                System.out.println(num + );

            }
        }

        System.out.println("Quantidades de números ímpares: "+countOdd);
    }
}