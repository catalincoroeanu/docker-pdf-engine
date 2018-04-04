# Docker Image of PDF Engine

### Details About the Image

The PDF Engine is based on 3 main frameworks/libraries:
  - Django==2.0.3
  - gunicorn==19.7.1
  - WeasyPrint==0.36

### Get started

The Entire Engine is based on Django Framework and it's template rendering to convert the received `context` into a `valid HTML` content and through Weasyprint into a PDF document.

It takes 

### Start the PDF Engine Docker

```
$ docker-compose -f local.yml up --build pdf-engine
```


It will provide:
* [localhost:8200](http://localhost:8200/) - `PDF Engine`



```
PDFTester => GET & POST requests => Only for Test Purpose - Default: Document
```

```
Complex PDFTester =>  GET & POST requests => /?lang=de-ch&doc_type=invoice&font=Proxima&filename=My%20Lovely%20PDF
```
 - /?lang=de-ch&doc_type=project&font=Proxima&filename=My%20Lovely%20PDF
 - lang = [en, de, de-ch] #default=en
 - doc_type = [invoice,(...anything)] #default=invoice
 - font = [Proxima, Lato, Roboto, Saira_Semi_Condensed] # default=Proxima
 - filename = Sample Name Document #default="Sample Title"
 deactivate
 
```
HTML Version =>  GET & POST requests => Only to speed up development for the HTML with Gulp and BrowserSync
```



### Prepare the Python environment:


```
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt

# optional
$ cp .env.example .env
```

## Issues:


