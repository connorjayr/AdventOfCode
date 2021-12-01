#include <algorithm>
#include <list>
#include <iostream>
#include <unordered_map>

using namespace std;

int main() {
  list<int> cups = {5,8,3,9,7,6,2,4,1};
  int min_cup = 1;
  int max_cup = 9;
  while (cups.size() < 1000000) {
    cups.push_back(max_cup++ + 1);
  }
  // cout << max_cup << endl;

  unordered_map<int, list<int>::iterator> find_map;
  for (list<int>::iterator itr = cups.begin(); itr != cups.end(); ++itr) {
    find_map[*itr] = itr;
  }
  list<int>::iterator current_itr = cups.begin();
  for (int i = 0; i < 10000000; ++i) {
    list<int>::iterator erase_itr = current_itr;
    ++erase_itr;
    if (erase_itr == cups.end()) {
      erase_itr = cups.begin();
    }

    int r1 = *erase_itr;
    erase_itr = cups.erase(erase_itr);
    if (erase_itr == cups.end()) {
      erase_itr = cups.begin();
    }
    int r2 = *erase_itr;
    erase_itr = cups.erase(erase_itr);
    if (erase_itr == cups.end()) {
      erase_itr = cups.begin();
    }
    int r3 = *erase_itr;
    erase_itr = cups.erase(erase_itr);
    if (erase_itr == cups.end()) {
      erase_itr = cups.begin();
    }

    int dest_label = *current_itr - 1;
    while (dest_label == r1 || dest_label == r2 || dest_label == r3 || dest_label < min_cup) {
      --dest_label;
      if (dest_label < min_cup) {
        dest_label = max_cup;
      }
    }
    list<int>::iterator dest_itr = find_map[dest_label];
    ++dest_itr;
    find_map[r1] = cups.insert(dest_itr, r1);
    find_map[r2] = cups.insert(dest_itr, r2);
    find_map[r3] = cups.insert(dest_itr, r3);

    ++current_itr;
    if (current_itr == cups.end()) {
      current_itr = cups.begin();
    }
    // if (i % 1000 == 0) {
    //   cout << i << endl;
    // }
  }

  list<int>::iterator one_itr = find(cups.begin(), cups.end(), 1);
  ++one_itr;
  if (one_itr == cups.end()) {
    one_itr = cups.begin();
  }
  int v1 = *one_itr;
  ++one_itr;
  if (one_itr == cups.end()) {
    one_itr = cups.begin();
  }
  int v2 = *one_itr;
  for (int cup : cups) {
    cout << cup;
  }
  cout << endl;
  std::cout << ((long long) v1 * (long long) v2) << std::endl;
}
