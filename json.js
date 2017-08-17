// Installed npm packages: jquery underscore request express
// jade shelljs passport http sys lodash async mocha chai sinon
// sinon-chai moment connect validator restify ejs ws co when
// helmet wrench brain mustache should backbone forever debug


// given an array of x length, ie
// var array = [item0, item1, item2]

// You need to generate a nested json like so:

// state = {
//     ...state,
//     value: {
//         ...state.value,
//         item0: {
//             ...state.value.item0,
//             item1:{
//                 ...state.value.item0.item1,
//                 item2: {
//                     ...state.value.item0.item1.item2,
//                     item3 : [continued-etc]
//                 }
//             }
//         }
//     }
// }

var state={key1:'assinobine', key2:'collegeOfTheRockies'}

var array = [
    {
        name: 'toby',
        age:30,
        gender:'male',
        job: 'developer'
     },

     {
        name: 'dong',
        age:50,
        gender:'male',
        job: 'unemployed'
     },

     {
         name: 'cynthia',
         age:37,
         gender:'female',
         job: 'full-stack-developer'
     },
     {
         name: 'parsa',
         age:27,
         gender:'male',
         job: 'data-analytics'
     }
 ];

//ultimately you want:
// state = {
//     key1:'assinobine',
//     key2:'collegeOfTheRockies',
//     toby: {
//         age:30,
//         gender:'male',
//         dong: {
//             age:50,
//             gender:'male'
//             cynthia: {
//                 age: 37,
//                 gender:'female'
//             }
//         }
//     }
// }

function solution(state, array) {
    var i = 0
    var point = state
    var output = point
    while(array[i]){
        var newObject = {}
        Object.keys(array[i]).forEach(function(key) {
            if (key != "name"){

                newObject[key] = array[i][key]
            }
        })
        point[array[i].name] = newObject
        // This is the trick below here.
        point = newObject
        i+= 1
    }
    console.log(output)
}

//A+
// No its SSS+


function solutionr(state, array, result) {
    console.log("it started");

    if (!result){
        var result = state;
    }

    var newObject = {};
    Object.keys(array[0]).forEach(function(key) {
    if (key != "name"){
        newObject[key] = array[0][key];

    }
    })

    state[array[0]["name"]] = newObject;

    if (array[1]){
        solutionr(newObject, array.slice(1), result);
    }else{
        console.log(JSON.stringify(result));
        return result;
    }
}

// STOP IM TRYING TO READ IT

//k

solutionr(state,array)
