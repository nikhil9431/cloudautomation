package javaprogram;

import java.util.*;

public class longestsubstringwor {
	// longest substring without repeating
	
	private static String getUniqueCharacterSubstring(String input1) {
		// TODO Auto-generated method stub
		Map<Character, Integer> visited = new HashMap<>();
	    String output = "";
	    for (int start = 0, end = 0; end < input1.length(); end++) {
	        char currChar = input1.charAt(end);
	        if (visited.containsKey(currChar)) {
	            start = Math.max(visited.get(currChar)+1, start);
	        }
	        if (output.length() < end - start + 1) {
	            output = input1.substring(start, end + 1);
	        }
	        visited.put(currChar, end);
	    }
	    return output;
		
	}

	public static void  main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc=new Scanner(System.in);
		System.out.println("enter a string: ");
		String input1=sc.nextLine();
		System.out.println("longest substring "+longestsubstringwor.getUniqueCharacterSubstring(input1));
	

	}

}
