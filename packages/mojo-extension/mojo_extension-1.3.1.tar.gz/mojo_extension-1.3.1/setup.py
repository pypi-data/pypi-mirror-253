# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'source/packages'}

packages = \
['mojo', 'mojo.extension']

package_data = \
{'': ['*']}

install_requires = \
['mojo-startup>=1.3.1,<1.4.0']

setup_kwargs = {
    'name': 'mojo-extension',
    'version': '1.3.1',
    'description': 'Automation Mojo Extension Package',
    'long_description': '=================================\nAutomation Mojo Extension Package\n=================================\n\nThis is a python package that provides a mechanism for extending other python packages.  This\npackage is different from other python extension packages in that it uses the python Protocol type\nto query for a type.\n\nFor example, if we want to be able to create instance of object like these from a factory.\n\n.. code:: python\n\n    class Hey:\n        def __str__(self):\n            return "Hey"\n\n    class Ho:\n        def __str__(self):\n            return "Ho"\n\n\n    class MyExtTypeProtocol(ExtProtocol):\n\n        ext_protocol_name = "mojo-myextypeprotocol"\n\n        @classmethod\n        def give_me_a_hey(cls):\n            ...\n\n        @classmethod\n        def give_me_a_ho(cls):\n            ...\n\n    class MyExtTypeFactory(ExtFactory, MyExtTypeProtocol):\n\n        @classmethod\n        def give_me_a_hey(cls):\n            return Hey\n        \n        @classmethod\n        def give_me_a_ho(cls):\n            return Ho\n\n\nThen what we do i we register the module where the type is found.\n\n.. code:: python\n\n    from mojo.extension.extensionconfiguration import ExtensionConfiguration\n    from mojo.extension.wellknown import ConfiguredSuperFactorySingleton\n\n    ExtensionConfiguration.CONFIGURED_FACTORY_MODULES = [\n            "myextinst",\n            "myexttype"\n        ]\n\n\nThen we get an instance of the super factory singleton.\n\n.. code:: python\n\n    from mojo.extension.wellknown import ConfiguredSuperFactorySingleton\n\n    superfactory = ConfiguredSuperFactorySingleton()\n\n\nThen when we want to get the type from the extension, we utilize the protocol that\nwas declared and ask for the type using the function on the protocol that will return\nthe type.\n\n.. code:: python\n\n    hey_type = self._super_factory.get_override_types_by_order(MyExtTypeProtocol.give_me_a_hey)\n    ho_type = self._super_factory.get_override_types_by_order(MyExtTypeProtocol.give_me_a_ho)\n\n    hey = hey_type()\n    ho = ho_type()\n\n    print("")\n    print(f"{hey}... {ho}... {hey}... {ho}...")\n\n\n==========\nReferences\n==========\n\n- `User Guide <userguide/userguide.rst>`_\n- `Coding Standards <userguide/10-00-coding-standards.rst>`_\n',
    'author': 'Myron Walker',
    'author_email': 'myron.walker@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'http://automationmojo.com',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
