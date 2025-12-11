//write a c++ program to sort characters(numbers and punctuation symbols are not included in a string )
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

string sortc( const string &input){
    string letters;
    for(char c: input){ //extract only alphabets 
        if(isalpha(c)){
            letters+=c;
        }
    }
    sort(letters.begin(),letters.end());
    return letters;

}
int main(){
    string input;

    cout << "Enter the string: ";
    getline(cin,input);

    string result = sortc(input);
    cout << "sorted string= " << result << endl;
    return 0;
}