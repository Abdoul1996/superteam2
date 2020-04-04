db.createUser({
  user: "cscl",
  pwd: "SuperSecret",
  roles: [
    {
      role: "readWrite",
      db: "cscl"
    }
  ]
});

db.books.createIndex({ isbn: 1 });
