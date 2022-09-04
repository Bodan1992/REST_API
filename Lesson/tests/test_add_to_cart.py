import os

from uuid import uuid4
from Lesson.utils.sessions import demoqa


def test_add_to_cart_unauthorized():
    response = demoqa().post(
        '/addproducttocart/catalog/31/1/1',
        cookies={'Nop.customer': 'ba141d9f-5ea3-44f0-91d0-9066a2a3b5dd;'}
    )
    assert response.status_code == 200
    assert response.json()['success'] is True
    assert response.json()['message'] == 'The product has been added to your <a href=\"/cart\">shopping cart</a>'


def test_add_to_cart_unauthorized_one_product():
    response = demoqa().post(
        '/addproducttocart/catalog/31/1/1',
        cookies={'Nop.customer': str(uuid4())}
    )
    assert response.status_code == 200
    assert response.json()['success'] is True
    assert response.json()['message'] == 'The product has been added to your <a href=\"/cart\">shopping cart</a>'
    assert response.json()['updatetopcartsectionhtml'] == '(1)'


def test_add_to_cart_authorized(demoqa_authorized):

    response = demoqa_authorized.post('/addproducttocart/catalog/31/1/1',)

    assert response.status_code == 200
    assert response.json()['success'] is True
    assert response.json()['message'] == 'The product has been added to your <a href=\"/cart\">shopping cart</a>'
    assert response.json()['updatetopcartsectionhtml'] == '(1)'


#
# def test_add_to_cart_authorized():
#
#     aut_cookie_name = 'NOPCOMMERCE.AUTH'
#     login = os.getenv('user_login')
#     password = os.getenv('user_password')
#
#     response = demoqa().post('/login', data={'email': login, 'password': password},
#                              allow_redirects=False)
#     auth_cookie_value = response.cookies.get(aut_cookie_name)
#     # print(auth_cookie_value)
#     response = demoqa().post('/addproducttocart/catalog/31/1/1',
#                              cookies={aut_cookie_name: auth_cookie_value}
#                              )
#
#     assert response.status_code == 200
#     assert response.json()['success'] is True
#     assert response.json()['message'] == 'The product has been added to your <a href=\"/cart\">shopping cart</a>'
#     assert response.json()['updatetopcartsectionhtml'] == '(1)'
"""
LOGIN="andy123munik@gmail.com"
PASSWORD="123456"
"""
