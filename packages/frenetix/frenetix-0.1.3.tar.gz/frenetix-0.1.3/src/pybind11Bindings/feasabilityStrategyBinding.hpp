#pragma once

//pybind includes
#include <pybind11/numpy.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/eigen.h>

#include "strategies/FeasabilityStrategy.hpp"
#include "trajectoryFunctionsBinding/feasabilityFunctionsBinding.hpp"

namespace py = pybind11;

namespace plannerCPP
{

    void initBindFeasabilityStrategy(pybind11::module &m);

} //plannerCPP

