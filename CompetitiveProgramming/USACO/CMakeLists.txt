cmake_minimum_required(VERSION 3.29)
project(USACO)

set(CMAKE_CXX_STANDARD 20)

add_executable(USACO main.cpp usaco_utils.h
        general/basketBallOneOne.cpp)
