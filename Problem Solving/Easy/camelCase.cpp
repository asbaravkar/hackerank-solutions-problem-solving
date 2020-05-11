#include <bits/stdc++.h>

using namespace std;

// Complete the camelcase function below.
int camelcase(string s) {
int cnt=0;
int n=s.length();
for(int i=0; i<n; i++)
{
    if(s[i]>='A' && s[i]<='Z')
        cnt++;
}
return cnt+1;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);

    int result = camelcase(s);

    fout << result << "\n";

    fout.close();

    return 0;
}
