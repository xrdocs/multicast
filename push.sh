#!/bin/sh

setup_git() {
  git config --global user.email "lambrosgavogiannis1@hotmail.com"
  git config --global user.name "lambros90"
}

commit_website_files() {
  git checkout -b test-travis
  touch test.py
  git add test.py
  git commit --message "Travis build: $TRAVIS_BUILD_NUMBER"
}

upload_files() {
  git remote add origin-pages https://${GH_TOKEN}@github.com/MVSE-outreach/resources.git > /dev/null 2>&1
  git push --quiet --set-upstream origin-pages gh-pages 
}

setup_git
commit_website_files
upload_files