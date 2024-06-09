#include <iostream>
#include <string>
#include <cstring>
using namespace std;

// Functions
string *split(string main_string, string sep_char);

int main()
{
    int num;
    cin >> num;
    getchar(); // get the enter

    string words_list;
    getline(cin, words_list);
    string main_string;
    getline(cin, main_string);
    string *ptr = split(words_list, ","); // split words and index them in ptr

    for (int j = 0; j < num; j++)
    {
        string word = *(ptr + j);
        string star_str = "";
        for (int i = 0; i < 2 * word.length(); i++) // make the word with stars
        {
            star_str += "*";
        }

        // replace all words which is in ptr with stars
        int index = main_string.find(word);
        while (index != string::npos)
        {
            if ((isalpha(main_string[index + word.length()])) || (isalpha(main_string[index - 1]))) // check : after or before the word is alphabet or not
            {
                index = main_string.find(word, index + 1);
            }
            else
            {
                main_string.replace(index, word.length(), star_str);
                index = main_string.find(word, index + 1);
            }
        }
    }
    cout << main_string << endl;
    return 0;
}

string *split(string main_string, string sep_char) // split list of words by sep_char and return an array
{
    static string List[100];
    int i = 0, start = 0;
    int pos = main_string.find(sep_char);
    while (pos != -1)
    {
        List[i] = main_string.substr(start, pos - start);
        start = pos + sep_char.size();
        pos = main_string.find(sep_char, start);
        i++;
    }
    List[i] = main_string.substr(start, pos - start);
    return List;
}
