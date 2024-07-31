#include <iostream>

#include <cstdio>

#include <cstdlib>

#include <cmath>

#include <cstring>

#include <numeric>

#include <algorithm>

#include <functional>

#include <vector>

#include <queue>

#include <stack>

#include <set>

#include <map>

#include <unordered_map>

#include <list>

#include <bitset>

#include <utility>

#include <cassert>

#include <iomanip>

#include <ctime>

#include <fstream>

#include <bitset>

 

using namespace std;

 

const int MAX_ELEMENTS = 500025;

 

int n;

int A[MAX_ELEMENTS];

int count_array[MAX_ELEMENTS];

set<int> not_active_set;

 

int main(int argc, const char * argv[]) {

 

  

   clock_t start_time = clock();

 

   scanf("%d", &n); 

   for(int i = 0; i < n; i ++)

       scanf("%d", &A[i]); 

   for(int i = 0; i < n + 1; i ++)

       not_active_set.insert(i + 1);

   int result = 0, ptr = 0;

   for(int i = 0; i < n; i ++){

       count_array[A[i]] ++;

       if(not_active_set.find(A[i]) != not_active_set.end())

           not_active_set.erase(A[i]);

       while(count_array[A[i]] > 1){

           count_array[A[ptr]] --;

           if(count_array[A[ptr]] == 0)

               not_active_set.insert(A[ptr]);

           ptr ++;

       }

       result = max(result, *(not_active_set.begin()) - 1);

   }

 

  

   clock_t end_time = clock();

 

   // Calculate and print the runtime in milliseconds

   double runtime_ms = double(end_time - start_time) / CLOCKS_PER_SEC * 1000.0;

   cout << "Runtime: " << runtime_ms << " ms" << endl;

 

   cout << result << endl;

 

   return 0;

}