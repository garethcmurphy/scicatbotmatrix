#!/usr/bin/env bash

curl -vvv -XPOST -d '{"type":"m.login.password", "user":"scicatbot", "password":"scicatbot"}' "https://scitest.esss.lu.se/_matrix/client/r0/login"
