var express = require('express');
var router = express.Router();


router.post('/addPoint', function(req, res) {
    console.log("Add Point");
});

module.exports = router;
