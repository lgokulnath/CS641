#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define M 1000000007
int ROUND=6;
vector<ll> cpy(vector<ll> a, ll l, ll r)
{
    vector<ll> temp;
    for (ll j = l; j <= r; j++)
    {
        temp.push_back(a[j]);
    }
    return temp;
}
vector<ll> expansion(vector<ll> a)
{
    vector<ll> ans;
    vector<ll> temp = {32, 1, 2, 3, 4, 5,
                       4, 5, 6, 7, 8, 9,
                       8, 9, 10, 11, 12, 13,
                       12, 13, 14, 15, 16, 17,
                       16, 17, 18, 19, 20, 21,
                       20, 21, 22, 23, 24, 25,
                       24, 25, 26, 27, 28, 29,
                       28, 29, 30, 31, 32, 1};
    for(ll j=0;j<48;j++){
        ans.push_back(a[temp[j]-1]);
    }
    return ans;
}
vector<ll>XOR(vector<ll>a,vector<ll>b){
    for(ll j=0;j<a.size();j++){
        a[j]=a[j]^b[j];
    }
    return a;
}
vector<ll>permutation(vector<ll>a){
    vector<ll>ans;
    vector<ll>temp={16 ,	7 ,	20 ,	21 ,	29 ,	12 ,	28 	,17,
                    1 ,	15 	,23 ,	26 ,	5 	,18 	,31 ,	10,
                    2 ,	8 	,24 ,	14 ,	32 ,	27 	,3 	,9,
                    19 ,	13 	,30 ,	6 	,22 ,	11 	,4 ,	25 };
    for(ll j=0;j<a.size();j++){
        ans.push_back(a[temp[j]-1]);
    }
    return ans;
}
vector<ll>SBOX(vector<ll>a){
    vector<vector<ll>>s1={{ 14 ,4 ,13 ,1 ,2 ,15 ,11 ,8 ,3 ,10 ,6 ,12 ,5 ,9 ,0 ,7 },
                            { 0 ,15 ,7 ,4 ,14 ,2 ,13 ,1 ,10 ,6 ,12 ,11 ,9 ,5 ,3 ,8 },
                            { 4 ,1 ,14 ,8 ,13 ,6 ,2 ,11 ,15 ,12 ,9 ,7 ,3 ,10 ,5 ,0 },
                            { 15 ,12 ,8 ,2 ,4 ,9 ,1 ,7 ,5 ,11 ,3 ,14 ,10 ,0 ,6 ,13 }
                            };
    vector<vector<ll>>s2={{ 5 ,1 ,8 ,14 ,6 ,11 ,3 ,4 ,9 ,7 ,2 ,13 ,12 ,0 ,5 ,10 ,},
                        { 3 ,13 ,4 ,7 ,15 ,2 ,8 ,14 ,12 ,0 ,1 ,10 ,6 ,9 ,11 ,5 ,},
                        { 0 ,14 ,7 ,11 ,10 ,4 ,13 ,1 ,5 ,8 ,12 ,6 ,9 ,3 ,2 ,15 ,},
                        { 13 ,8 ,10 ,1 ,3 ,15 ,4 ,2 ,11 ,6 ,7 ,12 ,0 ,5 ,14 ,9 ,},
                        };   
    vector<vector<ll>>s3={{ 10 ,0 ,9 ,14 ,6 ,3 ,15 ,5 ,1 ,13 ,12 ,7 ,11 ,4 ,2 ,8 ,},
                        { 13 ,7 ,0 ,9 ,3 ,4 ,6 ,10 ,2 ,8 ,5 ,14 ,12 ,11 ,15 ,1 ,},
                        { 13 ,6 ,4 ,9 ,8 ,15 ,3 ,0 ,11 ,1 ,2 ,12 ,5 ,10 ,14 ,7 ,},
                        { 1 ,10 ,13 ,0 ,6 ,9 ,8 ,7 ,4 ,15 ,14 ,3 ,11 ,5 ,2 ,12 ,},
                        };       
    vector<vector<ll>>s4= {{ 7 ,13 ,14 ,3 ,0 ,6 ,9 ,10 ,1 ,2 ,8 ,5 ,11 ,12 ,4 ,15 ,},
                        { 13 ,8 ,11 ,5 ,6 ,15 ,0 ,3 ,4 ,7 ,2 ,12 ,1 ,10 ,14 ,9 ,},
                        { 10 ,6 ,9 ,0 ,12 ,11 ,7 ,13 ,15 ,1 ,3 ,14 ,5 ,2 ,8 ,4 ,},
                        { 3 ,15 ,0 ,6 ,10 ,1 ,13 ,8 ,9 ,4 ,5 ,11 ,12 ,7 ,2 ,14 ,},
                        };
    vector<vector<ll>>s5= {{ 2 ,12 ,4 ,1 ,7 ,10 ,11 ,6 ,8 ,5 ,3 ,15 ,13 ,0 ,14 ,9 ,},
                        { 14 ,11 ,2 ,12 ,4 ,7 ,13 ,1 ,5 ,0 ,15 ,10 ,3 ,9 ,8 ,6 ,},
                        { 4 ,2 ,1 ,11 ,10 ,13 ,7 ,8 ,15 ,9 ,12 ,5 ,6 ,3 ,0 ,14 ,},
                        { 11 ,8 ,12 ,7 ,1 ,14 ,2 ,13 ,6 ,15 ,0 ,9 ,10 ,4 ,5 ,3 ,},
                        };
    vector<vector<ll>>s6={{ 12 ,1 ,10 ,15 ,9 ,2 ,6 ,8 ,0 ,13 ,3 ,4 ,14 ,7 ,5 ,11 ,},
                        { 10 ,15 ,4 ,2 ,7 ,12 ,9 ,5 ,6 ,1 ,13 ,14 ,0 ,11 ,3 ,8 ,},
                        { 9 ,14 ,15 ,5 ,2 ,8 ,12 ,3 ,7 ,0 ,4 ,10 ,1 ,13 ,11 ,6 ,},
                        { 4 ,3 ,2 ,12 ,9 ,5 ,15 ,10 ,11 ,14 ,1 ,7 ,6 ,0 ,8 ,13 ,},
                        };
    vector<vector<ll>>s7={{ 4 ,11 ,2 ,14 ,15 ,0 ,8 ,13 ,3 ,12 ,9 ,7 ,5 ,10 ,6 ,1 ,},
                        { 13 ,0 ,11 ,7 ,4 ,9 ,1 ,10 ,14 ,3 ,5 ,12 ,2 ,15 ,8 ,6 ,},
                        { 1 ,4 ,11 ,13 ,12 ,3 ,7 ,14 ,10 ,15 ,6 ,8 ,0 ,5 ,9 ,2 ,},
                        { 6 ,11 ,13 ,8 ,1 ,4 ,10 ,7 ,9 ,5 ,0 ,15 ,14 ,2 ,3 ,12 ,},
                        };
    vector<vector<ll>>s8={{ 13 ,2 ,8 ,4 ,6 ,15 ,11 ,1 ,10 ,9 ,3 ,14 ,5 ,0 ,12 ,7 ,},
                        { 1 ,15 ,13 ,8 ,10 ,3 ,7 ,4 ,12 ,5 ,6 ,11 ,0 ,14 ,9 ,2 ,},
                        { 7 ,11 ,4 ,1 ,9 ,12 ,14 ,2 ,0 ,6 ,10 ,13 ,15 ,3 ,5 ,8 ,},
                        { 2 ,1 ,14 ,7 ,4 ,10 ,8 ,13 ,15 ,12 ,9 ,0 ,3 ,5 ,6 ,11 ,},
                        };
    vector<vector<vector<ll>>>s;
    s.push_back(s1);
    s.push_back(s2);
    s.push_back(s3);
    s.push_back(s4);
    s.push_back(s5);
    s.push_back(s6);
    s.push_back(s7);
    s.push_back(s8);
    vector<ll>ans;
    for(ll j=0;j<8;j++){
        vector<ll>temp;
        for(ll k=j*6;k<j*6+6;k++){
            temp.push_back(a[k]);
        }
        ll r,c;
        r=temp[0]*2+temp[5]*1;
        c=temp[1]*8+temp[2]*4+temp[3]*2+temp[4]*1;
        ll y=s[j][r][c];
        vector<ll>x;
        for(ll k=0;k<4;k++){
            x.push_back(y%2);
            y=y/2;
        }
        for(ll k=3;k>=0;k--){
            ans.push_back(x[k]);
        }
    }
    return ans;
}
vector<ll> round_output(vector<ll> inp, vector<ll> key)
{   vector<ll> left = cpy(inp, 0, 31);
    vector<ll> right = cpy(inp, 32, 63);
    vector<ll> aft_exp = expansion(right);
    vector<ll> aft_exp_xor= XOR(aft_exp,key);
    vector<ll> aft_exp_xor_sbox=SBOX(aft_exp_xor);
    vector<ll> aft_exp_xor_sbox_per=permutation(aft_exp_xor_sbox);
    vector<ll> temp = XOR(aft_exp_xor_sbox_per,left);
    vector<ll> ans;
    for(ll j=0;j<left.size();j++){
        ans.push_back(right[j]);
    }
    for(ll j=0;j<temp.size();j++){
        ans.push_back(temp[j]);
    }
    return ans;
}
vector<ll>PC1(vector<ll>key){
    vector<ll>temp={57 ,  49   , 41 ,  33  ,  25  ,  17  ,  9,
               1 ,  58  ,  50  , 42  ,  34  ,  26  , 18,
              10 ,   2  ,  59  , 51  ,  43  ,  35  , 27,
              19 ,  11  ,   3  , 60  ,  52  ,  44  , 36,
              63 ,  55  ,  47  , 39  ,  31  ,  23  , 15,
               7 ,  62  ,  54  , 46  ,  38  ,  30  , 22,
              14 ,   6  ,  61  , 53  ,  45  ,  37  , 29,
              21  , 13  ,   5  , 28  ,  20  ,  12  ,  4};
    vector<ll>ans;
    for(ll j=0;j<temp.size();j++){
        ans.push_back(key[temp[j]-1]);
    }
    return ans;
}
vector<ll>PC2(vector<ll>key){
    vector<ll>temp={14 ,   17  , 11 ,   24  ,   1 ,   5,
                  3  ,  28  , 15 ,    6  ,  21 ,  10,
                 23  ,  19  , 12  ,   4  ,  26 ,   8,
                 16  ,   7  , 27  ,  20   , 13 ,   2,
                 41  ,  52  , 31  ,  37   , 47  , 55,
                 30   , 40 ,  51   , 45   , 33  , 48,
                 44  ,  49  , 39   , 56   , 34  , 53,
                 46   , 42  , 50    ,36  ,  29  , 32};
    vector<ll>ans;
    for(ll j=0;j<temp.size();j++){
        ans.push_back(key[temp[j]-1]);
    }
    return ans;
}
vector<ll>ls(vector<ll>key){
    vector<ll>left=cpy(key,0,27);
    vector<ll>right=cpy(key,28,55);
    ll t=left[0];
    for(ll j=0;j<27;j++){
        left[j]=left[j+1];
    }
    left[27]=t;
    t=right[0];
    for(ll j=0;j<27;j++){
        right[j]=right[j+1];
    }
    right[27]=t;
    vector<ll>ans;
    for(ll j:left){
        ans.push_back(j);
    }
    for(ll j:right){
        ans.push_back(j);
    }
    return ans;
}
vector<vector<ll>>gen_key(vector<ll>key){
    vector<ll>no_left_shift={1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1};
    vector<vector<ll>>ans;
    for(ll j=0;j<ROUND;j++){
        for(ll k=0;k<no_left_shift[j];k++){
            key=ls(key);    
        }
        ans.push_back(key);
    }
    for(ll j=0;j<ROUND;j++){
        ans[j]=PC2(ans[j]);
    }

    return ans;
}
vector<ll>IP(vector<ll>a){
    vector<ll>temp={58  ,  50  , 42  ,  34    ,26  , 18 ,   10   , 2,
            60   , 52  , 44  ,  36  ,  28  , 20  ,  12  ,  4,
            62   , 54  , 46  ,  38  ,  30  , 22   , 14  ,  6,
            64    ,56  , 48  ,  40  ,  32  , 24  ,  16  ,  8,
            57   , 49 ,  41  ,  33  ,  25  , 17  ,   9  ,  1,
            59   , 51  , 43  ,  35  ,  27  , 19  ,  11  ,  3,
            61   , 53  , 45  ,  37  ,  29 ,  21  ,  13  ,  5,
            63   , 55  , 47  ,  39  ,  31  , 23  ,  15  ,  7};
    vector<ll>ans;
    for(ll j=0;j<temp.size();j++){
        ans.push_back(a[temp[j]-1]);
    }
    return ans;
}
vector<ll>IP_inverse(vector<ll>a){
    vector<ll>temp={40  ,   8   ,48 ,   16  ,  56  , 24  ,  64  , 32,
            39   ,  7   ,47   , 15  ,  55 ,  23   , 63  , 31,
            38   ,  6   ,46   , 14  ,  54 ,  22  ,  62  , 30,
            37   ,  5  , 45   , 13  ,  53 ,  21   , 61  , 29,
            36   ,  4  , 44  ,  12   , 52  , 20  ,  60  , 28,
            35    , 3  , 43  ,  11  ,  51 ,  19   , 59  , 27,
            34    , 2  , 42   , 10   , 50 ,  18   , 58  , 26,
            33    , 1  , 41   ,  9   , 49 ,  17   , 57  , 25};
    vector<ll>ans;
    for(ll j=0;j<temp.size();j++){
        ans.push_back(a[temp[j]-1]);
    }
    return ans;
}
vector<ll>revi(vector<ll>&a){
    for(ll j=0;j<32;j++){
        swap(a[j],a[j+32]);
    }
    return a;
}
vector<ll>des(vector<ll>inp,vector<ll>key,int enc){
    if(enc==1){
        vector<ll>ans=inp;
        key=PC1(key);
        vector<vector<ll>>fkey=gen_key(key);
        ans=IP(ans);
        for(ll j=0;j<ROUND;j++){
            ans=round_output(ans,fkey[j]);
        }
        vector<ll>fans=revi(ans);
        ans=IP_inverse(fans);
        return ans;
    }
    else{
        vector<ll>ans=inp;
        key=PC1(key);
        vector<vector<ll>>fkey=gen_key(key);
        reverse(fkey.begin(),fkey.end());
        ans=IP(ans);
        for(ll j=0;j<ROUND;j++){
            ans=round_output(ans,fkey[j]);
        }
        vector<ll>fans=revi(ans);
        ans=IP_inverse(fans);
        return ans;
    }
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif
    vector<ll>ans=des({0,0,0,0,0,0,0,1,0,0,1,0,0,0,1,1,0,1,0,0,0,1,0,1,0,1,1,0,0,1,1,1,1,0,0,0,1,0,0,1,1,0,1,0,1,0,1,1,1,1,0,0,1,1,0,1,1,1,1,0,1,1,1,1},{0,0,0,1,0,0,1,1,0,0,1,1,0,1,0,0,0,1,0,1,0,1,1,1,0,1,1,1,1,0,0,1,1,0,0,1,1,0,1,1,1,0,1,1,1,1,0,0,1,1,0,1,1,1,1,1,1,1,1,1,0,0,0,1},1);
    for(ll j:ans){
        cout<<j<<" ";
    }
}
