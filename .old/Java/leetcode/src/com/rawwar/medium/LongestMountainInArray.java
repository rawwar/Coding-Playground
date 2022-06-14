package com.rawwar.medium;

public class LongestMountainInArray {

    public static int longestMountain(int[] A) {
        int result=0;
        int leftIndex;
        int rightIndex;
        int currentPeak;
        int i=1;
        while(i < A.length-1){
            if (A[i] > A[i-1] && A[i] > A[i+1]){
                leftIndex = i-2;
                while(leftIndex >=0 && A[leftIndex] < A[leftIndex+1]){
                    leftIndex--;
                }
                rightIndex = i+2;
                while(rightIndex <A.length && A[rightIndex]< A[rightIndex-1]){
                    rightIndex++;
                }
                currentPeak = rightIndex - leftIndex -1;
                if(currentPeak>result){
                    result = currentPeak;
                }

            }else{
                i++;
                continue;
            }
            i = rightIndex;
        }

        return result;

    }

    public static void run(){
        int[] A = {2,1,4,7,3,2,5};
        System.out.println(longestMountain(A));

    }
}
