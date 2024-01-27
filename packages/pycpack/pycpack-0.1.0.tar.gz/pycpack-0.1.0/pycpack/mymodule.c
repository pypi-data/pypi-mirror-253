#include <Python.h>

// Define the actual function
int add(int a, int b) {
    return a + b;
}

double add_f(double a, double b){
    return a + b;
}

static PyObject *py_add(PyObject *self, PyObject *args) {
    int a, b;
    if (!PyArg_ParseTuple(args, "ii", &a, &b)) {
        return NULL;
    }
    return PyLong_FromLong(add(a, b));
}

static PyObject *py_add_f(PyObject *self, PyObject *args){
    double a, b;
    if (!PyArg_ParseTuple(args, "dd", &a, &b)) {
        return NULL;
    }
    return PyFloat_FromDouble(add_f(a, b));
}


static PyMethodDef methods[] = {
    {"add", py_add, METH_VARARGS, "Add two integers."},
    {"add_f", py_add_f, METH_VARARGS, "Add two floats."},
    {NULL, NULL, 0, NULL}  // Sentinel
};


// Define the module structure
static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "mymodule",  // Module name
    NULL,        // Documentation
    -1,          // Size of per-interpreter state or -1
    methods      // Method table
};

// Module initialization function
PyMODINIT_FUNC PyInit_mymodule(void) {
    return PyModule_Create(&module);
}



