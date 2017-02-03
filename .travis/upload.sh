#!/bin/bash

set -e
set -x

if [[ "$(uname -s)" == 'Darwin' ]]; then
    if which pyenv > /dev/null; then
        eval "$(pyenv init -)"
    fi
    pyenv activate conan
fi

if [[ "$(uname -s)" == 'Linux' ]]; then
    CC=$C_COMPILER
    CXX=$CXX_COMPILER
fi

conan user filonovpv -p $CONAN_PASSWORD -r conan.io
conan copy hello/0.1@demo/testing filonovpv/testing --all
conan upload hello/0.1@filonovpv/testing --all -r conan.io
