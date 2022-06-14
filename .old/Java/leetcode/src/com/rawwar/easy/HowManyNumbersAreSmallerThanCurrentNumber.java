package com.rawwar.easy;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class HowManyNumbersAreSmallerThanCurrentNumber {

    public static int[] smallerNumbersThanCurrent(int[] nums) {
        Map<Integer,Integer> map = new HashMap<>();
        int[] temp = nums.clone();
        Arrays.sort(temp);
        for (int i = 0; i < nums.length; i++) {
            map.putIfAbsent(temp[i],i);
        }
        for (int i = 0; i < nums.length; i++) {
            temp[i] = map.get(nums[i]);
        }
        return temp;
        }

    public static void run(){
        int[] nums = {8,1,2,2,3};
        for(int i: smallerNumbersThanCurrent(nums)){
            System.out.println(i);
        }
    }
}
