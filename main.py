from markdown2 import markdown_path as md
from datetime import datetime as dt

pre = """<!DOCTYPE html>
<html>
    <head>
        <meta name="viewport" content="width=device-width,initial-scale=1.0,minimum-scale=1"><title>Youshitsune</title>
        <meta property="og:title" content="Youshitsune">
        <meta property="og:type" content="website">


        <meta property="og:image" content="/img/avatar.png">

        <link rel="me" href="https://tilde.town/@youshitsune">

        <link rel="stylesheet" href="/css/bootstrap.min.css">
        <link rel="stylesheet" href="/css/animate.min.css">
        <link rel="stylesheet" href="/css/style.css">
    </head>
    <body>
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark sticky-top">
            <div class="container-fluid">
                <a class="navbar-brand" href="#"><img src="/img/avatar.png" alt="" width="30" height="30">  Youshitsune</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
                        <li class="nav-item">
                            <a class="nav-link active" aria-current="page" href="/#">Home</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="/#projects">Projects</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="/#posts">Posts</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
        <div id="ctx">"""

after = """
        </div>
    </body>
    <script defer src="/js/bootstrap.min.js"></script>
    <script defer src="/js/popper.min.js"></script>
</html>
"""

if __name__ == "__main__":
    title = input("Title: ")
    filepath = input("MD Path: ")
    path = input("WEB Path: ")
    date = input("Date: ")
    if date == "":
        date = dt.now().strftime("%Y/%m/%d")
    pre += f"\n<h1>{title}</h1>"
    pre+=md(filepath, extras=["fenced-code-blocks"])
    ctx = pre+after
    with open(path+".html", "w") as f:
        f.write(ctx)
    print(f"""<div id="item">
                <h5>{title}</h5>
                <p>{date}</p>
                <a class="btn btn-outline-danger" href="/posts/{path}.html">Read</a>
              </div>
          """)

