#include <bits/stdc++.h>

using namespace std;

// Complete the minimumNumber function below.
int minimumNumber(int n, string password) {
    // Return the minimum number of characters to make the password strong
    int len=password.size();
    string specials="!@#$%^&*()-+";
    // flags
    bool digit=false, lower=false, upper=false, special=false;

    for(int i=0; i<len; i++){
        if(password[i]>='a' && password[i]<='z') lower=true;
        if(password[i]>='A' && password[i]<='Z') upper=true;
        if(password[i]>='0' && password[i]<='9') digit=true;
        if(specials.find(password[i])!=string::npos) special=true;
    }

    int res=0;
    
    if(!lower) res++;
    if(!upper) res++;
    if(!digit) res++;
    if(!special) res++;
    if(len+res<6) res+=6-(len+res);

    return res;

}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    string password;
    getline(cin, password);

    int answer = minimumNumber(n, password);

    fout << answer << "\n";

    fout.close();

    return 0;
}
#include <bits/stdc++.h>

using namespace std;

// Complete the minimumNumber function below.
int minimumNumber(int n, string password) {
    // Return the minimum number of characters to make the password strong
    int len=password.size();
    string specials="!@#$%^&*()-+";
    // flags
    bool digit=false, lower=false, upper=false, special=false;

    for(int i=0; i<len; i++){
        if(password[i]>='a' && password[i]<='z') lower=true;
        if(password[i]>='A' && password[i]<='Z') upper=true;
        if(password[i]>='0' && password[i]<='9') digit=true;
        if(specials.find(password[i])!=string::npos) special=true;
    }

    int res=0;
    
    if(!lower) res++;
    if(!upper) res++;
    if(!digit) res++;
    if(!special) res++;
    if(len+res<6) res+=6-(len+res);

    return res;

}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    string password;
    getline(cin, password);

    int answer = minimumNumber(n, password);

    fout << answer << "\n";

    fout.close();

    return 0;
}
