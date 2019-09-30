# Cardinal Numbers API
### API to translate an integer number into the cardinal representation in portuguese. 
### The API supports numbers from -99999 to 99999.

## Setup
if you'd like to run the development server as an docker container, use the following command:
```bash
$ docker run -p 3000:5000 lsspelegrino/writenumberapi:v0.1
```
[Repository link on Dockerhub](https://hub.docker.com/r/lsspelegrino/writenumberapi)


Prerequisites:
* Python 3.7

Clone the repository using:  
```bash
$ git clone https://github.com/LSSPelegrino/write_number_api.git
```
Navigate to the created folder and create a virtual environment. I recommend [virtualenvwrapper](https://medium.com/the-andela-way/configuring-python-environment-with-virtualenvwrapper-8745c2895745).


With a virtual enviroment activated, install the requirements running the following command at the project's root:
```bash
(venv) $ pip install -r requirements.txt 
```
After the installation is complete, run:
```bash 
(venv) $ flask run
```
The development server should be running on [localhost](127.0.0.1:5000).

## API

The following actions are allowed:

Action  | HTTP Verb |URL Path       | Description
:------:|:---------:|---------------|---
Read    |```GET```  |```/{number}```|URL to read number in cardinal representation

Usage examples, with HTTPie:

```bash
$ HTTP GET http://localhost:3000/1
{
    "extenso": "um"
}
```

```bash
$ HTTP GET http://localhost:3000/-1042
{
    "extenso": "menos mil e quarenta e dois"
}
```

```bash
$ HTTP GET http://localhost:3000/94587
{
    "extenso": "noventa e quatro mil e quinhentos e oitenta e sete"
}  
```