/**
 * Returns a Mustache template rendered from an html file asynchronously
 * @param {String} template path to html template file
 * @param {Object} object the object to match against the template
 * Usage: loadTemplate("template.hmtl", {x:10}).then((html)=>{console.log(html);})
 */
function loadTemplate(template, object) {
    return new Promise(function(resolve, _reject) {
        $.get(template, (t) => {
            resolve(Mustache.render(t, object))
        })
    })
}