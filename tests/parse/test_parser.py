import pytest
import oastools.parse as parse


@pytest.fixture
def parser(path="./tests/fixtures/OpenAPI.yml"):
    parser = parse.OpenApiParser(path=path)
    return parser


def test_parser(parser):
    assert(isinstance(parser.spec, dict))
    spec = parser.spec
    assert(spec["info"]["title"] == "API Title")
    assert(spec["openapi"] == "3.0.2")
    assert(spec["paths"]["/test"]["get"] ==
           {"responses": {"200": {"description": "OK"}}})


def test_new_parser(parser):
    spec = parse.OASParser(parser.spec)
    print(spec.base_path)
