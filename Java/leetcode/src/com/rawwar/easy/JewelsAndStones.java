package com.rawwar.easy;

import java.util.HashSet;
import java.util.Set;

public class JewelsAndStones {

    public static int numJewelsInStones(String J, String S) {
        int total = 0;

        Set<Character> set = new HashSet<>();
        for (char c:J.toCharArray()){
            set.add(c);
        }

        for(char c: S.toCharArray()){
            if( set.contains(c)){
                total++;
            }
        }

        return total;


    }

    public static void run(){
        String J = "aA";
        String S = "aAAbbbb";
        System.out.println(numJewelsInStones(J, S));
    }
}
