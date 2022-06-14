package com.rawwar.easy;

public class SubtractTheProductAndSumOfDigits {
    public static void run(){
        int n = 4421;
        System.out.println(subtractProductAndSum(n));
    }

    public static int subtractProductAndSum(int n) {
        int sum=0,product=1;
        int temp;
        while(n>0){
            temp = n%10;
            n = n/10;
            sum += temp;
            product *=temp;

        }
        return product - sum;
    }

}
