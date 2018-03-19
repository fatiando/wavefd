#!/bin/bash
#
# Push the built HTML pages to the gh-pages branch.
#
# Keeps pages for releases in separate folvers. Pages for the master branch are
# in the 'dev' folder. 'latest' is a link to the last release.

# To return a failure if any commands inside fail
set -e
set -x

REPO=wavefd
USER=fatiando
BRANCH=gh-pages
CLONE_ARGS="--quiet --branch=$BRANCH --single-branch"
REPO_URL=https://${GH_TOKEN}@github.com/${USER}/${REPO}.git
CLONE_DIR=deploy
# Place the HTML is different folders for different versions
if [[ "${TRAVIS_TAG}" != "" ]]; then
    VERSION=${TRAVIS_TAG}
else
    VERSION=dev
fi

echo -e "DEPLOYING HTML TO GITHUB PAGES:"
echo -e "Target: branch ${BRANCH} of ${USER}/${REPO}"
echo -e "HTML dir: ${VERSION}"

# Clone the project, using the secret token.
# Uses /dev/null to avoid leaking decrypted key.
echo -e "Cloning ${USER}/${REPO}"
git clone ${CLONE_ARGS} ${REPO_URL} ${CLONE_DIR} 2>&1 >/dev/null

cd ${CLONE_DIR}

# Configure git to a dummy Travis user
git config user.email "travis@nothing.com"
git config user.name "TravisCI"

# Delete all the files and replace with our new  set
echo -e "Remove old files from previous builds"
rm -rf ${VERSION}
cp -Rf ${TRAVIS_BUILD_DIR}/doc/_build/html/ ${VERSION}/

# Need to have this file so that Github doesn't try to run Jekyll
touch .nojekyll

if [[ "${VERSION}" != "dev" ]]; then
    echo -e "Setup link from ${VERSION} to 'latest'"
    rm -f latest
    ln -sf ${VERSION} latest
fi

echo -e "Add and commit changes"
git add -A .
git status
if [[ "${VERSION}" == "dev" && `git log -1 --format='%s'` == *"dev"* ]]; then
    # If this is a dev build and the last commit was from a dev build, reuse
    # the same commit
    echo -e "Amending last commit"
    git commit --amend --reset-author --no-edit
else
    # Make a new commit
    echo -e "Making a new commit"
    git commit -m "Deploy $VERSION from TravisCI"
fi

echo -e "Pushing..."
git push -fq origin $BRANCH 2>&1 >/dev/null

echo -e "Finished uploading generated files."

# Workaround for https://github.com/travis-ci/travis-ci/issues/6522
# Turn off exit on failure.
set +x
set +e
