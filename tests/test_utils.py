
class TestClient:

    def test_get_and_server_responsed_error(self, client):
        resp = client.get('https://test-for-error')
        assert resp == {}

    def test_get_and_value_error_with_man_retry(self, client):
        resp = client.get('https://test-for-error', error='ValueError')
        assert resp == {}

    def test_get_and_httplib_incomplete_read(self, client):
        resp = client.get('https://test-for-error', error='IncompleteRead')
        assert resp == {}

    def test_get_and_keep_retry_error(self, client):
        resp = client.get('https://test-for-error', error='RetryError')
        assert resp is None

    def test_get_stream(self, client):
        resp = client.get_stream('https://test-for-get-stream')
        assert resp.ok