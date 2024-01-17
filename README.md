# Structuring-Python-projects-Basic
Organizing Python projects is essential for ensuring smooth internal functionality and facilitating distribution to other users in the form of packages. Personally, I find a well-designed project structure to be imperative for effective packaging.

If you're unfamiliar with the concepts of modules/packages and the intricacies of the import operation, a comprehensive guide is available to help you navigate these aspects.
README.rst
LICENSE
setup.py
requirements.txt
sample/__init__.py
sample/core.py
sample/helpers.py
docs/conf.py
docs/index.rst
tests/test_basic.py
tests/test_advanced.py
Let’s get into some specifics.

The Actual Module
Location	./sample/ or ./sample.py
Purpose	The code of interest
Your module package is the core focus of the repository. It should not be tucked away:

./sample/
If your module consists of only a single file, you can place it directly in the root of your repository:

./sample.py
Your library does not belong in an ambiguous src or python subdirectory.

License
Location	./LICENSE
Purpose	Lawyering up.
This is arguably the most important part of your repository, aside from the source code itself. The full license text and copyright claims should exist in this file.

If you aren’t sure which license you should use for your project, check out choosealicense.com.

Of course, you are also free to publish code without a license, but this would prevent many people from potentially using or contributing to your code.

Setup.py
Location	./setup.py
Purpose	Package and distribution management.
If your module package is at the root of your repository, this should obviously be at the root as well.

Requirements File
Location	./requirements.txt
Purpose	Development dependencies.
A pip requirements file should be placed at the root of the repository. It should specify the dependencies required to contribute to the project: testing, building, and generating documentation.

If your project has no development dependencies, or if you prefer setting up a development environment via setup.py, this file may be unnecessary.

Documentation
Location	./docs/
Purpose	Package reference documentation.
There is little reason for this to exist elsewhere.

Test Suite
For advice on writing your tests, see Testing Your Code.

Location	./test_sample.py or ./tests
Purpose	Package integration and unit tests.
Starting out, a small test suite will often exist in a single file:

./test_sample.py
Once a test suite grows, you can move your tests to a directory, like so:

tests/test_basic.py
tests/test_advanced.py
Obviously, these test modules must import your packaged module to test it. You can do this a few ways:

Expect the package to be installed in site-packages.
Use a simple (but explicit) path modification to resolve the package properly.
I highly recommend the latter. Requiring a developer to run setup.py develop to test an actively changing codebase also requires them to have an isolated environment setup for each instance of the codebase.

To give the individual tests import context, create a tests/context.py file:

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import sample
Then, within the individual test modules, import the module like so:

from .context import sample
This will always work as expected, regardless of installation method.

Some people will assert that you should distribute your tests within your module itself – I disagree. It often increases complexity for your users; many test suites often require additional dependencies and runtime contexts.

Makefile
Location	./Makefile
Purpose	Generic management tasks.
If you look at most of my projects or any Pocoo project, you’ll notice a Makefile lying around. Why? These projects aren’t written in C… In short, make is an incredibly useful tool for defining generic tasks for your project.

Sample Makefile:

init:
    pip install -r requirements.txt

test:
    py.test tests

.PHONY: init test
Other generic management scripts (e.g. manage.py or fabfile.py) belong at the root of the repository as well
