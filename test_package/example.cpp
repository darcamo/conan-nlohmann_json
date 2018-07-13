#include <nlohmann/json.hpp>
#include <iostream>


// for convenience
using json = nlohmann::json;

int main() {
    // instead, you could also write (which looks very similar to the JSON above)
    json j = {
        {"pi", 3.141},
        {"happy", true},
        {"name", "Niels"},
        {"nothing", nullptr},
        {"answer", {
                {"everything", 42}
            }},
        {"list", {1, 0, 2}},
        {"object", {
                {"currency", "USD"},
                {"value", 42.99}
            }}
    };

    std::cout << j << std::endl;

    return 0;
}
