package com.rawwar.easy;

import java.util.ArrayList;
import java.util.List;

public class DecompressRunLengthEncodedList {

    public static int[] decompressRLEList(int[] nums) {
        List<Integer> lst = new ArrayList<>();
        for (int i = 0; i < nums.length / 2; i++) {
            for (int j = 0; j < nums[2 * i]; j++) {
                lst.add(nums[2*i +1]);
            }
        }

        return lst.stream().mapToInt(i->i).toArray();

    }


    public static void run(){
        int[] nums = {1,2,3,4};
        int[] res = decompressRLEList(nums);

        for(int i: res){
            System.out.println(i);
        }
    }
}
