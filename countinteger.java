import java.io.*;
public class countinteger{
public void main (String args[]){
int count=0,num=548;
while(num!=0)
{
num=num/10;
++count;
}
System.out.println("no.of.digits:"+count);
}
}
