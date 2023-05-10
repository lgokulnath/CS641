#include<bits/stdc++.h>
using namespace std;
#define FOR(i, j, k, in) for (ll i = j; i < k; i += in)
#define RFOR(i, j, k, in) for (ll i = j; i >= k; i -= in)
#define REP(i, j) FOR(i, 0, j, 1)
#define RREP(i, j) RFOR(i, j, 0, 1)
#define pb push_back 

typedef long long ll;
typedef vector<long long> vl;

string inputFile = "input.txt"; //input file containing the cipher text
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

ll gcd (ll a, ll b)
{
    return (b==0)?a:gcd(b, a%b);
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    string cipher = readInput();
    cout<<cipher.length()<<endl;
    cout<<cipher<<endl;

    map<string, vl> bigrams; //map containing the frequencies of all the bigrams
    map<string, vl> trigrams; //map containing the frequencies of all the trigrams

    for(ll i=0; i<cipher.length()-1; i++)
    {
        string next_bigram = cipher.substr(i, 2);
        string next_trigram = cipher.substr(i, 3);
        if(bigrams.find(next_bigram) == bigrams.end())
        {
            bigrams[next_bigram].push_back(i);
        }
        else
        {
            bigrams[next_bigram].push_back(i);
        }
        if(i>cipher.length()-3)
            continue;
        if(trigrams.find(next_trigram) == trigrams.end())
        {
            trigrams[next_trigram].push_back(i);
        }
        else
        {
            trigrams[next_trigram].push_back(i);
        }
    }

    for(auto pair : bigrams)
    {
        if(pair.second.size()>2)
        {
            cout<<pair.first<<" occurs multiple times at indices: ";
            for(auto ind : pair.second)
                cout<<ind<<" ";
            cout<<endl;
        }
    }

    for(auto pair : trigrams)
    {
        if(pair.second.size()>1)
        {
            cout<<pair.first<<" occurs multiple times at indices: ";
            for(auto ind : pair.second)
                cout<<ind<<" ";
            cout<<endl;
        }
    }
    return 0;
}