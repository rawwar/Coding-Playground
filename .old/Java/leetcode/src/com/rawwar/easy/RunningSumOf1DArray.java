package com.rawwar.easy;

public class RunningSumOf1DArray {
    // https://leetcode.com/problems/running-sum-of-1d-array/

    public static int[] runningSum(int[] nums) {
        for(int i=1;i<nums.length; i++){
            nums[i] += nums[i-1];
        }
        return nums;

    }

    public static void run() {
        int[] nums = {3,1,2,10,1};
        int[] ret = runningSum(nums);
        for (int i:ret) {
            System.out.println(i);
        }
    }


}
