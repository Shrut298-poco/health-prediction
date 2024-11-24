#include<iostream>
using namespace std;
int main()
{   
    string name;
    string a;
    cout<<"WELCOME IN NLP:-";
    cout<<"\nPLEASE ENTER YOUR NAME:-"<<endl;
    cin>>name;
    cout<<"\nHii !!"<<name;
    cout<<"\nenter commom word NLP system is AUTOCOMPLETE these word.....WORDS LIKE:-thank,happy,may,I,take,good,how,what"<<endl;
    cin>>a;
     if(a=="thank")
    {
        cout<<" your choice:-THANKU YOU....";
    } 
     if(a=="happy")
    {
        cout<<"your choice:-HAPPY_BIRTHAY_DAY..";
    } 
     if(a=="may")
    {
        cout<<"your choice:-MAY_GOOD_BLESH_YOU...";
    } 
     if(a=="how")
    {
        cout<<"your choice:-HOW ARE YOU...";
    } 
     if(a=="what")
    {
        cout<<"your choice:-WHAT HAPPEND BUDDY...";
    } 
     if(a=="I")
    {
        cout<<"your choice:-I AM SORRY";
    } 
     if(a=="good")
    {
        cout<<"your choice:-GOOD MAORNIG/ GOOD AFTERNOON/ GOOD EVENING/ GOOD NIGHT";
    } 
     if(a=="take")
    {
        cout<<"your choice:-TAKE CARE";
    } 
    else
    {
      cout<<"\nSORRY WORD NOT MATCH!!!!!!!!!!";
    }
  
    cout<<"\nTHANKS FOR COMING";
    cout<<"\nBYE .... HAVE A NICE DAY";

}