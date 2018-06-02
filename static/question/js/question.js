'use strict'

var user1 = function() {
    return {
        data: [
            { name: "T. Woods", age: 37 },
            { name: "P. Mickelson", age: 43 }
        ],

        clickHandler: function (event) {
            var randomNum = ((Math.random() * 2 | 0) + 1) - 1;
            console.log(this.data[randomNum].name + " " + this.data[randomNum].age);
        }
    };
};

var user2 = {
    data:[
        {name:"Dan Li", age:37},
        {name:"Miles Li", age:43}
    ],
    
    clickHandler: function (event) {
        var randomNum = ((Math.random () * 2 | 0) + 1) - 1;
        console.log (this.data[randomNum].name + " " + this.data[randomNum].age);
    }
 };

 var anArrayLikeObj = {
     0: "Martin", 
     1: 78, 
     2: 67, 
     3: ["Letta", "Marieta", "Pauline"], 
     length: 4,
};

var user = {
    tournament: "The Masters",

    data: [
        {name:"T. Woods", age:37},
        {name:"P. Mickelson", age:43}
    ],
    
    clickHandler: function (event) {    
        var theUserObj = this;   

        this.data.forEach (function (person) {
            console.log (person.name + " is playing at " + theUserObj.tournament);
        });
    }
};

$(document).ready(function(){
    $('#button-test').click(function(){
        // var u1 = user1();
        // u1.clickHandler.bind(u1)();
        // console.log(Array.prototype.slice.call(anArrayLikeObj, 0));
        user.clickHandler();
    });   
});
