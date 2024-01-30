# pycounts_merete

Calculate word counts in a text file!


## Authors
Merete Lutz

## Installation

```bash
$ pip install pycounts_merete
```

## Usage

`pycounts_merete` can be used to count words in a text file and plot results
as follows:

```python
from pycounts_merete.pycounts_merete import count_words
from pycounts_merete.plotting import plot_words
import matplotlib.pyplot as plt

file_path = "test.txt"  # path to your file
counts = count_words(file_path)
fig = plot_words(counts, n=10)
plt.show()
```

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`pycounts_merete` was created by Merete Lutz. It is licensed under the terms of the MIT license.

## Credits

`pycounts_merete` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter). `pycounts_merete` was created following the tutorial created by Tomas Beuzen, licensed under the terms
of the MIT license. A link to the tutorial can be found [here](https://py-pkgs.org/03-how-to-package-a-python#put-your-package-under-version-control)
