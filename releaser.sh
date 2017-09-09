#!/usr/bin/env bash

GH=https://github.com/Saphyel/ipteller/compare/
LAST_TAG=`git describe --tags --abbrev=0 HEAD^`

printf "**Changelog** (since "${GH}${LAST_TAG}"...NEW)\n" > CHANGELOG.md
git log ${LAST_TAG}..HEAD --pretty=format:"* %s" >> CHANGELOG.md
printf "\n" >> CHANGELOG.md
