import oastools.parse as parse


def test_parser():
    parsed = parse.OpenApiParser(path="./tests/fixtures/OpenAPI.yml")
    assert(isinstance(parsed.spec, dict))
