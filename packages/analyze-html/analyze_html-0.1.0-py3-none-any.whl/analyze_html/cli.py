import typer
from analyze_html.scrap import get_html,count_tag

app = typer.Typer()

@app.command()
def generate_html(url,save_to_local:bool=typer.Option(default=False)):
    html = get_html(url)
    if save_to_local:
        with open("file.html","w",encoding="utf-8") as file:
            file.write(html)
            file.close()
        print("HTML saved to file.html")
    print("HTML ok")

@app.command()
def count_tag_from_url(tag,url):
    html = get_html(url)
    counter = count_tag(tag,html)
    print(f"{counter} of <{tag}> tag contained.")   

@app.command()
def count_tag_from_local(tag,file_html):
    with open(file_html,"r",encoding="utf-8") as file:
        html = file.read()
        file.close()
    counter = count_tag(tag,html)
    print(f"{counter} of <{tag}> tag contained.")   
    