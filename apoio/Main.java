package exercicios;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {

public static void main(String[] args) {
// TODO Auto-generated method stub
BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
BufferedWriter lec = new BufferedWriter(new OutputStreamWriter(System.out));

try
{
String[] num = br.readLine().split(" ");
int x = Integer.parseInt(num[0]);
int y = Integer.parseInt(num[1]);

while(y < 1)
{
y = Integer.parseInt(br.readLine());
}

int result = 0;

for(int i = x; i < (x + y); i++)
{
result += i;
}

lec.write(result + "\n");
lec.flush();
br.close();
}
catch(Exception ex){ }


}

}