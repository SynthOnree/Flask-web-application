# Tests for your routes go here

# === Example Code Below ===

"""
GET /emoji
"""
def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)"

# File: tests/test_app.py


"""
When: I make a POST request to /count_vowels
And: I send "eee" as the body parameter text
Then: I should get a 200 response with 3 in the message
"""
def test_post_count_vowels_eee(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eee'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 3 vowels in "eee"'

"""
When: I make a POST request to /count_vowels
And: I send "eunoia" as the body parameter text
Then: I should get a 200 response with 5 in the message
"""
def test_post_count_vowels_eunoia(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eunoia'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 5 vowels in "eunoia"'

"""
When: I make a POST request to /count_vowels
And: I send "mercurial" as the body parameter text
Then: I should get a 200 response with 4 in the message
"""
def test_post_count_vowels_mercurial(web_client):
    response = web_client.post('/count_vowels', data={'text': 'mercurial'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 4 vowels in "mercurial"'

"""
POST sort-names
Expected response (sorted list of names):
"Alice,Joe,Julia,Kieran,Zoe"
"""
def test_sort_names(web_client):
    response = web_client.post('/sort-names', data={'name': 'Alice,Charlie,Ben'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Alice,Ben,Charlie"

"""
GET /names?add=Eddie
Expected response (2OO OK):
Julia, Alice, Karim, Eddie
"""
def test_add_Eddie(web_client):
    response = web_client.get("/names?add=Eddie")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Julia, Alice, Karim, Eddie"



# === End Example Code ===
