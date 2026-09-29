const express = require("express");
const urlRoute = require('./routes/url');
const { connectToMongoDG } = require('./connection');
const path = require("path");
const URL = require("./models/url");
const staticRoute = require("./routes/staticRouter");

//creating express app
const app = express();
const PORT = 8001;

//ejs connection
app.set('view engine', 'ejs'); //set engine to express
app.set('views', path.resolve('./views')); //give path to express

//MongoDB connection
connectToMongoDG('mongodb://127.0.0.1:27017/short-url');

//middleware
app.use(express.json());
app.use(express.urlencoded({ extended: false }));

//Routes
app.use("/url", urlRoute);
app.use("/", staticRoute)

app.listen(PORT, ()=> console.log(`Server is Listening...\nat port : ${PORT}`));