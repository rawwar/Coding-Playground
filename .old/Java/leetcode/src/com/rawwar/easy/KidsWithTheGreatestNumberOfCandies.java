package com.rawwar.easy;

import java.util.ArrayList;
import java.util.List;

public class KidsWithTheGreatestNumberOfCandies {

    public static List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        List<Boolean> lst = new ArrayList<>();
        int max = candies[0];
        for (int i = 1; i < candies.length; i++) {
            if(candies[i] > max){
                max = candies[i];
            }
        }
        for (int i : candies) {
            if(i+extraCandies -max > 0){
                lst.add(true);
            }
                lst.add(false);

        }

        return  lst;
    }

    public static void run(){

        int[] candies = {2,3,5,1,3};
        int extraCandies = 3;
        for (boolean i : kidsWithCandies(candies,extraCandies)) {
            System.out.println(i);

        }
    }
}
