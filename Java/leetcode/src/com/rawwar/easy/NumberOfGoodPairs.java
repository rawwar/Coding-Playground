package com.rawwar.easy;

import java.util.HashMap;

public class NumberOfGoodPairs {
    // https://leetcode.com/problems/number-of-good-pairs/
    public static int numIdenticalPairs(int[] nums) {
        int total = 0;
        HashMap<Integer,Integer> map = new HashMap<>();
        for (int key : nums) {
            if (map.containsKey(key)){
                map.put(key,map.get(key)+1);
            }else{
                map.put(key,1);
            }
        }
        for(int each : map.values()){
            if(each>1){
                total += each*(each-1)/2;
            }
        }
//        for (Map.Entry<Integer,Integer> entry : map.entrySet())
//            System.out.println("Key = " + entry.getKey() +
//                    ", Value = " + entry.getValue());
        return total;

    }
//
//    public static int ncr(int num) {
//        return factorial(num) / (factorial(2) * factorial(num-2));
//
//    }
//
//    public static int factorial(int n) {
//        if(n<=1){
//            return 1;
//        }else{
//            return n* factorial(n-1);
//        }
//    }

    public static void run(){
        int[] nums = {6,5,1,5,7,7,9,1,5,7,1,6,10,9,7,4,1,8,7,1,1,8,6,4,7,4,10,5,3,9,10,1,9,5,5,4,1,7,4,2,9,2,6,6,4,2,10,3,5,3,6,4,7,4,6,4,4,6,3,4,10,1,10,6,10,4,9,6,6,4,8,6,9,5,4};

        System.out.println(numIdenticalPairs(nums));
    }

}
