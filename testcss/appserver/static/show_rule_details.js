require([
    "underscore",
    "jquery",
    "models/SplunkDBase",
    "splunkjs/mvc/sharedmodels",
    "splunkjs/mvc",
    "splunkjs/mvc/utils",
    "splunkjs/mvc/tokenutils",
    "splunkjs/mvc/simplexml/ready!"
    ],
    function(_, $, SplunkDModel, sharedModels, mvc, utils) {
        console.log("in function1");

        var unsubmittedTokens = mvc.Components.getInstance('default');
        
        //print values to description panel
        document.getElementById("outputName").innerHTML = "version5";
});
