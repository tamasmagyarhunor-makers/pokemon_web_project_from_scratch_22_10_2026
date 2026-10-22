from playwright.sync_api import Page, expect

def test_get_pokemons(db_connection, page, test_web_address):
    db_connection.seed("seeds/pokemon_seed.sql")

    page.goto(f"http://{test_web_address}/pokemons")

    list_items = page.locator("li")

    expect(list_items).to_have_text([
        "Pikachu, electric",
        "Charmander, fire",
        "Bulbasaur, water-earth",
        "MewTwo, psychio"
    ])

