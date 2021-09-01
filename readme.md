# python-app-sample

## python virtual environment

```bash
  virtualenv --python=python3 .venv
```

## install requirements

```bash
  source ./.venv/bin/activate
  pip install -r requirements.txt
```

## Running Tests

To run tests, run the following command

```bash
  make test
```

## build

To build app, run the following command

```bash
  make
```

## run

To run tests, run the following command

```bash
  docker run -it --rm python-app-sample:1.0.0.dev
```
