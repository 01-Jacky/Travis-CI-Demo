# Travis-CI-Demo
> Template to get a basic Travis CI running with unit test and style/static checks. 

[![Build Status](https://travis-ci.com/01-Jacky/Travis-CI-Demo.svg?branch=master)](https://travis-ci.com/01-Jacky/Travis-CI-Demo)

## Getting Started
### Installing
Python3.8
```
pip install -r requirements.txt
```

## Running the tests
```
python -m pytest tests
coverage run --source=sample -m pytest tests && coverage report
```

### And coding style tests
```
isort --check-only -rc sample && black --check sample && flake8 sample && mypy sample
```

## Using Travis-CI
Authorize Travis and add config: https://docs.travis-ci.com/user/tutorial/ 

Embed your badge https://docs.travis-ci.com/user/status-images/

Now each commit should trigger a build

## Authors
* **Jacky Lee** - [01-Jacky](https://github.com/01-Jacky)

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details