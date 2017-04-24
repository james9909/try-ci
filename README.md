# Try-Ci
You should try using continuous integration because...

[![Build Status](https://travis-ci.org/james9909/try-ci.svg?branch=master)](https://travis-ci.org/james9909/try-ci)

Table of Contents
=================
* [What is continuous integration?](#what-is-continuous-integration)
* [Why use continuous integration?](#why-use-continuous-integration)
* [How does it work?](#how-does-it-work)
* [Tools for CI](#tools-for-ci)
* [Best practices](#best-practices)

## What is continuous integration?
Continuous integration (CI) is a widespread software development practice that involves frequently committing code to a central repository.
Often refers to the build or integration stage of the software release process.
A major component of continuous integration is the use of automated test suites that are run to verify the integrity of the code being committed.
Many large-scale projects and organizations use continuous integration, including:
- NASA’s mission control framework
- React.js
- Vim
- MongoDB
- League of Legends

## Why use continuous integration?
- It allows developers to detect and locate the source of errors quickly
- Promotes collaboration between team members so recent code is always shared
- Reduces time and effort spent on integrating changes to the main code base
- Reduces overhead between the development and deployment processes
- Analyses and metrics generated from automated tests (including code coverage, code complexity, and linting) help keep a healthy codebase
- Code with confidence knowing that project standards are being adhered to and that the product is functioning

## How does it work?
![How Does it Work](https://raw.githubusercontent.com/james9909/try-ci/gh-pages/howDoesItWork.png)

## Tools for CI
#### Popular CI servers:
- [Travis](https://travis-ci.org)
- [Jenkins](https://jenkins.io/)
- [Gitlab](https://about.gitlab.com/)

#### Automated test tools:
- pytest, nose (Python)
- mocha (node.js)
- JUnit, Cactus (Java)

#### Automated build tools:
- Maven, ant, make, rake, gulp, grunt

## Best practices
- Use a version control system
- Use a standardized build script/tool that can be called from the command line
- Commit frequently
- Keep the builds relatively short (< 1 hour) and use parallel builds
- Test using a replica of the production environment
- Make it easy to view the results of a build

