#include <iostream>
#include <ctime>

int main() {

    srand(time(NULL));
    std::string password = "";

    std::cout << "-Password Generator-\n\n";

    int num;
    std::string characters = "abcdefghijklmnopqrstvwxyz123456789*/()!#_-^@$%&'";


    std::cout << "How long would you like the password to be?: ";
    std::cin >> num;

    while (num <= 5 || num >= 21)
    {
        if (num <= 5){
            std::cout << "The password has to be longer than 5 characters: ";
            std::cin >> num;
        }
        else{
            std::cout << "The password has to be shorter than 21 characters: ";
            std::cin >> num;
        }
        
    }
    
    for (size_t i = 0; i < num; i++)
    {
        password += characters[(rand() % characters.length())];
    }
    
    std::cout << "Your random password is: " << password;
    return 0;
}