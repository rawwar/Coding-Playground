package com.rawwar.easy;

public class DefangingAnIPAddress {
    public static String defangIPaddr(String address) {
        StringBuilder result = new StringBuilder();
        for(char c: address.toCharArray()){
            if(c == '.'){
                result.append("[.]");
            }else{
                result.append(c);
            }
        }
        return result.toString();
//        return address.replaceAll("\\.","\\[\\.\\]");
    }

    public static void run(){
        String address = "1.1.1.1";
        System.out.println(defangIPaddr(address));

    }
}
