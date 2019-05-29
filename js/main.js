'use strict';

$.ajax({
    url: "dados.json",
    success: handleMeals,

});

function setaf() {
    var texto = String(document.getElementById("tempbase").className)

    var datah = moment(moment(moment(texto.substring(9))).add(1, "d")).format("YYYY-MM-DD")
    $.ajax({
        url: "dados.json",
        success: (data) => { handleMeals(data, datah) },

    });
};

function setab() {
    var texto = String(document.getElementById("tempbase").className)

    var datah = moment(moment(moment(texto.substring(9))).subtract(1, "d")).format("YYYY-MM-DD")
    $.ajax({
        url: "dados.json",
        success: (data) => { handleMeals(data, datah) },

    });
};

function verdata() {
    var datah = document.getElementById("calendas").value;
    $.ajax({
        url: "dados.json",
        success: (data) => { handleMeals(data, datah) },

    });
};

function handleMeals(meals, datah) {
    var bom = moment(String(datah), moment.HTML5_FMT.DATE)._isValid
    if (bom === false) {
        //console.log(datah)
        //console.log(String(datah))
        //console.log(moment(String(datah),moment.HTML5_FMT.DATE))
        datah = moment().format("YYYY-MM-DD")
    } else {
        var tirar = document.getElementById("tempbase");
        //console.log(tirar)
        tirar.parentNode.removeChild(tirar);
    }

    /*meals.forEach(m => {
        //console.log(m[0])
        loadTemplate("templates/meal.html", m).then((html) => {
            //console.log(html)
            $("#meals").append($(html))
        })
    });*/

    //console.log(datah)
    var resultado = meals.filter(obj => {
        return obj.date === datah
    })

    //console.log(resultado[0])

    if (resultado[0] === undefined) {
        $.get("templates/dice.html", function (response) {
            $("#meals").append($(response));
        });

    } else {
        loadTemplate("templates/meal.html", resultado[0]).then((html) => {
            //console.log(html)
            $("#meals").append($(html))
        })
    }
}


