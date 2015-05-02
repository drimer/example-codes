#!/bin/bash

set -e

THIS_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

pushd ${THIS_DIR} >> /dev/null

python manage.py runserver 8000

popd >> /dev/null