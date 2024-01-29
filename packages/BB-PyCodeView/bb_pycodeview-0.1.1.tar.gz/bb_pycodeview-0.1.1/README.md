# BB-PyCodeView

> View syntax highlighted code from a filename or module name

### Options

```console
$ code-view --help

    code-view - view highlighted python code

    ( -c |    --comments     ):  Show comments in output
                                  - default = False
    ( -f |    --function     ):  Function name - same as adding ':function' after module name
    ( -H |      --html       ):  Output an html string
    ( -h |      --help       ):  Print help message
    ( -m |     --module      ):  View code from a module
                                  - will attempt to automagically parse this without the option given
    ( -n | --no-highlighting ):  Disable syntax highlighting in output
                                  - only effects output - string data is still processed
                                  - default = False
    ( -p |    --filepath     ):  View file contents
                                  - path can also be provided without this option
    ( -s |     --string      ):  Code view from a provided string

```

>   If the options `-p|--filepath`, `-m|--module`, or `-f|--function` are ommitted, it will attempt to automatically assign
> the arguments properly. May not work depending on the module name/path. Pathnames are almost guaranteed to work on their own.

### TODO

- theming

## ChangeLog

##### v0.1.0
    - initial release

##### v0.1.1
    - added html output
    - added licenses
