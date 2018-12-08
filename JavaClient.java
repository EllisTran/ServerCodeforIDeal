import java.io.*;  
    import java.net.*; 
	import java.util.Scanner;

    public class JavaClient {
		public static void main(String[] args) 
		{  

			Scanner scan = new Scanner(System.in);	//Allows for input from the terminal
			try
			{      
				Socket soc=new Socket("localhost",2004);  			//Creates new socket to connect with server

				//ALlows data to be received and sent to the server
				DataOutputStream dout=new DataOutputStream(soc.getOutputStream()); 
				DataInputStream din=new DataInputStream(soc.getInputStream());

				System.out.print("Enter your ID number: ");
				String id = scan.next();		//Takes input into id
				scan.close();		//stops input
	
				dout.writeUTF(id);		//Sends id to server
				dout.flush();

				//Receives data from Server
				String idfromServer = din.readUTF();
				String fullName = din.readUTF();
				String email = din.readUTF();
				System.out.println("\nName:\t\t" + fullName);
				System.out.println("Universiy ID:\t" + idfromServer);
				System.out.println("Email:\t\t" + email);
				din.close();
				dout.close(); 
				soc.close();
			
			}catch(Exception e){
				e.printStackTrace();
			} 			
		}  
		
	}