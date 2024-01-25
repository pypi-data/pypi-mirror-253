# Publish instructions #

- bump version in `setup.py` file
- generate the api files with running this command at the root of the documentation project `openapi-generator generate -i specs/vy-openapi.yml -g python -o generated-clients/python --additional-properties generateSourceCodeOnly=true datetimeFormat='%Y-%m-%dT%H:%M:%S%z'`
- build python with `rm -rf build dist vayu.egg-info && python setup.py sdist bdist_wheel`
- upload to pipy with `twine upload --repository pypi dist/* -u __token__ -p your-token-here`
