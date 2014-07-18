# Liaar
=============
A simple tool to create a fake REST API


##How to use?

You should create directories as resources’ namespace and then put JSON files inside them as API methods.

Suppose you have following directory structure:

```
.
..
resources
          |_ .
          |_ ..
          |_ users
                  |_ .
                  |_ ..
                  |_ profile.json
```

And the url would be `http://127.0.0.1:1234/users/profile`.

##Requirements

- Python v2.7
- Twisted v14.0

##License
MIT
