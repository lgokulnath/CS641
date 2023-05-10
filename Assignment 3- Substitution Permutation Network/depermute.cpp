#include<bits/stdc++.h>
using namespace std;
#define FOR(i, j, k, in) for (ll i = j; i < k; i += in)
#define RFOR(i, j, k, in) for (ll i = j; i >= k; i -= in)
#define REP(i, j) FOR(i, 0, j, 1)
#define RREP(i, j) RFOR(i, j, 0, 1)
#define PI 3.1415926535897932384626433832795
#define MOD 1000000007
#define pb push_back
#define f(v) v.begin(),v.end() 

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ll> vl;


string inputFile = "test.txt"; //input file containing the cipher text
string readInput() //function to read the input file and return the cipher text
{
	string txt;
	ifstream inFile;
	inFile.open(inputFile);
	if (inFile.is_open())
	{
		string line;
		while (getline(inFile, line))
		{
			std::transform(line.begin(), line.end(), line.begin(), ::tolower);
			line.erase(remove_if(line.begin(), line.end(), [](char c) { return !isalpha(c); }), line.end());
			txt = txt + line;
		}

		inFile.close();
	}
    else
    {
        cout<<"No input detected in the input file!"<<endl;
    }
	return txt;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    string ciphertext = readInput();
    ll i=0;
    ll n = ciphertext.length();
    string result;
    vector<int> perm = {3, 4, 1, 0, 2};
    while(i+5<n)
    {
        string sub = ciphertext.substr(i, 5);
        string temp = sub;
        ll j=0;
        for(auto ind : perm)
            temp[ind] = sub[j++];
        result.append(temp);
        i+=5;
    }
    cout<<result.length()<<endl;
    result.append(ciphertext.substr(i, n-i));
    cout<<result.length()<<endl;
    cout<<result<<endl;
    return 0;
}