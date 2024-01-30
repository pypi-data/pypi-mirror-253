<h1 align="center">
<img src="https://documentation.smartmt.com/MastaAPI/13.0/images/smt_logo.png" width="150" alt="SMT"><br>
<img src="https://documentation.smartmt.com/MastaAPI/13.0/images/MASTA_13_logo.png" width="400" alt="Mastapy" style="padding-top: 15px">
</h1><br>

[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Mastapy is the Python scripting API for MASTA.

- **Website**: https://www.smartmt.com/
- **Support**: https://support.smartmt.com/
- **Documentation**: https://documentation.smartmt.com/MastaAPI/13.0/


### Features

- Powerful integration with MASTA with the ability to run Python scripts from the MASTA interface directly.
- Ability to use MASTA functionality external to the MASTA software in an independent script.
- An up-to-date and tight integration with Python. This is not a lightweight wrapper around the C# API. It is specifically designed for Python and works great in tandem with other common scientific Python packages (e.g. SciPy, NumPy, Pandas, Matplotlib, Seaborn, etc.)
- Extensive backwards compatibility support. Scripts written in older versions of mastapy will still work with new versions of MASTA.

### Release Information

#### Major Changes
- Added support for Python 3.9, 3.10, 3.11 and 3.12.
- Debugging scripts from within MASTA has been greatly simplified. The old `mastapy.start_debugging` method has been deprecated and replaced by a "Calculate (Debug)" button on scripted properties.
- Performance has been greatly improved. All imports within mastapy are lazily evaluated and `typing.TYPE_CHECKING` has been used extensively internally to mask out imports only used for typing purposes.
- The package has been modernised. Packages now include a `pyproject.toml` file introduced in PEP 518 and are formatted using Black.
  
#### Minor Changes
- Adds lazy type checking to all applicable methods and properties. Type checking is only triggered if a TypeError or ValueError is raised. If an incorrect type is detected, a TypeCheckException will be raised.
- Adds `typing.Optional[bool]` and `typing.Optional[float]` as valid return types from MASTA properties.
- The old `cast` method has been deprecated in favour of the new `cast_to` property.
- Method and property documentation now has the return type on the first line.
- Adds support for a `MASTA_DIRECTORY` environment variable, which can be set to the path to your MASTA directory. If the environment variable is set, mastapy will automatically initialise using it.
- Adds `mastapy.masta_licences` which can be used as either a decorator or context manager to acquire and remove licences.
- Lots of bug fixes.