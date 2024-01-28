from reqflow import Client, given



def test_new():

    client = Client(base_url="https://httpbin.org")
    r = given(client).when("GET", "/get").then().get_content()
    print(r)
