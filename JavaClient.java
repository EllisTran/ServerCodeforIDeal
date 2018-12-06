import java.io.*;  
    import java.net.*; 
	import java.util.Scanner;
    public class JavaClient {
		public static void main(String[] args) {  
			Scanner scan = new Scanner(System.in);
			try{      
			Socket soc=new Socket("localhost",2004);  
			DataOutputStream dout=new DataOutputStream(soc.getOutputStream()); 
			DataInputStream din=new DataInputStream(soc.getInputStream());
			System.out.println("Enter your id number");
			String id = scan.next();
			dout.writeUTF(id);
			dout.flush();
			String idfromServer = din.readUTF();
				System.out.println("\nID Number: " + idfromServer);
				String fullName = din.readUTF();
				
				System.out.println("Name: " + fullName);
				String email = din.readUTF();
				System.out.println("Email: " + email);
				din.close();
				dout.close(); 
				soc.close();
			
			}catch(Exception e){
				e.printStackTrace();
			} 			
		}  
		
	}