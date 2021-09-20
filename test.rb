#!/usr/bin/ruby

rc = system('bash -c "set -o pipefail; echo aaa; false | echo bbb"')

