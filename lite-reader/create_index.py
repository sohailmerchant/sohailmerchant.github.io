import os, re

path = r"/mnt/c/Development Work/sohailmerchant.github.io/lite-reader/output"

def html_open_tag():
    html_opening_tag = """<html dir="rtl" lang="ar">
                        <head>
                        <meta name="viewport" content="width=device-width, initial-scale=1">

                            <meta charset="utf-8">

                            <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
                            
                            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
                            <link rel="preconnect" href="https://fonts.gstatic.com">
                            <link href="https://fonts.googleapis.com/css2?family=Amiri&display=swap" rel="stylesheet">
                           
                            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-ygbV9kiqUc6oa4msXn9868pTtWMgiQaeYH7/t7LECLbyPA2x65Kgf80OJFdroafW" crossorigin="anonymous"></script>

                            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">
                            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.3.0/font/bootstrap-icons.css">
                            <script src="https://cdn.jsdelivr.net/npm/mark.js@8.11.1/dist/mark.min.js"></script>
                            
                            <link rel="stylesheet" type="text/css" href="css/style.css"  />
                            <script type="text/javascript" src="js/CollapsibleLists.js"></script>

                        
                            
                        </head>
                        <body>
                            <div class="container-fluid h-100">
                                <!-- Navigation -->
                         <nav class="navbar navbar-light bg-light">
                            <div class="container-fluid">
                                <a class="navbar-brand" href="http://www.kitab-project.org" target="_blank">
                                <img src="./img/kitab-logo.png" width="60px"/></a>
                                
                                <a class="nav-link" aria-current="page" href="https://sohailmerchant.github.io/lite-reader/index.html">Book Index</a>
                               
                            </div>
                            </nav>
                        <div class='row p-30'>
        <div class='col-12 col-sm-12 context' id='container'>
         <div class="card-columns">

        
                            """
    
    return html_opening_tag

def create_index(path):
    index = ""
    for root, dirs, files in os.walk(path):       
        for name in files:
            if name.endswith('html'):
                #print(name)
                
            
                book_title = re.sub(r"(\w)([A-Z])", r"\1 \2", name.split('.')[1])
                author = re.sub(r"(\w)([A-Z])", r"\1 \2", name.split('.')[0])
                date = author[4]
                status = name.split('.')[-2]
                print(status)
                if status == 'completed' or status== 'mARkdown':

                    path = "../lite-reader/output/"+name
                    index += """
                   
                    <div class='card'>
                    <div class='card-body' >
                    <h5 class="card-title"><a href='{path}'>{book_title}</a></h5>
                    
                    <p class="card-text">{author} {date}</p>
                    
                    </div><div class="card-footer"><small class="text-muted">mARkdown</small><small class="text-muted"><a href='{path}'><i class="bi bi-book" title="Read"> </i></a></small><i class="bi bi-check-circle-fill markdown"></i></div></div>
                    
                    """.format(path=path,book_title=book_title,author=author,date=date)
                
                else:
                    path = "../lite-reader/output/"+name
                    index += """
                
                    <div class='card'>
                    <div class='card-body'>
                    <h5 class="card-title"><a href='{path}'>{book_title}</a></h5>

                    <p class="card-text">{author} {date}</p>
                    
                    </div><div class="card-footer"><small class="text-muted"><a href='{path}'><i class="bi bi-book" title="Read"></i></a></small></div></div>
                    
                    """.format(path=path,book_title=book_title,author=author,date=date)
                   
    return index

def html_close():
    html_closing_tag = """</div></div></div></div></body>"""
    return html_closing_tag


index = create_index(path)
#print(index)
full_html = html_open_tag()
full_html += index                         
full_html += html_close()

def create_html_file(html_str):
    print("SAVING AS", "index.html")
    with open("index.html", "w", encoding="utf-8") as e:
        #e.write(html_open())
        e.write(html_str)
        #e.write(html_close())
        
create_html_file(full_html)