# Doppler-Injector

Simple function to inject [Doppler](https://dashboard.doppler.com/) secrets into virtual environment.

## !!!NOT TESTED!!!

Do not install! Hasn't been tested. Publishing for personal use. Will create test and fortify.

In the meantime, just follow [Doppler-env](https://github.com/dopplerhq/python-doppler-env#setup) set-up.

## SETUP

First, define the `DOPPLER_ENV` environment variable in your IDE, editor, or terminal to trigger the injection of secrets:
```bash
export DOPPLER_ENV=1
```

You can enable logging for troubleshooting purposes by setting the `DOPPLER_ENV_LOGGING` environment variable:
```bash
export DOPPLER_ENV_LOGGING=1
```

Then configure which secrets to fetch for your application by either using the CLI in the root directory of your application:
```bash
doppler setup
```
