# -*- coding: utf-8 -*-
#
# Copyright (C) 2008-2023 EDF R&D
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307 USA
#
# See http://www.salome-platform.org/ or email : webmaster.salome@opencascade.com
#
# Author: Jean-Philippe Argaud, jean-philippe.argaud@edf.fr, EDF R&D

# from distutils.core import setup
from setuptools import setup, find_packages

from adao.daCore.version import version

# read the contents of README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.txt')) as f:
    long_description = f.read()

setup(
    name = "adao",
    packages = [
        "adao",
        "adao/daAlgorithms",
        "adao/daAlgorithms/Atoms",
        "adao/daCore",
        "adao/daEficas",
        "adao/daEficasWrapper",
        "adao/daGUI",
        "adao/daGuiImpl",
        "adao/daNumerics",
        "adao/daNumerics/Gnuplot",
        "adao/daUtils",
        "adao/daYacsIntegration",
        "adao/daYacsSchemaCreator",
        ],
    install_requires=['numpy', 'scipy'],
    python_requires='>=3.6',
    version = version,
    description = "A module for Data Assimilation and Optimization",
    author = "Jean-Philippe Argaud",
    author_email = "jean-philippe.argaud@edf.fr",
    url = "http://www.salome-platform.org/",
    license = "GNU Library or Lesser General Public License (LGPL)",
    keywords = [
        "optimization", "data assimilation", "calibration", "interpolation",
        "reduction", "inverse problem", "tunning", "sampling", "minimization",
        "black-box", "checking", "3D-Var", "4D-Var", "Filtering", "Kalman",
        "Ensemble", "Regression", "Quantile", "V&V", "Tabu Search", "BLUE",
        "EnKF", "Ensemble Kalman Filter", "PSO", "Particle Swarm Optimization",
        "UKF", "Unscented Kalman Filter", "Least Squares", "Unscented", "EIM",
        "DFO", "Derivative Free Optimization", "Swarm", "Optimal Positioning",
        "Gradient Test", "Adjoint Test", "Sensitivity", "Quantile Regression",
        ],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    long_description = long_description,
    long_description_content_type='text/x-rst'
)
