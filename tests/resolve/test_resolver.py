import pytest
import os.path
import oastools.resolve as resolve
import oastools.parse as parse


@pytest.fixture(scope="module")
def spec(path="./tests/fixtures/spec/root.yaml"):
    path = os.path.abspath(path)
    parsed = parse.OpenApiParser(path=path).spec
    return parsed


def test_traverse(spec):
    rootpath = os.path.abspath("./tests/fixtures/spec/")
    print(spec)
    print("+++++++++++++++++++++++=")
    parsed = resolve.traverse(spec, rootpath)
    print(parsed)
    assert(False)


if __name__ == "__main__":
    pytest.main()
