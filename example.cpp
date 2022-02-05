#include "pybind11/pybind11.h"
#include <windows.h>

namespace py = pybind11;

/*
int add(int i, int j) {
    return i + j;
}

PYBIND11_MODULE(example, m) {
    m.doc() = "pybind11 example plugin"; // optional module docstring

    m.def("add", &add, "A function which adds two numbers");
}
*/

int add(int i, int j){
    int z;
    Sleep(4000);
    z = i+j;
    return z;
}

PYBIND11_MODULE(example, m) {
    m.doc() = "pybind11 example plugin"; // optional module docstring

    m.def("add", &add, "A function which is providing the sizeof(int*)");
}