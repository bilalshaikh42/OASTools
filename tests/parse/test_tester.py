import pytest
import oastools.utils as utils
import oastools.test as test


def test_tester():

    spec = utils.parse_file("../fixtures/spec/DatanatorAPI.yaml")
    spec = test.swagger_test(oas_spec=spec, app_url="http://0.0.0.0:8080")
    # print(spec.paths.keys())
    # print(spec.generated_operation)
    print(spec)
    print("hello")


if __name__ == "__main__":
    test_tester()
