import typer

app = typer.Typer()

from georgia.scrap import *

@app.command()
def generate_html(url):
    html = get_html(url)
    print(f"HTML generated")

@app.command()
def get_all_profile(url, print_all:bool=False):
    profile_urls = all_profile(url)
    count_urls = len(profile_urls)
    print(f"Getting {count_urls} of profile links")
    if print_all:
        print(profile_urls)   

@app.command()
def get_number(text:str):
    numb = value_contact(text)
    print(f"from {text} get {numb}")