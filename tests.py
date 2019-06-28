import db

d = db.Database("localhost", "webaccess", "cs160mysql", "RESMGTDB")

# d.create_entry("menu", ["some kinda sauce 2", 133.70, "Food"])

d.modify_entry("menu", ("description", "sblounsktchd"), ("description", "saucenado"))


