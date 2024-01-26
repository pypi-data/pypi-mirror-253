# MakeShift

MakeShift is a tool for making procedurally generated text based on pre-defined phrase templates. 

This package includes a simple specification for how to write MakeShift-style phrase templates and an interpreter for generating text from those templates.

MakeShift is designed for dungeon masters, writers and storytellers of all kinds to find inspiration when making new `{ characters | settings | stories | worlds | anything }`.

## Installation

MakeShift can be installed from [PyPi](https://pypi.org/project/makeshift/) using Pip. I recommend doing this in a [Python virtual environment](https://docs.python.org/3/tutorial/venv.html).
```bash
> pip install makeshift
```

You can call `makeshift` from the command-line and provide a phrase template file to generate a random result.
```bash
> makeshift /path/to/file/my_template.txt
```

You can also download the MakeShift repository from [https://github.com/MJoseph1234/makeshift](https://github.com/MJoseph1234/makeshift)

There's a number of template files in the `examples/` directory of the repository. You can expand on those or use them as a blueprint to write your own.