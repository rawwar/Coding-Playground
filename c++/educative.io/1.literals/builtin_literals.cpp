#include <iostream>
#include <chrono>

using namespace std::literals::chrono_literals;

int main()
{
    std::cout << std::endl;

    typedef std::chrono::duration<long long, std::ratio<2700>> hour;
    auto schoolHour = hour(1);
    auto shortBreak = 300s;
    auto longBreak = 0.25h;
    auto schoolWay = 15min;
    auto homework = 2h;

    auto schoolDayInSeconds = 2 * schoolWay + 6 * schoolHour + 4 * shortBreak + longBreak + homework;

    std::cout << "School day in Seconds : " << schoolDayInSeconds.count() << std::endl;
    std::chrono::duration<double, std::ratio<3600>> schoolDayInHours = schoolDayInSeconds;
    std::chrono::duration<double, std::ratio<60>> schoolDayInMinutes = schoolDayInSeconds;
    std::chrono::duration<double, std::ratio<1, 1000>> schoolDayInMilliseconds = schoolDayInSeconds;

    std::cout << "School day in hours: " << schoolDayInHours.count() << std::endl;
    std::cout << "School day in minutes: " << schoolDayInMinutes.count() << std::endl;
    std::cout << "School day in milliseconds: " << schoolDayInMilliseconds.count() << std::endl;
}