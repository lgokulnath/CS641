#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define M 1000000007
int main() {
ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
#ifndef ONLINE_JUDGE
freopen("input.txt", "r", stdin);
freopen("output.txt", "w", stdout);
#endif
string temp;
char y;
while(cin>>y){
    if(y>='A'&&y<='Z'){
        temp=temp+(char)(y-'A'+'a');
    }
    else
    if(y>='a'&&y<='z'){
        temp=temp+y;
    }
}
vector<string>a(10);
for(ll j=0;j<10;j++){
    for(ll i=j;i<temp.size();i=i+10){
        a[j].push_back(temp[i]);
    }
}
vector<vector<double>>cnt(10,vector<double>(26,0));
for(ll i=0;i<10;i++){
    for(auto j:a[i]){
        cnt[i][j-'a']+=1;
    }
}
for(ll i=0;i<10;i++){
    double r=0;
    for(auto j:cnt[i]){
        r+=j;
    }
    for(ll j=0;j<cnt[i].size();j++){
        cnt[i][j]=cnt[i][j]/r;
    }
}
vector<double>orig={0.0812384,0.0148928,0.0271142,0.0431918,0.120195,0.0230386,0.0202575,0.0592146,0.0730542,0.00103125,0.00689511,0.0397854,0.0261159,0.0694777,0.0768117,0.0181895,0.0011245,0.0602129,0.0628075,0.0909859,0.0287763,0.011075,0.0209486,0.00172789,0.0211351,0.000702128};
vector<double>sum(10,0);
string key="jcaaaaaaaa";
for(ll i=0;i<10;i++){
    double mx=-1;
    for(ll p=0;p<26;p++){
        sum[i]=0;
        for(ll j=0;j<26;j++){
            sum[i]=sum[i]+(cnt[i][(j+p)%26]*orig[j]);
        }
        if(sum[i]>mx){
            mx=sum[i];
            key[i]='a'+p;
        }
    }
}
cout<<key<<"\n";
for(ll i=0;i<10;i++){
    sum[i]=0;
    for(ll j=0;j<26;j++){
        sum[i]=sum[i]+(cnt[i][(j+key[i]-'a')%26]*orig[j]);
    }
}
for(ll i=0;i<10;i++){
    cout<<sum[i]<<"\n";
}
for(ll j=0;j<temp.size();j++){
    temp[j]=(temp[j]-key[j%10]+26)%26+'a';
}
cout<<temp<<"\n";
string g="Kg fcwd qh vin pnzy hjcocnt, cjjwg ku wnth nnyvng kxa cjjwg. Urfjm xwy yjg rbbufqwi 'vjg_djxn_ofs_dg_rmncbgi' yq iq uqtxwlm. Oca zxw qcaj vjg tctnplyj hqs cjn pjcv ejbvdnt. Yt hkpe cjn gcnv,aqv okauy bknn ongm vt zvvgs vcpkh bqtft cjntj.";
ll e=0;
for(ll u=0;u<g.size();u++){
    if(g[u]>='A'&&g[u]<='Z'){
        g[u]=(g[u]-'A'+'a'-key[e%10]+26)%26+'A';
        e++;
    }
    else
    if(g[u]>='a'&&g[u]<='z'){
        g[u]=(g[u]-key[e%10]+26)%26+'a';
        e++;
    }
}
cout<<g;
}