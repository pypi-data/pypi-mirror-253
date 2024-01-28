"""
.. module:: overridevariables
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module that contains the ExtensionConfiguration variables.

.. moduleauthor:: Myron Walker <myron.walker@gmail.com>
"""

__author__ = "Myron Walker"
__copyright__ = "Copyright 2023, Myron W Walker"
__credits__ = []
__version__ = "1.0.0"
__maintainer__ = "Myron Walker"
__email__ = "myron.walker@gmail.com"
__status__ = "Development" # Prototype, Development or Production
__license__ = "MIT"

import os

from mojo.star import StartupConfigSingleton

my_config = {}

startup_config = StartupConfigSingleton()
if "MOJO-EXTENSION" in startup_config:
    my_config = startup_config["MOJO-EXTENSION"]

class ExtensionConfiguration:

    MJR_CONFIGURED_FACTORY_MODULES = []

    # For the `MJR_CONFIGURED_FACTORY_MODULES` variable, if we find it in the environment,
    # then the value set in the environment takes precedence over any value that might be
    # found in a configuration file.
    if "MJR_CONFIGURED_FACTORY_MODULES" in os.environ:
        modules_as_path = os.environ["MJR_CONFIGURED_FACTORY_MODULES"]
        MJR_CONFIGURED_FACTORY_MODULES = set([m.strip() for m in modules_as_path.split(",")])

    # Else, If the `MJR_CONFIGURED_FACTORY_MODULES` was not found in the environment, but was
    # found in the startup configuration file.  Then we 
    elif "MJR_CONFIGURED_FACTORY_MODULES" in my_config:
        modules_as_path = my_config["MJR_CONFIGURED_FACTORY_MODULES"]
        MJR_CONFIGURED_FACTORY_MODULES = set([m.strip() for m in modules_as_path.split(",")])

    
