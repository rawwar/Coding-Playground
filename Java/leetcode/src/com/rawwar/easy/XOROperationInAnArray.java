package com.rawwar.easy;

public class XOROperationInAnArray {

    public static int xorOperation(int n, int start) {
        int result = start;
        for (int i = 1; i <n ; i++) {
            result = result ^ (start + 2*i);
        }
        return result;

    }

    public static void  run(){
        int n=5;
        int start = 0;
        System.out.println(xorOperation(n, start));
    }
}
