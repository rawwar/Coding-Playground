package com.rawwar.easy;

public class ShuffleTheArray {

    public static int[] shuffle(int[] nums, int n) {

        int[] result = new int[2*n];
        for (int i = 0; i < n; i++) {
            result[2*i] = nums[i];
            result[2*i + 1] = nums[n+i];
            
        }
        return result;


    }


    public static void run() {
        int[] nums = {2,5,1,3,4,7};
        int n = 3;
        for(int i: shuffle(nums, n)) {
            System.out.println(i);
        }

    }
}
