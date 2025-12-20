//Write a program in C++ to calculate the sum of the series 1.2+2.3+3.4+4.5+5.6+.......

#include <iostream>
using namespace std;

int main(){
    int n;
    int sum=0;

    cout << "Enter the number: ";
    cin>>n;

    if(n<=0){
        cout << "Enter a postiive number";
        return 0;
    }
    for (int i=0;i<=n;i++){
        sum=sum+(i*1);
    }
    cout<< "Sum of the series: "<<sum<<endl;


}