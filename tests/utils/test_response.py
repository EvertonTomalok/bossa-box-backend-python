from src.utils.response import Response


def test_response_ok(snapshot):
    response = Response(code_status=200, data={"teste": True})
    snapshot.assert_match(response)


def test_response_not_ok(snapshot):
    response = Response(code_status=500, data={"teste": True})
    snapshot.assert_match(response)
